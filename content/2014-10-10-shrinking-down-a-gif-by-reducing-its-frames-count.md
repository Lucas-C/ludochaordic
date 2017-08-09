Title: Shrink down a GIF by reducing its frames count
Date: 2014-10-10 03:10
Tags: lang:en, bash, image, frames, gif, imagemagick, convert, fps, size, delay
Slug: shrinking-down-a-gif-by-reducing-its-frames-count
---
To illustrate my [previous post](https://chezsoi.org/lucas/blog/2014/10/10/en-setting-up-etherpad-in-a-server-subdirectory-aka-apache-config-hell/) and keep images at a reasonable size, I had to shrink down the top GIF from [14Mb](https://lh3.googleusercontent.com/-W4wSdhJ2O3A/UfgjKpNKBCI/AAAAAAAAAac/UGbf_GaXjA4/w400-h225-no/Cloudberry+Kingdom+difficulty.gif) to [3.2Mb](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x3.gif).

Usually, online GIF converters will provide the ability to lower down the image dimensions. Another solution to reduce its size is to simply skip some frames.

To do so, I used [ImageMagick](http://imagemagick.org/) wrapped in the following script:
```bash
gif_framecount_reducer () { # args: $gif_path $frames_reduction_factor
    local orig_gif="${1?'Missing GIF filename parameter'}"
    local reduction_factor=${2?'Missing reduction factor parameter'}
    # Extracting the delays between each frames
    local orig_delay=$(gifsicle -I "$orig_gif" | sed -ne 's/.*delay \([0-9.]\+\)s/\1/p' | uniq)
    # Ensuring this delay is constant
    [ $(echo "$orig_delay" | wc -l) -ne 1 ] \
        && echo "Input GIF doesn't have a fixed framerate" >&2 \
        && return 1
    # Computing the current and new FPS
    local new_fps=$(echo "(1/$orig_delay)/$reduction_factor" | bc)
    # Exploding the animation into individual images in /var/tmp
    local tmp_frames_prefix="/var/tmp/${orig_gif%.*}_"
    convert "$orig_gif" -coalesce +adjoin "$tmp_frames_prefix%05d.gif"
    local frames_count=$(ls "$tmp_frames_prefix"*.gif | wc -l)
    # Creating a symlink for one frame every $reduction_factor
    local sel_frames_prefix="/var/tmp/sel_${orig_gif%.*}_"
    for i in $(seq 0 $reduction_factor $((frames_count-1))); do
        local suffix=$(printf "%05d.gif" $i)
        ln -s "$tmp_frames_prefix$suffix" "$sel_frames_prefix$suffix"
    done
    # Assembling the new animated GIF from the selected frames
    convert -delay $new_fps "$sel_frames_prefix"*.gif "${orig_gif%.*}_reduced_x${reduction_factor}.gif"
    # Cleaning up
    rm "$tmp_frames_prefix"*.gif "$sel_frames_prefix"*.gif
}
```

```
$ for i in {2..5}; do gif_framecount_reducer Cloudberry-Kingdom-difficulty.gif $i; done
$ ls -sh *.gif | sort -r
8.7M Cloudberry-Kingdom-difficulty.gif
4.7M Cloudberry-Kingdom-difficulty_reduced_x2.gif
3.2M Cloudberry-Kingdom-difficulty_reduced_x3.gif
2.4M Cloudberry-Kingdom-difficulty_reduced_x4.gif
1.9M Cloudberry-Kingdom-difficulty_reduced_x5.gif
```

There are the results:

- [Cloudberry-Kingdom-difficulty.gif](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty.gif)
- [Cloudberry-Kingdom-difficulty\_reduced\_x2.gif](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x2.gif)
- [Cloudberry-Kingdom-difficulty\_reduced\_x3.gif](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x3.gif)
- [Cloudberry-Kingdom-difficulty\_reduced\_x4.gif](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x4.gif)
- [Cloudberry-Kingdom-difficulty\_reduced\_x5.gif](/lucas/blog/content/images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x5.gif)

This function also rely on the `gifsicle` command, that is dedicated to creating and editing GIFs. It can be more useful and reliable than ImageMagick `identify` to extract information. E.g. you can extract the frames count this way:

    gifsicle $gif -I | sed -ne 's/.* \([0-9]\+\) images/\1/p'