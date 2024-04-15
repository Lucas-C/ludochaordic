Title: Setting up linters in Gitlab CI for C++ and Groovy / Jenkins code
Date: 2024-04-15 16:30
Tags: lang:en, gitlab, gitlab-ci, pipeline, c++, groovy, gradle, jenkins, llvm, linter, static-code-analysis, continuous-integration, configuration, prog
---

A very short blog post to share some minimal code snippets on how to quickly and easily setup Gitlab CI pipelines to run static code analysis tools on C++ code and Jenkins pipelines (or any Groovy code).

![Logos Gitlab-CI, CodeNarc & clang-tidy](images/2024/04/gitlab-ci-codenarc-clang-tidy.png)

## Linting C++ code with clang-tidy

> [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) is a clang-based C++ linter tool that can identify and auto-fix some programming errors, like style violations, interface misuse, or bugs that can be deduced via static analysis.

```yaml
cpp-linter:
  # No need to specify the next line if your default Docker image is already an alpine:
  image: alpine:3.17
  script:
    - apk add clang-extra-tools
    - find . -name '*.cpp' -exec clang-tidy --fix {} \; | tee clang-tidy.log
    # Fail the job if errors were found:
    - ! grep "Found compiler error" clang-tidy.log
  rules:
    # Executing for every commit on the main branch where C++ files were modified:
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == "main"
      changes:
        - "*.cpp"
        - "**/*.cpp"
    # Executing for every commit in a non-draft merge request where C++ files were modified
    - if: $CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TITLE !~ /^Draft:.*$/
      changes:
        - "*.cpp"
        - "**/*.cpp"
```

You should also initiate a `.clang-tidy` configuration file like this:
```yaml
Checks: '*,-llvmlibc-*'
WarningsAsErrors: '*'
```

This default file is a strict starting point: it enables all rules, except the ones specific to LLVM, and treat all warnings as errors.
You can then add `-${ruleName}` to the `Checks` entry in this file to disable some checks.
Check the [clang-tidy documentation](https://clang.llvm.org/extra/clang-tidy/) for more details about rules and suppressing errors & warnings using code comments.


## Linting Groovy / Jenkins code with CodeNarc

> [CodeNarc](https://codenarc.org/) analyzes Groovy code for defects, bad practices, inconsistencies, style issues and more.

It can be used to perform static code analysis on [Jenkins pipelines](https://www.jenkins.io/doc/book/pipeline/).

Because [executing CodeNarc from the command-line](https://codenarc.org/codenarc-command-line.html#executing-codenarc-from-the-command-line) is not so simple, I find it easier to use [Gradle](https://gradle.org/) and its dedicated plugin to execute CodeNarc:

```yaml
groovy-linter:
  image: gradle:8.7
  script:
    - gradle check
  rules:
    # Executing for every commit on the main branch where C++ files were modified:
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == "main"
      changes:
        - "*.groovy"
        - "**/*.groovy"
    # Executing for every commit in a non-draft merge request where Groovy files were modified
    - if: $CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TITLE !~ /^Draft:.*$/
      changes:
        - "*.groovy"
        - "**/*.groovy"
```

You will also need a `build.gradle` file in the directory where the `gradle` command is executed:
```groovy
repositories {
    jcenter()
}

apply plugin: 'groovy'
apply plugin: 'codenarc'

sourceSets {
    main {
        groovy {
            // Specify the relative paths to the directories containing your .groovy files:
            srcDirs = ['.']
        }
    }
}
codenarc {
    configFile = file('./codenarc_rules.groovy')
    toolVersion = '3.4.0'
    reportFormat = 'text'
}
// The two following blocks allow to display the CodeNarc report in the console:
// ( this recipe comes from this SO answer: https://stackoverflow.com/a/36899862/636849 )
task codenarcConsoleReport {
    doLast {
        println file("${codenarc.reportsDir}/main.txt").text
    }
}
codenarcMain {
    finalizedBy codenarcConsoleReport
}
// You can optionnally disable the Groovy compilation step:
compileGroovy.enabled = false
```

And finally you can initialize a configuration file for the linter, named `codenarc_rules.groovy`:

<details>
  <summary>codenarc_rules.groovy</summary>
  <pre><code>ruleset {

    ruleset('rulesets/basic.xml')

    ruleset('rulesets/braces.xml')

    ruleset('rulesets/comments.xml')

    ruleset('rulesets/concurrency.xml')

    ruleset('rulesets/convention.xml') {
        // You may want to disable some rules, like this:
        CompileStatic(enabled:false)
        MethodParameterTypeRequired(enabled:false)
        MethodReturnTypeRequired(enabled:false)
        NoDef(enabled:false)
        PublicMethodsBeforeNonPublicMethods(enabled:false)
        VariableTypeRequired(enabled:false)
        TrailingComma(enabled:false)
    }

    ruleset('rulesets/design.xml')

    ruleset('rulesets/dry.xml') {
        // Allowing several benign cases of code duplication:
        DuplicateListLiteral(enabled:false)
        DuplicateMapLiteral(enabled:false)
        DuplicateNumberLiteral(enabled:false)
        DuplicateStringLiteral(enabled:false)
    }

    ruleset('rulesets/enhanced.xml')

    ruleset('rulesets/exceptions.xml')

    ruleset('rulesets/formatting.xml') {
        // Disabling rules that are too strict for my project:
        BlockEndsWithBlankLine(enabled:false)
        BlockStartsWithBlankLine(enabled:false)
        ConsecutiveBlankLines(enabled:false)
        Indentation(enabled:false)
        LineLength(enabled:false)
        SpaceAfterOpeningBrace(enabled:false)
        SpaceAroundMapEntryColon(enabled:false)
        SpaceBeforeClosingBrace(enabled:false)
    }

    ruleset('rulesets/generic.xml')

    // ruleset('rulesets/grails.xml')

    ruleset('rulesets/groovyism.xml')

    ruleset('rulesets/imports.xml')

    // ruleset('rulesets/jdbc.xml')
    // ruleset('rulesets/junit.xml')

    ruleset('rulesets/logging.xml') {
        // Allowing to print to stderr & stdout
        SystemErrPrint(enabled:false)
        SystemOutPrint(enabled:false)
    }

    ruleset('rulesets/naming.xml')

    ruleset('rulesets/security.xml')

    ruleset('rulesets/serialization.xml')

    ruleset('rulesets/size.xml')

    ruleset('rulesets/unnecessary.xml')

    ruleset('rulesets/unused.xml')

}</code></pre>
</details>

<br>
