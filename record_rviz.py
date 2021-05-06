#! /usr/bin/env python
from window_recorder.recorder import WindowRecorder
import time
print("hello")


if __name__ == "__main__":
    with WindowRecorder(["RViz*"],
                        frame_rate=30.0, name_suffix="rviz_demo",
                        save_dir="/home/bradsaund/tmp"):
        while True:
            time.sleep(1)


