#!/bin/bash

# line=$(catkin run_tests --no-deps --this -j1)

# if [ $? ]
# then
#     echo "$line"
#     echo ""
#     echo "BUILD FAILED"
#     exit 1
# fi

# echo "$line" | grep "\[" | grep -v "^\[build" | grep -v "^make" |grep -v "^\[ \?[0-9]"
catkin run_tests --no-deps --this -j1 | grep -v "^make" | grep -v "\/home" | grep -v "^\[build" |grep -v "^\[ \?[0-9]" | grep -v "\/usr" | grep -v "\-\-"

catkin_test_results ~/catkin_ws/build/

if [ $? == 0 ]
then
    echo ""
    echo "ALL TESTS PASSED"
else
    echo ""
    echo "TESTS FAILED"    
fi
