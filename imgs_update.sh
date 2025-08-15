grep -h wwcb content/*.md | sed -e 's~.*src="\([^ ]*\)".*~content/\1~' -e 's~.*\](\([^)]*\)).*~content/\1~' >rsync.include
../pelican-mg/gen_imgs_from_mds.py --list content/*.md | grep -v wwcb >>rsync.include
../pelican-mg/gen_imgs_from_mds.py --list content/pages/*.md | grep -v wwcb >>rsync.include
python -c 'from pelicanconf import READINGS; [print("content/"+img["img_url"]) for img in READINGS]' >>rsync.include
rsync --files-from=rsync.include -rv chezsoi:ludochaordic/ .

