Title: [EN] Follow a process progress to read a file
Date: 2014-10-08 05:10
Tags: bash, pv, proc, throughput, socat, watch, monitor, read, progress, file-descriptor
Slug: en-follow-a-progress-progress-to-read-a-file
---
Do you know the `pv` command ? It's really nifty.

There are a few use cases:

```bash
echo "You can simulate on-screen typing just like in the movies" | pv -qL 10

# Show the incoming TCP packets rate:
tcpdump tcp -w - | pv -btr >/dev/null

# Show the maximum throughput between two machines:
# (provided the correct iptables OUTPUT/INPUT rules allowing traffic through port 7070 are set)
socat - tcp-listen:7070 > /dev/null # on the receiving host side
pv -btr /dev/zero | socat - tcp:$host:7070 # on the sending server side

# Monitor progress of a command
gzip access.log | pv > access.log.gz

# Copy a file and watch its progress 
pv sourcefile > destfile
```

Actually the last two examples are the most common usages.

But what if you already started a command without `pv` but still want to watch the file processing progress ? Or if the file reading is done **inside** your command, without using Unix pipes ?

Well I've got a solution for you, heavily inspired by [Keegan McAllister article on Ksplace Oracle blog](//blogs.oracle.com/ksplice/entry/solving_problems_with_proc):

```bash
FIFTY_NON_SHADY_NOR_GREY_HASHES='##################################################'
progress_bar () {       # receive a serie of integers in {1..100} as input and update a unique progress bar line accordingly
    local percent
    while read percent; do
        printf "\r%-50s (%-3s%%)" ${FIFTY_NON_SHADY_NOR_GREY_HASHES:0:$((percent / 2))} $percent
    done
    echo
}

proc_read_fd_progress () {   # args: $pid [$fd]
    local pid=${1:?'Missing pid first argument'}
    ! [ -e /proc/$pid/ ] && echo "No process found with PID=$pid" >&2 && return 1
    local fd=$2
    if [ -z "${fd:-}" ]; then
        readlink /proc/$pid/fd/* | nl -v 0
        echo -n "Choose a file descriptor: "
        read fd
    fi
    local proc_fd=/proc/$pid/fd/$fd
    ! [ -e $proc_fd ] && echo "fd=$fd is not a valid file descriptor in /proc/$pid/fd/" >&2 && return 2
    local fd_size=$(wc -c $proc_fd | awk '{print $1}')
    echo "Progress reading '$(readlink $proc_fd)':"
    local percent_progress=0
    while [ -e $proc_fd ] && [ "$percent_progress" -ne 100 ] && ! read -n 1 -t 1 dummy; do
        local file_read_progress=$(grep ^pos /proc/$pid/fdinfo/$fd | awk '{print $2}')
        percent_progress=$((100 * $file_read_progress / $fd_size))
        echo $percent_progress
    done | progress_bar
}
```

Simply put the code above in your _.bashrc_, and you'll be able to test it immediately:

```
$ cat slow-reader.py
import sys, time
f = file(sys.argv[1], 'r')
while f.read(1024):
    time.sleep(0.01)
$ python slow-reader.py bigfile &
[1] 18589
$ proc_read_fd_progress 18589
     0  /dev/pts/25
     1  /dev/pts/25
     2  /dev/pts/25
     3  /home/lucas/bigfile
Choose a file descriptor: 3
Progress reading '/home/lucas/bigfile':
############################################       (88 %)
```

There are a few small differences with the original _phantom-progress.bash_:

- if none is provided, the command interactively asks which file descriptor to use from the list of files opened by the process
- it doesn't use the terminal-invasive `dialog` interface (nor `zenity`), but a bare simple one-line progress bar
- the command can be interrupted by any keystroke or _CTRL+C_