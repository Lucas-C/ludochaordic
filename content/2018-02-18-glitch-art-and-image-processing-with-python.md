Title: Glitch art and image processing with Python
Date: 2018-02-18 23:00
Tags: lang:en, glitch-art, reddit, image-processing, python, music, net-art, datamoshing, art, lazy-loading, prog
Slug: glitch-art-and-image-processing-with-python
Image: images/2018/02/colorstolen_japanified_TDZSJMs.jpg
---

This week I discovered the fantastic [glitch art](https://www.reddit.com/r/glitch_art) Reddit community
(for a little more context on glitch art, [wikipedia has a page](https://en.wikipedia.org/wiki/Glitch_art)).
These are the pieces I love the most (click on them to find the source):

<!-- The a > div > noscript seems not valid in terms of HTML syntax -->
<a href="https://www.reddit.com/r/glitch_art/comments/7x3ps0/dream_girl_gaze/">
<div class="lazyload" data-noscript=""><noscript><img alt="dream_girl_gaze art by misteach" src="images/2018/02/pd1gx9xucuf01.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/75ok6f/walk_it_off/">
<div class="lazyload" data-noscript=""><noscript><img alt="Walk it off by skybrian" src="images/2018/02/zqvSQdO.png"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/5wbei8/pxl_rain/">
<div class="lazyload" data-noscript=""><noscript><img alt="pxl_rain by GutturalEcho" src="images/2018/02/ljc76jy3s8iy.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/pixelsorting/comments/757ung/a_bit_of_rain/">
<div class="lazyload" data-noscript=""><noscript><img alt="A bit of rain by cirodoggy" src="images/2018/02/31t7i2m9rrqz.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/7glph4/the_heavens_opened_up_when_the_rain_came/">
<div class="lazyload" data-noscript=""><noscript><img alt="The heavens opened up When the rain came by txchick1983" src="images/2018/02/fBb1s47.png"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/8n8xnu/sakura/">
<div class="lazyload" data-noscript=""><noscript><img alt="Sakura by piromantic" src="images/2018/02/sakura.png"></noscript></div>
</a>

<a href="https://www.reddit.com/r/pixelsorting/comments/61iwka/liquid_metal/">
<div class="lazyload" data-noscript=""><noscript><img alt="Liquid metal by Tw1gz666" src="images/2018/02/tap4xb93enny.jpg"></noscript></div>
</a>
This one above reminds me of [The Great Wave off Kanagawa](https://en.wikipedia.org/wiki/The_Great_Wave_off_Kanagawa).
Like many other pieces, it uses a "glitching" technique called Pixed Sorting.

<a href="https://www.reddit.com/r/glitch_art/comments/6nsxna/city_lights/">
<div class="lazyload" data-noscript=""><noscript><img alt="City Lights by Sarxasm" src="images/2018/02/DKgMD0A.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/pixelsorting/comments/7b3u4x/have_you_ever_retired_a_human_by_mistake/">
<div class="lazyload" data-noscript=""><noscript><img alt="Have you ever retired a human by mistake? by pixelated_spliffs" src="images/2018/02/nxmkk00scbwz.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/79bm2k/lost_city/">
<div class="lazyload" data-noscript=""><noscript><img alt="Lost City by Kek_Snek" src="images/2018/02/ep2fjwlh3muz.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/22dk1u/wakegif/">
<div class="lazyload" data-noscript=""><noscript><img alt="wake.gif by HopelessPerson" src="images/2018/02/SFVf5ov.gif"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/6ylvyw/you_cant_handle_the_glitch_by_arsikere/">
<div class="lazyload" data-noscript=""><noscript><img alt="You can't handle the Glitch by @Arsikere" src="images/2018/02/AWlGFnu.gif"></noscript></div>
</a>

This other glitch video by MarshmellowNinja is very funny, but better viewed online: <https://www.reddit.com/r/glitch_art/comments/7xhbrf/woah/>

<a href="https://www.reddit.com/r/glitch_art/comments/26w188/a_landscape_piece/">
<div class="lazyload" data-noscript=""><noscript><img alt="A landscape piece. by vvdr12" src="images/2018/02/vvdr12_14116705239_cd7ae031e4_k.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/1kztnf/japanization_python_pixel_editing_bug/">
<div class="lazyload" data-noscript=""><noscript><img alt="Japanization: Python pixel editing bug by vvdr12" src="images/2018/02/vvdr12_9655801399_c763157694_o.png"></noscript></div>
</a>

<a href="https://www.flickr.com/photos/vvdr12/10343539123/">
<div class="lazyload" data-noscript=""><noscript><img alt="elephant hill by vvdr12" src="images/2018/02/vvdr12_10343539123_128a0c8375_k.jpg"></noscript></div>
</a>

Those 4 last ones are from Reddit user [vvdr12](https://www.reddit.com/user/vvdr12), whose [flickr gallery](https://www.flickr.com/photos/vvdr12/) also includes great intentionnaly made pieces. He [kindly explained](https://www.reddit.com/r/glitch_art/comments/1kztnf/japanization_python_pixel_editing_bug/) [how he made this "japanify" effect in Python](https://www.reddit.com/r/glitch_art/comments/1p5mno/elephant_hill/), and specified the [source image](http://imgur.com/TDZSJMs).

He did not provide the code for the palette substitution, so I re-rewrote it: [japanify.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/img_processing/japanify.py) + [steal_colors_with_same_brightness.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/img_processing/steal_colors_with_same_brightness.py)
```bash
./japanify.py TDZSJMs.jpg
./steal_colors_with_same_brightness.py --palette-img edJl3YU.jpg japanified_TDZSJMs.jpg
```

(I'd love to also replicate [this animated Joy Division effect by vvdr12](https://imgur.com/Jcs4BMw), but he only provided some code to produce a static image - maybe a GIF could be created using [Zhao Liang GIFWriter](https://github.com/neozhaoliang/pywonderland/blob/master/src/wilson/encoder.py)...)

The Glasgow band [Kill the Waves](https://soundcloud.com/killthewaves) even used his idea for their album cover:

![Kill The Waves band album cover](http://i.imgur.com/JrPsI1y.jpg)

It was nice to stumble on this band, I especially like their [Anymore](https://soundcloud.com/tonguesmusic/anymore) & [Vow](https://soundcloud.com/killthewaves/vow) songs.

What do you think of those glitches ? ?? Are there other ones you known and like ? ??

**EDIT [2018/03/05]** : I learned thanks to <http://rhizome.org> about the name of one of those technics, _datamoshing_,
of which this video is an example : <https://www.youtube.com/watch?v=TxFeesWL5OI>.

There is also this tumblr collecting glitch GIFs: <http://glitchgifs.tumblr.com>.

**EDIT [2018/11/16]** : another outstanding one

<a href="https://www.reddit.com/r/glitch_art/comments/5qlthr/pixel_sort_rotation_gif_oc/">
<div class="lazyload" data-noscript=""><noscript><img alt="Pixel sort Rotation by HI_IM_DR_PHIL" src="images/2018/02/ls5etz2fodcy.gif"></noscript></div>
</a>

**EDIT [2020/07/17]** : a couple of new ones

<a href="https://www.reddit.com/r/glitch_art/comments/hpvuxe/7122020/">
<div class="lazyload" data-noscript=""><noscript><img alt="7/12/2020 by YTChyme"
src="images/2018/02/998zibjfzfa51.jpg"></noscript></div>
</a>

<a href="https://www.reddit.com/r/glitch_art/comments/hfk749/im_glitching_out/">
<div class="lazyload" data-noscript=""><noscript><img alt="Im glitching out by Cruel_Coppinger"
src="images/2018/02/7wr3m65mg1751.jpg"></noscript></div>
</a>

Check also the [sǝʌᴉʇɐuɹǝʇlɐ](https://imgur.com/a/ruqeUJV).


<style>
article img {
    max-height: 80vh;
}
.lazyload, .lazyloaded {
    padding: .2rem;
    display: flex;
    justify-content: center;
    align-items: center;
}
.lazyloading {
    opacity: 0;
}
.lazyloaded {
    opacity: 1;
    transition: opacity 300ms;
}
</style>
<script>
function setTitles() {
  document.querySelectorAll('article img').forEach(img => img.title = img.alt)
  setTimeout(setTitles, 2000);
}
setTitles();
</script>
