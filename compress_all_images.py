#! /usr/bin/env python
from PIL import Image, ImageOps
import PIL
import numpy as np
from packaging import version


def compress_single_image(img_path, save_path, max_width=1000, max_height=1000):
    img = Image.open(img_path)
    if version.parse(PIL.__version__) >= version.Version("8.2"):
        img = ImageOps.exif_transpose(img) # Uncomment this when new version of PIL (8.2?) appears on apt
    ratio = np.clip(np.min(np.array([max_width, max_height]) / img.size), 0, 1)
    new_size = (ratio * np.array(img.size)).astype(np.int)
    img = img.resize(new_size, Image.ANTIALIAS)
    img.save(save_path, optimize=True, quality=75)


if __name__ == "__main__":
    print("Not yet implemented yet, still a work in progress")
