#!/bin/bash
set -o errexit -o nounset -o pipefail
export LANG=C
for md_filepath in ${@:-content/*.md}; do
    date_prefix=$(echo ${md_filepath#*/} | cut -d- -f1-3)
    if ! grep -m 1 -q -F "Date: $date_prefix" $md_filepath; then
        echo Erroneous date in $md_filepath
        # For drafts, just display a warning, do not error-out:
        grep -qF "Status: draft" $md_filepath || exit 1
    fi
done
