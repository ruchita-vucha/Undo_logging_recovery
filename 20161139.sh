#!/bin/sh
if [ "$#" -ne 1 ]; then
    python2 20161139_1.py $1 $2 > 20161139_1.txt
else
    python2 20161139_2.py $1 > 20161139_2.txt
fi

