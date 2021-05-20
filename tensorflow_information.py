#! /usr/bin/env python
try:
    import tensorflow as tf
except:
    print("Error: Tensorflow cannot be imported")


def display_useful_info():
    print(f"Tensorflow version: {tf.__version__}")
    gpus = tf.config.list_physical_devices('GPU')
    print(f"There are {len(gpus)} available GPUS: {gpus}")


if __name__ == "__main__":
    display_useful_info()
