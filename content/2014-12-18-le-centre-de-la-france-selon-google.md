Title: Le centre de la France selon Google
Date: 2014-12-18 11:12
Tags: lang:fr, google, jq, curl, geoip, france, tresor
Slug: le-centre-de-la-france-selon-google
---
C'était la prise de conscience rigolote de ce matin :)

Petite explication: plusieurs des services web de géolocalisation gracieusement fournis par Google utilisent la même interface (API). Cette interface requiert de définir une "zone de travail" géographique dans laquelle on va ensuite pouvoir interroger Google sur des adresses, des itinéraries, etc.

La façon la plus simple de spécifier cette zone est d'indiquer au service les coordonnées du centre d'un carré géographique. Exemple pour la France:

![](/lucas/blog/content/images/2014/Dec/le_centre_de_la_France_square.png)

Or Google fournit un valeur par défaut précise pour ces coordonnées...

    $ curl -s https://maps.googleapis.com/maps/api/geocode/json?address=France | jq '..|objects|.location//empty'
    {
      "lat": 46.227638,
      "lng": 2.213749
    }

Où se trouve donc le centre de la France alors ? Pas très loin de Montluçon il semblerait :

![](/lucas/blog/content/images/2014/Dec/le_centre_de_la_France_map.jpg)

Vous seriez pas curieux de creuser dans cette clairière vous ? Je parie qu'un trésor nous attend...

![](/lucas/blog/content/images/2014/Dec/le_centre_de_la_France_satelite.jpg)