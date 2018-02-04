grep -h wwcb content/*.md | sed -e 's~.*src="\([^ ]*\)".*~content/\1~' -e 's~.*\](\([^)]*\)).*~content/\1~' >rsync.include
../pelican-mg/gen_imgs_from_mds.py --list content/*.md | grep -v wwcb >>rsync.include
echo content/images/readings/* >>rsync.include
rsync --files-from=rsync.include -rv ct-lucas:ludochaordic/ .

