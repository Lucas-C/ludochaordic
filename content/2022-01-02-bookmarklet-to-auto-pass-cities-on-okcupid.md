Title: Bookmarklet to auto-pass cities on OkCupid
Date: 2022-01-02 18:30
Tags: lang:en, html, okcupid, bookmarklet, javascript, open-source, prog
---
<!-- Com'
* https://www.reddit.com/r/OkCupid/
* https://webapps.stackexchange.com/questions/60101/why-is-okcupid-showing-me-matches-who-live-more-than-5-kilometers-away
-->
<a href="https://www.okcupid.com"><img class="logo" alt="OkCupid logo" src="https://lucas-c.github.io/okcupid-auto-pass-cities/OkCupid-logo.jpg"></img></a> is great!

One things that annoys me a little though,
is that I often get matches for **people too far away** from where I live,
even with the **distance filter** set in my _Settings_:

<img class="screenshot" src="https://lucas-c.github.io/okcupid-auto-pass-cities/OkCupid-distance-filter.jpg">

Hence I wrote some simple Javascript code that **auto-pass matches for a list of given cities**.
<details>
    <summary>Javascript snippet</summary>
    <pre><code>const CITIES = 'London,Paris';
function autoPassCities() {
    const loc = document.getElementsByClassName('card-content-header__location')[0].textContent;
    if (CITIES.split(',').some(city => loc.endsWith(city))) {
        console.log('AutoPass:', loc);
        document.getElementsByClassName('pass')[0].click();
    }
    setTimeout(autoPassCities, 500);
}
autoPassCities();</code></pre>
</details>

You can generate **your own [bookmarklet](https://en.wikipedia.org/wiki/Bookmarklet)**
for the cities you wish to exclude
on this page: <https://lucas-c.github.io/okcupid-auto-pass-cities/>

<style>
img.logo { display: initial; width: 6rem; border-radius: 2rem; }
img.screenshot { width: 30rem; }
</style>
