#!/bin/bash
set -o errexit -o nounset -o pipefail
for f in ${@:-content/*.md}; do
    date_prefix=$(echo ${f#*/} | cut -d- -f1-3)
    LANG=C grep -m 1 -q -F "Date: $date_prefix" $f || { echo Erroneous date in $f; exit 1; }
done
