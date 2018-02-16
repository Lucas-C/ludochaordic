Title: Reverse engineering de l'API HTTP derrière une app android
Date: 2018-02-14 23:30
Tags: lang:fr, lubie, reverse-engineering, android, fail
Slug: reverse-engineering-the-http-api-behind-an-android-app
---

Ces dernières 24h, j'ai eu cette lubie stupide de vouloir utiliser l'API Tickets Restaurant.
Une API qui n'est pas documentée. Dont le site est en ASP.NET (beurk). Qui a une app officielle android.

Ahah !

Bref, j'ai tenté de _reverse-engineer_ un APK alors que je n'ai même pas de _smartphone_ 🤦

<img alt="reverse engineer" src="images/2018/02/reverse_engineer.jpg">

Au passage, je recommande vivement [apktool](https://ibotpeaches.github.io/Apktool/),
pour extraire le contenu d'un APK,
et [jadx](https://github.com/skylot/jadx) pour décompiler le bytecode Dex en du code Java à peu près correct.
En tout cas, même s'il fait un peu plus d'erreurs (oublis de déclarations de variables par exemple),
il produit un code bien plus clair que [JD-GUI](http://jd.benow.ca) (il extrait même les noms de variables !),
et l'interface graphique est bien pratique.

Le résultat au final ?

![Ninja smoke bomb fail](images/2018/02/fail.gif)

Un bon gros _fail_.

Alors oui, j'ai eu la joie de réduire plusieurs milliers de lignes de Java très répétitives et pleines de fautes à [une centaine de lignes de Python](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/edenred.py).
Et c'était super fun de voir mes appels à cette fichue API SOAP retourner des erreurs incompréhensibles d'un _backend_ visiblement en Ruby On Rails.

Mais au final, pas moyen de récupérer mon solde programmatiquement 😢

Au final j'en viens vraiment à douter que cette app fonctionne, surtout vu [les avis dessus](https://play.google.com/store/apps/details?id=com.endenred.tr.fr&hl=fr).
Donc si quelqu'un avec un ordinateur de poche pouvait me le confirmer, ça me ferait bien plaisir ! :D

<style>
article img {
    display: block;
    margin: 0 auto;
    max-height: 15rem;
}
</style>
