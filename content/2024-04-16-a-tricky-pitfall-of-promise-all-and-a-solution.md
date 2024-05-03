Title: A tricky pitfall of Promise.all() and a solution
Date: 2024-04-16 12:00
Tags: lang:en, javascript, typescript, jest, async, promise, algorithms, prog
---

This article aims to describe a tricky situation that can often occur when using `Promise.all()`,
and a simple solution to this problem.

## The context

[The MDN page for `Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) provides the following description of this function:

> The `Promise.all()` static method takes an iterable of promises as input and returns a single **Promise**. This returned promise fulfills when all of the input's promises fulfill (including when an empty iterable is passed), with an array of the fulfillment values. It rejects when any of the input's promises rejects, with this first rejection reason.

[`Promise.all()` was introduced in the 6th edition of ECMAScript, published in 2015](https://262.ecma-international.org/6.0/#sec-promise.all), when promises were first added as a builtin mechanism in the language, but they were already widely used before, through the use of libraries like [bluebird](http://bluebirdjs.com/docs/why-promises.html).

ECMAScript 2020, the 11th edition, introduced `Promise.allSettled()`, which has a slightly different behaviour:

> The `Promise.allSettled()` static method takes an iterable of promises as input and returns a single **Promise**. This returned promise fulfills when all of the input's promises settle (including when an empty iterable is passed), with an array of objects that describe the outcome of each promise.

Finally, with the advent of `async`, `Promise.all()` & `Promise.allSettled()` can be used to `await` for the completion of several asynchronous functions:
```javascript
await Promise.all([asyncFunc1(), asyncFunc2()]) // can throw an exception

const results = await Promise.allSettled([asyncFunc1(), asyncFunc2()]) // never throw an exception
```

## The problem

`Promise.all()` is a very handy function, but its behaviour regarding error management is actually quite tricky.

Whereas `Promise.allSettled()` requires to check the promises resulting statuses,
the promise produced by `Promise.all()` will **reject** if any of the input promises fails.
And in that case, it means that `await Promise.all(...)` will throw an exception.

But **when `Promise.all()` rejects, some of the input promises can still be executing!**
And this situation is often not considered by developpers.

The following diagram and code snippet demonstrates this problem:

![Diagram explaining a pitfall with Promise.all()](images/2024/04/waitForPromises.drawio.png)

```javascript
async function sleep(durationMs) {
    return new Promise((resolve) => setTimeout(resolve, durationMs));
}

async function sleepAndFail(durationMs) {
  await sleep(durationMs);
  throw new Error(`sleepAndFail(${durationMs}) FAILED`);
};

let promiseStatus = "not-started";
async function sleepAndTrackStatus(durationMs) {
  promiseStatus = "executing";
  await sleep(durationMs);
  promiseStatus = `sleepAndTrackStatus(${durationMs}) SUCCEEDED`;
};

(async function () {
  const failing = sleepAndFail(100);
  const fastSucceeding = sleep(50);
  const slowSucceeding = sleepAndTrackStatus(200);
  try {
    console.log(await Promise.all([
      failing,
      fastSucceeding,
      slowSucceeding,
    ]));
  } catch (error) {
    console.log(error); // -> Error: sleepAndFail(100) FAILED
  }
  console.log("Final promiseStatus for slowSucceeding:", promiseStatus); // -> executing!
})()
```

The problem is that, when an input promise fails, `Promise.all()` will **reject early**, without waiting for the other promises, that can still be processing asynchronously.

This can lead to many problematic situations, where code executed by those other promises perform operations that can conflict with the code executed following the call to `Promise.all()`. For exemple, issues with database connexions or I/O with files can be expected.

In my case, I identified this underlying problem in a situation of cascading failures with a [Jest](https://jestjs.io/fr/) test suite: the code in some asynchronous `afterEach()` methods wasn't properly waiting for shared resources to be cleaned up, when some unit tests were failing, due to a call to `await Promise.all()`.

## The root cause

Out of curiosity, I tried to find out the source code of the implementation of `Promise.all()`.
I think most of its logic lies in the file [src/builtins/promise-all.tq](https://github.com/nodejs/node/blob/main/deps/v8/src/builtins/promise-all.tq) in the V8 JavaScript Engine.
`.tq` files are written in [Torque](https://v8.dev/docs/torque), a high-level language specific to V8 that gets transpiled to C++. Hence, I found it difficult to figure out where the "short-circuit" promise rejection logic happens exactly in the implementation 😅.

For the curious reader, there is a section about the Torque language in the excellent [learning-v8 repo by  Daniel Bevenius](https://github.com/danbev/learning-v8?tab=readme-ov-file#torque).

## A solution

Regarding this problem, `Promise.allSettled()` is a better alternative to `Promise.all()`,
as it waits for the completion of all the promises passed as parameter to this function.
In fact, `allSettled` was introduced to EcmaScript exactly for this reason, as [its original proposal document](https://github.com/tc39/proposal-promise-allSettled) reveals:

> `Promise.allSettled` is unique in always waiting for all of its input values.

However, `Promise.allSettled()` requires that you handle potential rejections yourself, which can be easily forgotten, or create repeated boilerplate code.

The solution that I propose is **a drop-in safe replacement for `Promise.all()`**:

```javascript
/*
 * This function ensures that (1) all the promises provided have completed
 *                        and (2) that a rejection is produced if at least one of those promises is rejected.
 */
async function waitForPromises<T>(promises: Iterable<PromiseLike<T>>) {
  const results = await Promise.allSettled(promises);
  const rejectedResults: PromiseRejectedResult[] = results.filter(
    (result): result is PromiseRejectedResult => result.status === "rejected"
  );
  if (rejectedResults.length === 1) {
    throw rejectedResults[0].reason;
  }
  if (rejectedResults.length > 1) {
    throw new AggregateError(rejectedResults.map((result) => result.reason), `${rejectedResults.length} promises failed`);
  }
  const successfullResults: PromiseFulfilledResult<Awaited<T>>[] = results.filter(
    (result): result is PromiseFulfilledResult<Awaited<T>> => result.status === "fulfilled"
  );
  return successfullResults.map((result) => result.value);
}
```
This is in fact [TypeScript with Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-types), but you can just remove the `: types` and `<T>` to get valid Javascript code:
<details>
  <summary><em>waitForPromises in Javascript</em></summary>
  <pre><code>async function waitForPromises(promises) {
  const results = await Promise.allSettled(promises);
  const rejectedResults = results.filter(result => result.status === "rejected");
  if (rejectedResults.length === 1) {
    throw rejectedResults[0].reason;
  }
  if (rejectedResults.length > 1) {
    throw new AggregateError(rejectedResults.map((result) => result.reason), `${rejectedResults.length} promises failed`);
  }
  return results.map((result) => result.value);
}</code></pre>
</details>

You can test this function by replacing `Promise.all` by `waitForPromises` in the initial code snippet of this article.

Although sometimes the "short-circuit" behaviour of `Promise.all` can be handy, I think that `waitForPromises` is a better, safer alternative in most situations, and should be the go-to default option to `await` the completion ofseveral asynchonous functions.

_(thanks to [Reddit user @senocular](https://www.reddit.com/user/senocular/) for the very relevant feedbacks on this blog post)_

## Further readings

* [GIF Cheatsheets for Javascript Promise API methods @ dev.to](https://dev.to/hem/gif-cheatsheet-for-javascript-promise-api-methods-promise-all-promise-allsettled-promise-race-promise-any-1l2o#promiseallsettled)
* [Avoid the Promise.all pitfall! Rate limit async function calls by Mike Talbot @ dev.to](https://dev.to/miketalbot/avoid-the-promiseall-pitfall-38ik) and also, on the same suject, [ Beware of Promise.all @ dev.to](https://dev.to/jdorn/beware-of-promiseall-3pph)
* [Beware of short-circuiting Promise combinators in JavaScript @ medium.com](https://medium.com/@volodymyrfrolov/beware-of-short-circuiting-promise-combinators-in-javascript-bbb5b7a9e70f) : an older article from 2019 already raising a similar warning

<!-- Com' :
* [x] https://news.ycombinator.com/item?id=40246656
* [x] https://www.reddit.com/r/javascript/comments/1cj6vd6/a_tricky_pitfall_of_promiseall_and_a_solution/
* [x] https://news.humancoders.com/t/javascript - lucas.cimon+humancoders
* [ ] https://dev.to/lucasc/
* [ ] https://medium.com/@Lucas_C/
-->
