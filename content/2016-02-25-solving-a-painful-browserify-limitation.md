Title: Solving a painful browserify limitation : portable source files selection with a wildcard pattern
Date: 2016-02-25 15:02
Tags: lang:en, node-js, browserify, bundle, windows, npm, glob, portability, prog
Slug: solving-a-painful-browserify-limitation
---
In any UNIX shell, the following will always work out of the box:
```
browserify src/main/lib/js/*.js > out-bundle.js
```

But of course, **not under Windows**.

And `browserify` does not accept directory names as primary parameter, nor wildcard globbing patterns. There is a pending [issue & pull request](https://github.com/substack/node-browserify/issues/1170) aiming to solve this, but it doesn't seem it's going to get merged soon. So lets solve this.

Put the following code in a file named `browserify_glob.js` :
```
var browserify = require('browserify'),
    glob = require('glob');

var bundler = browserify();

console.error('Called with: ' + process.argv.slice(2));
var glob_pattern = process.argv[2];
if (glob_pattern.charAt(0) === "'") { // Needed for Windows compatibility
    glob_pattern = glob_pattern.slice(1, -1);
}

glob(glob_pattern, function (error, srcFiles) {
    if (error) { throw error; }
    srcFiles.forEach(function (srcFile) {
        console.error('- Adding', srcFile);
        bundler.add(srcFile);
    });

    bundler.bundle().pipe(process.stdout);
});
```

And in your `package.json` :
```
{
  "devDependencies": {
    "browserify": "latest",
    "glob": "latest"
  },
  "scripts": {
    "build:js": "node browserify_glob.js 'src/main/lib/js/**/*.js' > out-bundle.js"
  }
}
```

And now you can `npm install && npm run build:js` and it will work under Windows !

In fact, a `**/*.js` glob pattern is even more powerful that a typical UNIX-style wildcard, as it will list files recursively.

**EDIT [2016/05/17]** : I realized this trick is uterly dumb and useless : `browserify` is able to  [find dependancies using static analysis from a single JS file entry point](https://github.com/substack/browserify-handbook#how-browserify-works).
