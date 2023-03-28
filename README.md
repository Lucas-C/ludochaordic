
    pip install -r requirements.txt
    invoke livereload
    invoke publish -- -D

The [pelican-plugins](https://github.com/getpelican/pelican-plugins)
repositoriy need to be present in the parent directory, under this name.

In cass of `[pelican] CRITICAL OSError: [Errno 18] Invalid cross-device link` under WSL:

    export TMPDIR=/c/Temp


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>
