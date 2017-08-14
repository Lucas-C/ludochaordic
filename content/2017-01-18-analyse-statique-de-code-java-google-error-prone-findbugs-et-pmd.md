Title: [FR] Analyse statique de code Java : Google Error Prone, Findbugs et PMD
Date: 2017-01-18 13:01
Tags: lang:fr, findbugs, google, error-prone, java, maven, pmd, static-code-analysis, prog
Slug: analyse-statique-de-code-java-google-error-prone-findbugs-et-pmd
---
![](/lucas/blog/content/images/2017/01/img_3069.jpg)

Ce court article détaille comment mettre en place simplement 3 analyseurs de code statique avec Maven.


## Contexte

Au sein de mon équipe à [Voyages-Sncf](http://jobs.voyages-sncf.com), le nombre de composants Java est en train d'augmenter.

Nous avons déjà toute une batterie de tests pour valider notre code, ainsi qu'un Sonar en place.

Néanmoins, aucune <strong><em>analyse<strong> </strong>statique du code à la compilation</em></strong>, avant de commiter.

La mise en place de tels outils de validation a permis de<em> <strong>détecter un bug majeur</strong></em> : Findbugs a repéré qu'un accesseur de DAO retournait le mauvais champ.

Pour l'occasion, j'ai fais un petit tour d'horizon des analyseurs de code Java utilisés aujourd'hui, et j'ai en testé 3.


## Google Error Prone

<a href="http://errorprone.info/">Error Prone</a> est un petit nouveau (2012) parmi les analyseurs de code statique. Il est implémenté comme un "hook" du compileur <code>javac</code>, et est très facile à mettre en place avec Maven :
```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.3</version>
    <configuration>
        <compilerId>javac-with-errorprone</compilerId>
        <forceJavacCompilerUse>true</forceJavacCompilerUse>
        <source>8</source>
        <target>8</target>
    </configuration>
    <dependencies>
        <dependency>
            <groupId>org.codehaus.plexus</groupId>
            <artifactId>plexus-compiler-javac-errorprone</artifactId>
            <version>2.8.1</version>
        </dependency>
        <!-- override plexus-compiler-javac-errorprone's dependency on Error Prone with the latest version -->
        <dependency>
            <groupId>com.google.errorprone</groupId>
            <artifactId>error_prone_core</artifactId>
            <version>2.0.15</version>
        </dependency>
    </dependencies>
</plugin>
```
&nbsp;
En terme de config, on peut noter les tags <code>source</code> et <code>target</code> indiquant la version de Java utilisée.


## Findbugs

Bien que le projet soit <a href="https://garygregory.wordpress.com/2016/11/07/of-the-demise-of-findbugs-and-monty-python/">actuellement au point mort</a>, Findbugs reste un outil très utilisé et très puissant. Tout un ensemble d'analyseurs supplémentaires peut même lui être ajouté via le plugin <a href="https://github.com/mebigfatguy/fb-contrib">fb-contrib</a>.

Voici comment le mettre en place avec Maven :
```
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>findbugs-maven-plugin</artifactId>
    <version>3.0.4</version>
    <configuration>
        <failOnError>true</failOnError>
        <threshold>Default</threshold>
        <effort>Max</effort>
        <omitVisitors>ExceptionSoftening,FieldCouldBeLocal,OverlyConcreteParameter,PossiblyRedundantMethodCalls,SuspiciousJDKVersionUse,UnnecessaryStoreBeforeReturn</omitVisitors>
        <plugins>
            <plugin>
                <groupId>com.mebigfatguy.fb-contrib</groupId>
                <artifactId>fb-contrib</artifactId>
                <version>6.8.1</version>
            </plugin>
        </plugins>
    </configuration>
    <executions>
        <execution>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
   </executions>
</plugin>
```
Ici, l'exécution du plugin se fera en phase Maven <code>compile</code>. Si vous ne souhaitez pas utiliser <code>fb-contrib</code>, il suffit de supprimer la section <code>plugins</code>.

Le degré de sévérité des analyseurs, peut être contrôlé via les tags <code>threshold</code> et <code>effort</code>. Pour supprimer des erreurs, on peut éliminer entièrement un analyseur en l'incluant dans le champ <code>omitVisitors</code>, ou bien en utilisant l'annotation [`@SuppressFBWarning`](http://findbugs.sourceforge.net/api/edu/umd/cs/findbugs/annotations/SuppressFBWarnings.html).

Enfin, cet analyseur peut également produire des rapports HTML (même si ça peut être un peu <a href="http://stackoverflow.com/a/10365954/636849">alambiqué</a> à mettre en place), mais si on veut conserver le comportement failOnError il faut alors configurer <a href="http://stackoverflow.com/a/38655823/636849">deux phases d'exécution</a>.


## PMD

<a href="https://pmd.github.io/">PMD</a> est un outil très complet, capable d'analyser de nombreux languages.
Encore une fois, il est assez simple à mettre en place avec Maven:
```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-pmd-plugin</artifactId>
    <version>3.7</version>
    <configuration>
        <failOnViolation>true</failOnViolation>
        <failurePriority>5</failurePriority>
        <printFailingErrors>true</printFailingErrors>
        <linkXRef>false</linkXRef>
    </configuration>
    <executions>
        <execution>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```
Encore une fois, l'exécution du plugin se fera en phase Maven <code>compile</code>.

<code>printFailingErrors</code> permet d'avoir une liste d'erreur en terminal.

Pour <a href="http://pmd.sourceforge.net/pmd-4.3.0/suppressing.html">supprimer des erreurs</a>, on peut utiliser une annotation ou bien un simple commentaire "<code>NOPMD</code>" en fin de ligne de code.


## Infer

Facebook a développé un outil très prometteur nommé [infer](http://fbinfer.com/), mais malheureusement il ne tourne pas sous Windows.

Si malgré tout vous souhaitez le tester, il est possible de [le lancer via Docker](https://www.lolware.net/2016/02/12/argon2-code-review.html).

![](/lucas/blog/content/images/2017/01/oh-no-the-robots.jpg)
