Title: World map of an open-source project contributors
Date: 2021-06-28 12:00
Lang: en
Tags: lang:en, libre-software, open-source, fpdf2, geocoding, maps, cartography, leafletjs, github, github-actions, python, prog
Slug: world-map-of-an-open-source-project-contributors
---
<!-- Com' :
* Feature suggested: https://github.com/all-contributors/all-contributors/issues/537
-->

I have been amazed recently at the **diversity** of contributors on the [fpdf2](https://github.com/PyFPDF/fpdf2) project,
coming from all around the world!

Then I thought it would be nice to visualize this diversity by building a world map
of all contributors locations.
There it is:

[![](images/2021/06/contributors-map.png)](https://pyfpdf.github.io/fpdf2/contributors.html)

Click on the image to access an up-to-date online version.

The web page is built by a Python script that queries the GitHub v3 API
to retrieve all the locations of the project contributors,
if this information is provided on their profile page.

Then [LeafletJS](https://leafletjs.com)
and [Leaflet Control Geocoder](https://github.com/perliedman/leaflet-control-geocoder)
are used to place all contributors on a world map.

Finally, the page is built & deployed by the GitHub Actions pipeline on every push on the `master` branch.

I tried to make it easy to reuse for other projects,
and it is under [CC-0 license](https://creativecommons.org/publicdomain/zero/1.0/deed.en),
so **feel free to add a similar contributor world maps to your favorite open-source project!**
