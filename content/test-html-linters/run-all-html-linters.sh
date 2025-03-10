#!/bin/bash
cd $( dirname "${BASH_SOURCE[0]}" )/../..
echo 'Executing vnu...'
time ./vnu-runtime-image/bin/vnu --Werror "$@"
echo
echo 'Executing tidy-html5...'
time tidy -errors "$@"
echo
echo 'Executing htmlhint...'
time htmlhint "$@"
echo
echo 'Executing html-validate...'
time html-validate "$@"
echo
echo 'Executing html-lint...'
time html-lint "$@"
