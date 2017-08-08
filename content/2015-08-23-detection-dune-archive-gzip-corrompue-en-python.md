Title: Détection d'une archive gzip corrompue en Python
Date: 2015-08-23 16:08
Tags: lang:fr, python, gzip, zlib, requests, crc, open-data, meteo, ipython
Slug: fr-detection-dune-archive-gzip-corrompue-en-python
---
Il y a quelques jours, un ami m'a demandé de jeter un oeil à un problème qu'il recontrait: alors qu'il analysait des données de [donneespubliques.meteofrance.fr](http://donneespubliques.meteofrance.fr) dans un [IPython notebook](http://ipython.org/notebook.html), en utilisant la fantastique lib [requests](http://docs.python-requests.org), il a été confronté à un bug étrange:

> Mon soucis c'est que ma requête fonctionne très bien de 1996 à février 2015, mais après de mars 2015 à août 2015 ma requête ne me retourne que les données des premiers jours de chaque mois inexplicablement.

Après quelques essais infructueux à bases d'examens d'entêtes HTTP et de `python -m trace`, j'ai finalement trouvé une piste intéressante:
```python
import requests, urllib2, zlib
from sh import gunzip
ERRONEOUS_CSV_URL = 'https://donneespubliques.meteofrance.fr'\
        '/donnees_libres/Txt/Synop/Archive/synop.201503.csv.gz'

response = requests.get(ERRONEOUS_CSV_URL)
print('[requests] Response Content-Encoding: {}'.format(
        response.headers['content-encoding']))
print('[requests] => Uncompressed CSV lines count: {}'.format(
        len(response.content.splitlines())))

response_content = urllib2.urlopen(ERRONEOUS_CSV_URL).read()
csv_content = zlib.decompress(response_content, zlib.MAX_WBITS|16)
print('[urllib2] + zlib => Uncompressed CSV lines count: {}'.format(
        len(csv_content.splitlines())))
csv_content = gunzip(_in=response_content)
print('[urllib2] + gunzip => Uncompressed CSV lines count: {}'.format(
        len(csv_content.splitlines())))
```
Et le résultat:
```
[requests] Response Content-Encoding: gzip
[requests] Uncompressed CSV lines count: 61
[urllib2] + zlib => Uncompressed CSV lines count: 61
[urllib2] + gunzip => Uncompressed CSV lines count: 13516
```

Le problème vient donc de `zlib` !
En effet, `requests` décompresse automatiquement le fichier téléchargé avec le module standard `zlib` lorsqu'il détecte l'entête HTTP `Content-Encoding: gzip`.
Mais lorsqu'on utilise la bibliothèque standard `urllib2` avec la command unix `gunzip`, on récupère bien bien le contenu décompressé correct !

Je me suis donc mis en tête de vérifier le contenu de l'archive `.gz` pour vérifier si elle n'était pas corrompue, et plus précisément au niveau de ses entêtes `gzip`.
Après quelques recherches sur le web, à part un très peu loquace `gzip -t` qui vérifie les archives, je n'ai trouvé aucune commande qui afficherait simplement les en-têtes `gzip` d'une archive compressée.

En définitve, j'ai donc bricolé un [petit script](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/gzip_headers_reader.py) pour examiner ça:
```
$ BASE_REPO_URL=https://rawgit.com/Lucas-C/linux_configuration/master
$ BASE_CSV_URL=https://donneespubliques.meteofrance.fr/donnees_libres
$ wget -q \
    $BASE_REPO_URL/languages/python/gzip_headers_reader.py \
    $BASE_CSV_URL/Txt/Synop/Archive/synop.201502.csv.gz \
    $BASE_CSV_URL/Txt/Synop/Archive/synop.201503.csv.gz
$ for f in synop*.csv.gz; do echo $f; python2.7 gzip_headers_reader.py $f | tail -n 8; done
```
Et le résultat:
```
synop.201502.csv.gz
CRC32: 694988689
  -> CRC32 COMPUTED FROM DECOMPRESSED DATA: 694988689
ISIZE: 3575777 bytes
    (size of the original (uncompressed) input data modulo 2^32)
  -> ACTUAL COMPRESSED DATA LENGTH: 564016 bytes
  -> ACTUAL DECOMPRESSED DATA LENGTH: 3575777 bytes
  -> ZLIB: len(unused_data)=0

synop.201503.csv.gz
CRC32: 856966149
  -> CRC32 COMPUTED FROM DECOMPRESSED DATA: 2470910129
ISIZE: 14979 bytes
    (size of the original (uncompressed) input data modulo 2^32)
  -> ACTUAL COMPRESSED DATA LENGTH: 682100 bytes
  -> ACTUAL DECOMPRESSED DATA LENGTH: 16436 bytes
  -> ZLIB: len(unused_data)=678973
```

On voit donc bien que le champ `ISIZE` de l'archive de mars 2015 est incorrect, et que 99.5% des données compressées n'ont pas été extraites par `zlib`.

Pour ce week-end je vais m'arrêter là, mais il serait intéressant de poursuivre un peu plus loin:

- contacter [donneespubliques.meteofrance.fr](http://donneespubliques.meteofrance.fr) pour les prévenir du problème de corruption d'archive
- regarder dans le [code source de `zlib`](https://hg.python.org/cpython/file/tip/Modules/zlibmodule.c) pourquoi la vérification du `CRC32` et du `ISIZE` n'est pas faite, et peut-être proposer un patch sur le code source CPython pour l'ajouter optionnellement. Et si `gunzip` peut le faire, `zlib` devrait aussi être capable de décompresser un `.gz` aux entêtes incorrectes !!

**EDIT**: Voici une solution rapide à ce problème, utilisant uniquement des modules standards, si jamais vous êtes coincé avec ce type d'archive `.gz` corrompue:
```python
import gzip, requests, StringIO
response = requests.get(URL, stream=True)
gzipped_file_obj = StringIO.StringIO(response.raw.read())
with gzip.GzipFile(fileobj=gzipped_file_obj, mode='rb') as gunzipped_file_obj:
    decoded_content = gunzipped_file_obj.read()
```

Comme `gzip` utilise `zlib` et ne semble pas présenter ce problème de décompression, le bug initial provient peut-être d'une mauvaise utilisation de zlib par `requests`.
À investiguer...