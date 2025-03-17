Title: Extracting images/photos from a diaporama video
Date: 2014-09-14 13:09
Lang: en
Tags: lang:en, ffmpeg, avconv, video, frames, extraction, duplicate, phash, grandma, prog
Slug: extracting-imagesphotos-from-a-diaporama-video
---
I was asked the other day by my grand-mother in law to try to recover her photos from a diaporama video she created years ago.

The diaporama was made of a succession of photos, occupying the whole screen for a moment and then transitioning with various effects to the next photo.

To avoid the manual approach of taking successive screenshots, I decided to build a simple pipeline out of some existing Linux tools to carry out the following plan:

* extract frames from the video as image files
* find the _static_ frames, i.e. consecutive identical ones, in opposition to frames that are part of transition effects
* select only one image for each batch of static frames

For the first phase I used the powerful `avconv` command (formerly known as `ffmpeg`), getting inspiration from [this forum post](http://ubuntuforums.org/showthread.php?t=2014630&p=12099770#post12099770):

```
sudo aptitude install avconv
mkdir ${video_file}_extracted
avconv -i $video_file.VOB -r 1 -an "${video_file}_extracted/videoframe%03d.png"
```

`-r 1` sets the [FPS](//en.wikipedia.org/wiki/Frame_rate) to 1 second and `-an` disables the audio recording. Because the output file pattern contains _"%0Nd"_, the **image2** file muxer is used by `avconv`.

At this point, I had more than 700 images. The next step was to find which ones were visually identical.

While there are many tools available to do the job, including the very interesting [perceptual hash](http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) algorithm in use at [TinEye](//www.tineye.com/) <sup><a href="#fn1" id="ref1"><small>1</small></a></sup>, my first pick was for a Perl-command available in the Ubuntu repositories, and it did the trick perfectly:

```
sudo aptitude install findimagedupes
mkdir triaged/
findimagedupes --threshold=99% --include 'VIEW() { middle_index=$(($# / 2)); middle_img=$(echo "$@" | sort | cut -d" " -f $middle_index); cp $middle_img triaged/; }' ${video_file}_extracted/
mv triaged ${video_file}_triaged/
rm -r ${video_file}_extracted/
```

The `--threshold` argument sets the similarity level required to group images in batches. In my case, with the default **90%** value, transition images were sometimes considered similar to static images; while with **100%**, some images that were visually identical were placed in separate batches.
The `VIEW` shell function defined in-line by `--include` is invoked for each batch of duplicate image file names. In this command it simply moves the select file of one batch in a separate directory. The selected image is the one in the middle of a serie of frames considered identical.

Et _voilà_, 60 static images properly extracted !



**EDIT [5/01/2014]** : to also extract the soundtrack of your .VOB file :
```
avconv -i /path/to/$video_file.VOB -vn -c:a libmp3lame -b:a 128k $video_file.mp3
```

**EDIT [15/02/2015]** : for a generic approach to extracting frames, check this very detailed post on [MoviePy](http://zulko.github.io/blog/2015/02/01/extracting-perfectly-looping-gifs-from-videos-with-python-and-moviepy/) Python library.

<br><hr><br>

<sup id="fn1">1. Among other examples of _pHash_ usage: [ImageHash](//pypi.python.org/pypi/ImageHash) a generic Python library, and an [image-deduplication-tool](//github.com/mk-fg/image-deduplication-tool). <a href="#ref1">↩</a></sup>
