Title: Simply adding HTML meta tags in Wordpress
Date: 2025-08-10 10:00
Lang: en
Tags: lang:en, wordpress, plugin, html, metadata, source-code, semantic-web, seo, prog
Image: images/2025/08/HTML-Meta-Tags.png
---

Just a quick blog post about Wordpress configuration, mostly as a reminder to myself.

If you manage a public website, you probably want it to include some [HTML metadata](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta):
it is important for referencing your website in search engines,
as well as to provide a nice "preview miniature" on social on social networks, using [Open Graph meta tags](https://www.opengraph.xyz).

<figure>
  <img src="images/2025/08/HTML-Meta-Tags.png" alt="HTML meta tags">
  <figcaption>HTML meta tags – Author: Seobility – License: <a title="Creative Commons License BY-SA 4.0" href="/en/wiki/creative-commons-license-by-sa-4-0">CC BY-SA 4.0</a></figcaption>
</figure>

I was wondering how to add such metadata in a Wordpress website, in the easiest way.
I tested various plugins, like [OG — Better Share on Social Media](https://fr.wordpress.org/plugins/og/) or [Head Meta Data](https://wordpress.org/plugins/head-meta-data/).
They are well made and have interesting features, like the ability to have custom tags depending on the current Wordpress page.

However I discovered that the simplest way to setup HTML `<meta>` tags, as a web developper, without having to install any plugin (that will require updates), is to just use [the `wp_head` hook](https://developer.wordpress.org/reference/hooks/wp_head/):
```php
function head_meta_html() {
    echo <<<'EOD'
<meta name="author" content="<author>">
<meta name="description" content="<description>">
<meta property="og:description" content="<description>">
<meta property="og:image" content="<full URL to a cover image for your website>">
<meta property="og:type" content="website">
<meta property="og:locale" content="<language code>">
<meta property="og:site_name" content="<website name>">
<meta property="og:title" content="<website name>">
<meta property="og:url" content="<website base URL>">
<meta name="rating" content="General">
<meta name="keywords" content="<keywords>">
<meta content="on" name="twitter:dnt">
<meta content="FR-49" name="geo.region">
<meta content="<city name or location name>" name="geo.placename">
<meta content="<coordinates; semicolon-separated>" name="geo.position">
<meta content="<coordinates, comma-separated>" name="ICBM">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  ...
}
</script>
EOD;
}
add_action('wp_head', 'head_meta_html');
```

You can for example put this in your Wordpress template `functions.php` file.
You may also want to [remove the default `<meta name="generator" content="WordPress X.Y.Z" />` tag](https://stackoverflow.com/questions/16335347/wordpress-how-do-i-remove-meta-generator-tags/17484970#17484970), for security reasons.

Note that Wordpress, the theme you are using and the plugins you have installed, may already setup some `<meta>` tags,
like the `charset` or the `viewport`.

If you are interested in the relevance of HTML meta tags nowadays,
I heavily recommend this article: [You probably don’t need http-equiv meta tags @ rviscomi.dev](https://rviscomi.dev/2023/07/you-probably-dont-need-http-equiv-meta-tags/).
