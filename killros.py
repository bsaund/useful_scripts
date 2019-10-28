#!/usr/bin/env python

"""
Kills all ROS processes
"""

import subprocess, signal
import os
import IPython

p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():

    if 'ros' in line:
        if 'killros' in line:
            continue
        pid = int(line.split()[1])
        print("")
        print("killing process: " + line)
        
        os.kill(pid, signal.SIGKILL)


