Title: [EN] Extracting setup_requires dependencies out of a setup.py
Date: 2017-07-04 12:07
Tags: python, setup-py, dependencies
Slug: en-extracting-setup_requires-dependencies-out-of-a-setup-py
---
I ended up not using this code, but it may be useful to others:

- `mock_setup_provider.py`:
```
import sys
from unittest.mock import Mock

class MockSetupProvider(Mock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.captured_setup_requires = set()
    def setup(self, *args, **kwargs):
        self.captured_setup_requires.update(kwargs.get('setup_requires'))
```

- `setup_extractor.py`:
```
import sys
from .mock_setup_provider import MockSetupProvider

def extract_setup_requires(setup_dir_path):
    real_setuptools = sys.modules.get('setuptools')
    real_distutils_core = sys.modules.get('distutils.core')
    sys.path.insert(0, setup_dir_path)
    try:
        mock_setup_provider = MockSetupProvider()
        sys.modules['setuptools'] = sys.modules['distutils.core'] = mock_setup_provider
        import setup
        return mock_setup_provider.captured_setup_requires
    finally:
        sys.path.pop(0)
        sys.modules.get('distutils.core') = real_distutils_core
        sys.modules.get('setuptools') = real_setuptools
```

- `test_setup_extractor.py`:
```
from setup_extractor import extract_setup_requires

def test_ok():
    assert extract_setup_requires('tests-fixtures') == set(['damn42'])
```

- `test-fixtures/setup.py`:
```
from setuptools import setup, find_packages

setup(
    name='toto',
    version='1.2.3',
    install_requires=['dummy'],
    setup_requires=['damn42'],
)
```
