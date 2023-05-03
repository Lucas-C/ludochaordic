Title: Bonnes pratiques Gitlab CI
Date: 2021-07-28 22:00
Tags: lang:fr, oui.sncf, usine-logicielle, gitlab-ci, git, continuous-integration, best-practices, performances, security, dependency-confusion, cache, secrets, dependencies, renovate, sonar, java, maven, python, pip, pip-compile, nodejs, npm, docker, prog
Slug: bonnes-pratiques-gitlab-ci
---

![Logo Gitlab](images/2021/07/gitlab-ci.png)

À [E-voyageurs Technologies](https://www.oui.sncf), je travaille au sein d'une équipe en charge de l'**usine logicielle**,
qui administre depuis plusieurs années une instance Gitlab _self-hosted_.

Cet article contient quelques-unes de nos recommandations à l'intention des utilisateurs de notre Gitlab,
ayant pour but à la fois **améliorer les performances de leurs _pipelines_**,
et **limiter leur impact en termes de ressources** sur cette instance Gitlab partagée entre des dizaines d'équipes.
Un dernier volet rassemble quelques points de **sécurité**.

Ces conseils sont essentiellement issus de mon expérience au fil des années,
mais recoupent également des recommandations officielles de Gitlab.
J'espère qu'en les partageant ici ils pourront être utiles à la communauté qui gravite autour de ce bel outil.
Merci à Christophe, Etienne, Gilles, Jérôme & Raphaël pour la relecture.

- [Shallow cloning avec GIT_DEPTH=1](bonnes-pratiques-gitlab-ci.html#shallow-cloning-avec-git_depth=1)
- [Cache](bonnes-pratiques-gitlab-ci.html#cache)
- [Artefacts](bonnes-pratiques-gitlab-ci.html#artefacts)
- [Retry](bonnes-pratiques-gitlab-ci.html#retry)
- [Évitez les déploiements depuis les forks](bonnes-pratiques-gitlab-ci.html#evitez-les-deploiements-depuis-les-forks)
- [Sécurité - Lockez vos versions pour rendre vos builds reproductibles](bonnes-pratiques-gitlab-ci.html#securite---lockez-vos-versions-pour-rendre-vos-builds-reproductibles)
- [Sécurité - Services intégrés](bonnes-pratiques-gitlab-ci.html#securite---services-integres)

## Shallow cloning avec GIT_DEPTH=1

Afin de **raccourcir vos temps d'exécution** et **limiter la quantité de données transitant sur le réseau**,
vous pouvez définir cette variable d'environnement afin que Gitlab ne récupère
qu'**un seul commit d'historique** de votre repository avant d'exécuter votre pipeline.

Cette variable peut-être définie dans le `.gitlab-ci.yml`, au niveau des variables CI/CD de votre repo,
ou même plus largement au niveau des variables de CI/CD de votre groupe Gitlab.

Plus d'information ici : <https://docs.gitlab.com/ee/ci/yaml/#configure-runner-behavior-with-variables>

De même, si vous clonez manuellement un repo `git` dans vos _pipelines_, pensez à employer `git clone --depth 1`.

Pour les très gros repos, Gitlab suggère quelques optimisations possibles,
notamment en configurant `GIT_CLEAN_FLAGS` & `GIT_FETCH_EXTRA_FLAGS` : <https://docs.gitlab.com/ee/ci/large_repositories/>

## Cache

Il est vraiment simple et très efficace de mettre en cache entre vos _builds_ successifs
les dépendances de vos applications rapatriées par votre outil favori (Maven, Gradle, Go, npm, pip...) :
```yaml
default:
  cache:
    paths:
      - .cache/ansible
      - .cache/pip
      - .gradle/caches
      - .gradle/wrapper
      - .m2/repository
      - cache/bundler  # Ruby
      - node_modules
```

Le dossier de cache doit obligatoirement être relatif au dossier de _build_ de votre pipeline.
Pour certaines technos, cela requiert de configurer le dossier de cache employé par votre _package manager_
via des variables d'environnement :
```yaml
variables:
  ANSIBLE_ROLES_PATH: "$CI_PROJECT_DIR/.cache/ansible"
  GEM_PATH: "$CI_PROJECT_DIR/cache/bundler/ruby/2.1.0"
  GRADLE_HOME: "$CI_PROJECT_DIR"
  MAVEN_OPTS: "-Duser.home=$CI_PROJECT_DIR"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
```

Définir une `cache:key` est souvent une bonne idée, ainsi éventuellement qu'une `CACHE_FALLBACK_KEY`.
Pour plus de détails, vous pouvez vous référer aux [Good caching practices](https://docs.gitlab.com/ee/ci/caching/#good-caching-practices) & [Common use cases for caches](https://docs.gitlab.com/ee/ci/caching/#common-use-cases-for-caches) de la documentation Gitlab CI.

Notez également que le niveau de compression du cache est configurable via la variable [CACHE_COMPRESSION_LEVEL](https://docs.gitlab.com/ee/ci/runners/configure_runners.html#artifact-and-cache-settings), et la vitesse de compression via [FF_USE_FASTZIP](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/26490).

Enfin, pour approfondir le sujet, vous pouvez lire la manière dont Gitlab optimise sa gestion de cache pour son propre projet `git` : <https://docs.gitlab.com/ee/development/pipelines.html#caching-strategy>

## Artefacts

Lorsque vous faites transiter des [artefacts](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html)
entre différentes étapes de vos _pipelines_, pensez à [**toujours configurer une courte durée de rétention maximale**](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html#create-job-artifacts)
afin de limiter l'empreinte disque de vos _pipelines_ :
```yaml
artifacts:
  paths:
    - target/myapp.jar
  expire_in: 1 day
```

Notez également que le niveau de compression des artefacts est configurable via la variable [ARTIFACT_COMPRESSION_LEVEL](https://docs.gitlab.com/ee/ci/runners/configure_runners.html#artifact-and-cache-settings), et la vitesse de compression via [FF_USE_FASTZIP](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/26490).

Enfin, pour approfondir le sujet, vous pouvez lire la manière dont Gitlab optimise sa gestion d'artefacts pour son propre projet `git` : <https://docs.gitlab.com/ee/development/pipelines.html#artifacts-strategy>

## Retry

Si certaines étapes de votre pipeline ont tendance à tomber en échec de temps en temps,
par exemple à cause d'une instabilité irrégulière d'un service externe, vous pouvez configurer cette étape pour se relancer un 2e fois en cas d'échec :
```yaml
retry: 1
```

Plus de détails ici : <https://docs.gitlab.com/ee/ci/yaml/#retry>

⚠️ ATTENTION : `retry` peut avoir des effets secondaires néfastes, comme ajouter de la charge sur Gitlab ou de marteler inutilement des services externes.
Ne le mettez en place que si cela résout effectivement des instabilités temporaires.
Bien souvent, résoudre le problème "de fond" de l'instabilité sera la meilleure solution.

## Évitez les déploiements depuis les _forks_

Il est courant d'effectuer certaines étapes d'une pipeline uniquement sur la branche `master` / `main`,
comme la publication de livrables (telle une image Docker) ou le déclenchement d'action de déploiement.

La syntaxe suivante est alors souvent employée :
```yaml
only:
  - master
```

Néanmoins, le risque avec cette règle ci-dessus est que **ces actions seront tout même effectuées sur les branches `master` / `main` des _forks_** de votre repo !

N'importe quel contributeur de votre projet peut alors déclencher un déploiement par mégarde en déclenchant la pipeline de leur _fork_.
Bien sûr, dans de nombreux cas ce déploiement sera un échec si, par exemple, votre pipeline nécessite des variables auxquels les _forks_ n'ont pas accès.

Néanmoins, pour éviter tout risque, vous pouvez employer la syntaxe suivante qui indique précisément le groupe Gitlab du repo autorisé à effectuer les actions de déploiement :
```yaml
rules:
  - if: '$CI_PROJECT_PATH == "group-name/repo-name"'
```

## Sécurité - Lockez vos versions pour rendre vos builds reproductibles

Selon le _package manager_ que vous employez, les outils varient, mais l'idée est la même :
**versionner sous git votre arbre complet de dépendances**, avec un fichier de _lock_,
pour que la construction de votre livrable dans une version donnée ne puisse jamais changer
si une de vos dépendances est mise à jour plus tard sur un _registry_.

Plus d'infos sur l'approche générale :

[![Logo Reproductible Builds](images/2021/07/reproductible-builds.svg)](https://reproducible-builds.org)

* Avec **Maven (Java)** :

    + N'employez jamais les mots-clefs dépréciés `LATEST` ou `RELEASE` dans vos `pom.xml`, qui peuvent vous exposer à des attaques de type _Dependency Confusion_ ([Maven 3.x Compatibility Notes on RELEASE and LATEST metaversions](https://cwiki.apache.org/confluence/display/MAVEN/Maven+3.x+Compatibility+Notes#Maven3.xCompatibilityNotes-PluginMetaversionResolution)).
    De même, n'employez pas les _versions ranges_ et préférez-y l'emploi du [plugin Versions](https://www.mojohaus.org/versions-maven-plugin/).
    + Utilisez le [plugin dependency-check](https://jeremylong.github.io/DependencyCheck/dependency-check-maven/) dans votre pipeline, et définissez `failBuildOnCVSS` pour que son exécution interrompe le _build_ en cas de vulnérabilité détectée

* Avec **npm (NodeJS)** :

    + Invoquez `"npm ci"` plutôt que `"npm install"` dans vos _pipelines_ afin d'employer le `package-lock.json` et d'assurer que vos _builds_ sont toujours identiques ([article explicatif en anglais](https://betterprogramming.pub/npm-ci-vs-npm-install-which-should-you-use-in-your-node-js-projects-51e07cb71e26))
    + Si possible, lorsque vous publiez vos propres packages, employez des [`@scopes`](https://docs.npmjs.com/cli/v7/using-npm/scope).
    Si vous publiez vos packages "scopés" sur un _registry_ privé, pensez à créer également le `@scope` sur <https://npm.org> (sans pour autant y publier de package), pour évitez tout risque de _Dependency Confusion_.
    + Invoquez [npm audit](https://docs.npmjs.com/cli/v7/commands/npm-audit) dans vos _pipelines_ pour détecter d'éventuelles vulnérabilités dans vos dépendances : en cas de [code de retour non 0](https://docs.npmjs.com/cli/v7/commands/npm-audit#exit-code), la pipeline doit s'interrompre. [retire](https://github.com/Retirejs/retire.js) constitue un outil alternatif ayant la même utilité.

* Avec **pip (Python)** :

    + _Lockez_ votre arbre de dépendances, par exemple avec [pip-compile](https://github.com/jazzband/pip-tools)
    + Invoquez [safety](https://github.com/pyupio/safety-db) dans vos _pipelines_ pour détecter d'éventuelles vulnérabilités dans vos dépendances : en cas de code de retour non 0, la pipeline doit s'interrompre
    + Invoquez le linter de sécurité [bandit](https://github.com/PyCQA/bandit) dans vos _pipelines_ : en cas de code de retour non 0, la pipeline doit s'interrompre

* Avec **CocoaPods (iOS)** :

    + _Lockez_ les versions de vos pods, et versionnez votre `Podfile.lock` sous `git` ([documentation officielle](https://guides.cocoapods.org/using/using-cocoapods.html#what-is-podfilelock))
    + Pour évitez une _Dependency Confusion_, déclarez directement l’URL du repo git qui héberge le pod au niveau de l’import ([documentation officielle](https://guides.cocoapods.org/using/the-podfile.html#from-a-podspec-in-the-root-of-a-library-repo)). Exemple :
```ruby
pod 'Org/MyPod', :git => 'git@gitlab.example.com:org/my-pod.git', :tag => '1.2.3'
```


## Sécurité - Services intégrés

Pour finir, nous encourageons nos utilisateurs à intégrer dans leurs _pipelines_ les services suivants,
qui font également partie de notre usine logicielle :

* **Ne stockez aucun secret dans votre code source**

Ne versionnez dans votre repository `git` aucun _credential_ sensible : mot de passe, token, certificat privé...

Une solution recommandée pour stocker vos secrets et les employer de manière sécurisée dans vos _pipelines_ est [HashiCorp Vault](https://docs.gitlab.com/ee/ci/secrets/), dont une instance est mise à disposition.

![Logo Vault](images/2021/07/vault.png)

* **Configurez Renovate Bot sur vos repos**
Afin que les dépendances de leurs applications soient le plus à jour possible,
nous mettons à disposition de nos utilisateurs [Renovate Bot](https://renovatebot.com).

![Logo Renovate](images/2021/07/renovate.png)

* **Faites analyser votre code par Sonar**

Nous mettons à disposition de nos utilisateurs une instance [SonarQube](https://sonarqube.org),
qui intègre un ensemble de checks permettant de détecter des failles de sécurité.

L'image Docker [sonar-scanner-cli](https://hub.docker.com/r/sonarsource/sonar-scanner-cli) peut être employée pour soumettre à Sonar vos couvertures de tests depuis une _pipeline_ Gitlab.
Voici un exemple d'usage dan un repo Python, une fois les tests exécutés lors d'une étape précédente :
```yaml
image:
  name: sonarsource/sonar-scanner-cli:4.6
  entrypoint: [""]
script:
  - sonar-scanner -Dsonar.projectKey=... -Dsonar.projectName=... -Dsonar.projectVersion=...
                  -Dsonar.sources=. -Dsonar.host.url=$SONAR_HOST_URL
                  -Dsonar.python.coverage.reportPaths=cover/*coverage*.xml -Dsonar.coverage.exclusions=**/tests/**
```

![Logo SonarQube](images/2021/07/sonarqube.png)

Et vous, avez-vous des recommandations à partager autour de Gitlab CI ?

<!-- Com' :
* https://medium.com/@Lucas_C/bonnes-pratiques-gitlab-ci-9a380c83a74a
* https://linuxfr.org/users/lucas-c/liens/bonnes-pratiques-gitlab-ci
* https://dev.to/lucasc/bonnes-pratiques-gitlab-ci-5fb7
* https://www.journalduhacker.net/s/cafeya/bonnes_pratiques_gitlab_ci
* En cours de modération : https://news.humancoders.com
-->

<script>
['h2'].forEach(function (selector) {
    document.querySelectorAll(selector).forEach(function (title) {
        if (!title.classList.length) {
            title.id = title.textContent
                            .toLowerCase()
                            .replace(/[()?!:,'&@]/g, '')
                            .replace(/[à]/g, 'a')
                            .replace(/[ç]/g, 'c')
                            .replace(/[éêè]/g, 'e')
                            .replace(/[ï]/g, 'i')
                            .replace(/ /g, '-');
        }
    });
});
</script>
<style>
section > ul > li { margin-top: .5rem; }
article img { width: 16rem; }
</style>
