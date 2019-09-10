Title: Quick stats on a stream of values in the console
Date: 2014-09-09 15:09
Tags: lang:en, bash, unix, shell, statistics, awk, grep, stream, flow, variance, prog
Slug: quick-stats-on-a-stream-of-values-in-the-console
---
I often find myself `grep`-ing for information in system or application log files. And often, by combining pipes, I end up generating a flow of values that is sometimes difficult to interpret.

In this post I'll show you a quick-and-dirty but handy solution to get basic statistical quantities from a UNIX text stream of values.

There is the `bash` function using `awk` to put in your _.bashrc_:

```
stats () { # --no-header | awk '{print $3}'
    [ "$1" = "--no-header" ] || printf "%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n"\
        1-SUM 2-COUNT 3-MEAN 4-STD_DEV 5-MIN 6-TP01 7-TP10 8-MEDIAN 9-TP90 10-TP99 11-MAX
    sort -n | awk 'BEGIN{n=0;sum=0;mean=0;M2=0}\
        /^[^#]/{a[n++]=$1;sum+=$1;delta=$1-mean;mean+=delta/n;M2+=delta*($1-mean)}\
        function tp(ratio){i=n*ratio-1;if(i<0){return a[0];}else{return a[int(i)];}}
        END{unbiased_variance=M2/(n-1);
        std_dev=sqrt(unbiased_variance);
        if((n%2)==1){median=a[int(n/2)];}\
        else{median=(a[n/2]+a[n/2-1])/2;}\
        printf "%-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n",\
            sum,n,mean,std_dev,a[0],tp(.01),tp(.1),median,tp(.9),tp(.99),a[n-1]}'
}
```

Now, a very basic example:
```
# seq 1 10 | stats
1-SUM      2-COUNT    3-MEAN     4-STD_DEV  5-MIN      6-TP01     7-TP10     8-MEDIAN   9-TP90     10-TP99    11-MAX
55         10         5.5        3.02765    1          1          1          5.5        9          9          10
```

Then, what about the min & max hop length (in ms) when pinging _google.com_ ?

```
# traceroute google.com | sed '1d;/\*/d' | awk '{print $(NF-1)}'
1-SUM      2-COUNT    3-MEAN     4-STD_DEV  5-MIN      6-TP01     7-TP10     8-MEDIAN   9-TP90     10-TP99    11-MAX
377.292    9          41.9213    14.8838    3.101      3.101      3.101      46.556     48.472     48.472     52.235
```

Finally, let's look at the sizes (in bytes) of all the files in _/var/log_:

```
# stat -c '%s' /var/log/* | stats --no-header
8129626    119        68316.2    201958     0          0          218        5140       168528     704151     1693462
```

Of course, this little function is not meant to be used in production, where Python [pandas](http://pandas.pydata.org) library would do a far better job.

Inspiration taken from [a StackOverflow answer by Bruced Ediger](//unix.stackexchange.com/a/13779/48906) and [this Wikipedia online algorithm](//en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm) to compute variance.

**EDIT** [22/09/2014] : I found two very useful existing commands that do similar things: [`ministat`](https://github.com/thorduri/ministat) and [`tinystat`](//github.com/codahale/tinystat/blob/master/cmd/tinystat/main.go) written in Go.

**EDIT** [8/12/2014] : Another great one : `csvstat` (install it with `pip install csvkit`).
