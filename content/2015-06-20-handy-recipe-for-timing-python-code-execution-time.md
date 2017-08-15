Title: Handy recipe for timing Python code execution time
Date: 2015-06-20 15:06
Tags: lang:en, python, recipe, trace, decorator, context-manager, time, prog
Slug: handy-recipe-for-timing-python-code-execution-time
---
The `timeit` module is useful for micro benchmarks, but does not allow to measure execution time of large snippets, as it requires the code tested to fit in a string.
Hence, I went looking for a context or decorator-based solution. And I found [this bug report](https://bugs.python.org/issue19495) commented by Guido van Rossum, recommending a few recipes.

Here is another one, that can be used either as a decorator or as a "with-context", combining the following inspirations:

- [timeit.Timer.timeit](https://hg.python.org/cpython/file/tip/Lib/timeit.py#l165) from the standard library
- <http://dabeaz.blogspot.it/2010/02/function-that-works-as-context-manager.html>
- <http://code.activestate.com/recipes/577896/>

```python
import gc
from contextlib import contextmanager
from functools import wraps
from time import perf_counter  # used by timeit module

def trace_exec_time(end_callback=None, **kwargs):
    @contextmanager
    def benchmark(**ctx_kwargs):
        gc_was_enabled = gc.isenabled()
        gc.disable()
        start = perf_counter()
        yield ctx_kwargs
        end = perf_counter()
        ctx_kwargs['exec_duration'] = end - start
        if end_callback:
            end_callback(ctx_kwargs)
        if gc_was_enabled:
            gc.enable()
    if end_callback:
        def decorator(func):
            @wraps(func)
            def wrapper(*func_args, **func_kwargs):
                with benchmark(func_args=func_args, func_kwargs=func_kwargs,
                               func_name=func.__name__, **kwargs):
                    return func(*func_args, **func_kwargs)
            return wrapper
        return decorator
    else:
        return benchmark(**kwargs)
```

The triple args/kwargs variable shadowing is ugly, but that keeps the code short.

There are some usage examples:

    @trace_exec_time(end_callback=print)
    def add(a, b):
        return a + b

    add(2, b=3)  # -> {'func_kwargs': {'b': 3}, 'exec_duration': 1.9-06, 'func_args': (2,), 'func_name': 'add'}

    with trace_exec_time(name='Heavy calculation') as report:
        result = big_compute(list_of_things)
    print(report['name'], "%0.3fs" % report['exec_duration'])  # -> Heavy calculation 10.576s

__[UPDATED] on 2016/08/04__

With an aggregated list of all your timings, if you don't have `numpy`/`scipy` at hand, here is a handy recipe to compute some useful statistics out of them (requires Python 3 `statistics` module for `pstdev`):
```
import statistics

def compute_timing_stats(timings_in_ms):
    timings_in_ms = sorted(timings_in_ms)
    total = sum(timings_in_ms)
    return = {
        'count': len(timings_in_ms),
        'mean': total / len(timings_in_ms),
        'p00_min', timings_in_ms[0],
        'p01', percentile(timings_in_ms, 1),
        'p10', percentile(timings_in_ms, 10),
        'p50_median', percentile(timings_in_ms, 50),
        'p90', percentile(timings_in_ms, 90),
        'p99', percentile(timings_in_ms, 99),
        'p100_max', timings_in_ms[-1],
        'pstdev': statistics.pstdev(timings_in_ms),
        'sum': total
   }

def percentile(sorted_data, percent):
    """
    Find the percentile of a list of values.

    @parameter sorted_data - is an ALREADY SORTED list of values
    @parameter percent - a float value from 0.0 to 1.0.

    @return - the percentile of the values
    """
    assert 0 <= percent < 1
    index = (len(sorted_data)-1) * percent
    return sorted_data[int(index)]
```
