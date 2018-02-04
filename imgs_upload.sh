# USAGE: ./imgs_upload.sh content/images/2017/08
scp -r $1/ ct-lucas:ludochaordic/$(dirname $1)