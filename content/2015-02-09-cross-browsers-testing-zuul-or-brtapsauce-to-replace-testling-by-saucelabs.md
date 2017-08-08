Title: Cross-browsers testing : zuul or sauce-tap-runner to replace testling by SauceLabs ?
Date: 2015-02-09 16:02
Tags: lang:en, javascript, testling, tap, unit-testing, browser-testing, zuul, saucelabs, travis-ci, mocha, quint, jasmine, ecovoit
Slug: en-cross-browsers-testing-zuul-or-brtapsauce-to-replace-testling-by-saucelabs
---
[Since July 2014](//github.com/substack/testling/issues/88), **Substack** great cross-browsers testing tool `testling` has been unavailable.

Today I was looking for an alternative to use with [**ecovoit**](https://github.com/Lucas-C/ecovoit), my carpooling search engine. [Saucelabs](//saucelabs.com/docs/onboarding) is a very interesting solution, and is free for open-source projects.

Now I found 2 tools to easily launch your Javascript TAP tests to SauceLabs:

- [zuul](//github.com/defunctzombie/zuul)
- [sauce-tap-runner](//github.com/conradz/sauce-tap-runner) + potentially [brtapsauce](//github.com/rvagg/brtapsauce)

There is a comparison table to choose betwen the two :

<table>
  <thead>
    <tr>
      <th></th>
      <th>zuul</th>
      <th>sauce-tap-runner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Project maturity</td>
      <td>352 commits<br>20 contributors</td>
      <td><< 50 commits<br>1 contributor</td>
    </tr>
    <tr>
      <td>Project vitality</td>
      <td>last commit 7 days ago</td>
      <td>last commit one year ago</td>
    </tr>
    <tr>
      <td>Run tests locally</td>
      <td><code>zuul -- test</code></td>
      <td><code>npm run-script test-local</code></td>
    </tr>
    <tr>
      <td>Configuration file</td>
      <td><code>.zuul.yml</code> + <code>.zuulrc</code></td>
      <td><code>test/sauce.js</code></td>
    </tr>
    <tr>
      <td>Supported test frameworks</td>
      <td>mocha, tape, qunit, jasmine</td>
      <td>TAP</td>
    </tr>
    <tr>
      <td>Module to interact with SauceLabs</td>
      <td>included <a href="https://github.com/defunctzombie/zuul/blob/master/lib/SauceBrowser.js">SauceBrowser.js</a></td>
      <td><a href="https://github.com/conradz/sauce-tap-runner">sauce-tap-runner</a> downloads & launches the Sauce Connect JAR</td>
    </tr>
    <tr>
      <td>Bonus points</td>
      <td><a href="https://github.com/defunctzombie/zuul/wiki/quickstart">great tutorial</a> including how to setup Travis CI with secured credentials</td>
      <td></td>
    </tr>
  </tbody>
</table>