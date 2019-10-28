#!/bin/bash
FILES=*
for f in $FILES
do
    # echo "$f"
    # size=${#f}
    # if [ 11 > 10 ]
    # then
    # echo "$size"
    # echo "${f:0:10}"
        if [ ${f:0:10} == "compressed" ]
        then
            echo "Skipping $f, already compressed"
            continue
        fi
    # fi
        
    if [ ${f: -4} != ".mp4" ]
    then
        echo "Skipping $f, not a mp4"
        continue
    fi
    echo "Processing $f"
    ffmpeg -i "$f" -b 1000000 -strict -2 "compressed_$f"

done
