
    pip install -r requirements.txt
    invoke livereload
    invoke publish -- -D

The [pelican-plugins](https://github.com/getpelican/pelican-plugins)
repositoriy need to be present in the parent directory, under this name.

In case of `[pelican] CRITICAL OSError: [Errno 18] Invalid cross-device link` under WSL:

    export TMPDIR=/c/Temp

In case of repeated `FileNotFoundError: [Errno 2] No such file or directory: 'output/thumbnails/...`:

    while ! python $opt/pelican-plugin-image-preview-thumbnailer/image_preview_thumbnailer.py output/pages/images-libres-de-droits.html; do sleep .5; done

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>
