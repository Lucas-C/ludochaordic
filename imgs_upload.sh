# USAGE: ./imgs_upload.sh content/images/2017/08
[ "$#" -gt 1 ] && echo 'Too many args!' >&2 && exit 1
scp -r "$1/" chezsoi:ludochaordic/$(dirname "$1")