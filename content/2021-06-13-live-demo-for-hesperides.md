Title: Live demo for Hesperides!
Date: 2021-06-13 14:30
Tags: lang:en, libre-software, open-source, oui.sncf, hesperides, heroku, java, angularjs, configuration-management, hexagonal-architecture, cqrs, event-sourcing, ddd, ladr, github-actions, jenkins, python, prog
Slug: live-demo-for-hesperides
---

![Hesperides logo](images/2021/06/hesperides.png)

Today I finally took the time to put up a **live demo website** for **Hesperides**!

<https://hesperides.herokuapp.com>

Hesperides is an open source tool dedicated to **configuration management**:
it stores **applications properties** and [mustache](https://mustache.github.io) templates for **configurations files**.
It is **strongly hierarchized** based on few main concepts: **modules**, **applications** and **environments**.

Hesperides has two main components: a [REST API backend](https://github.com/voyages-sncf-technologies/hesperides)
and a [web frontend](https://github.com/voyages-sncf-technologies/hesperides-gui).
It has a companion [CLI written in Python](https://github.com/voyages-sncf-technologies/hesperides-cli)
a dedicated [Jenkins shared lib](https://github.com/voyages-sncf-technologies/hesperides-jenkins-lib),
and it has been used in production for more than 5 years.

My first contribution to this project dates from 2017,
but it's in 2019 that I extensively worked with [Thomas L'Hostis](https://github.com/thomaslhostis)
on fully re-writing its Java backend.

Following this major overhaul, many interesting methodologies & tools were used on this project:

* [Hexagonal architecture & CQRS](https://github.com/voyages-sncf-technologies/architecture-hexagonale-cqrs)
* [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
* [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)
* [BDD testing](https://en.wikipedia.org/wiki/Behavior-driven_development)
* [Lightweight Architecture Decision Records](https://github.com/voyages-sncf-technologies/hesperides/tree/master/documentation/lightweight-architecture-decision-records)
* containerization using `Docker`
* fully automated daily deployments, partially based on [GitHub Actions pipelines](https://docs.github.com/en/actions)

Over the years, many contributors helped on this project: [backend contributors](https://github.com/voyages-sncf-technologies/hesperides/graphs/contributors) - [frontend contributors](https://github.com/voyages-sncf-technologies/hesperides-gui/graphs/contributors).
Special shout-out to **Sylvain Maillard**, **Adrien Auffredou**, **Victor Salaun**, **Mamadou Bhoye Barry**
and the persons who took part in the Hesperides workshops: thank you all for your great work!

The live demo website is hosted on [Heroku](https://www.heroku.com).
I wrote down a short tutorial on how this was done here:<https://voyages-sncf-technologies.github.io/hesperides-gui/start.html#heroku>.
