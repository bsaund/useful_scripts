#!/bin/bash

if [ $# -ne 1 ]
  then
    echo "Usage: voxelize_all.sh resolution"
    exit 1
fi

RESOLUTION="$1"


FILES="./*.stl"
for f in $FILES
do
    printf "\n\n\n===================================\n"
    printf "Voxelizing $f\n"
    printf "===================================\n\n\n"
    voxelize.sh $f $RESOLUTION
done

