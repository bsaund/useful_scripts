#! /usr/bin/env python
from PIL import Image, ImageOps
import PIL
import numpy as np
from packaging import version
import argparse
from pathlib import Path


def compress_single_image(img_path, save_path, max_width=1000, max_height=1000):
    img = Image.open(img_path)
    if version.parse(PIL.__version__) >= version.Version("8.2"):
        img = ImageOps.exif_transpose(img)  # Uncomment this when new version of PIL (8.2?) appears on apt
    ratio = np.clip(np.min(np.array([max_width, max_height]) / img.size), 0, 1)
    new_size = (ratio * np.array(img.size)).astype(np.int)
    img = img.resize(new_size, Image.ANTIALIAS)
    img.save(save_path, optimize=True, quality=75)


def get_default_save_path(file: Path):
    if file.suffix.lower() != ".jpg":
        raise RuntimeError("Cannot yet handle non jpg images")
    save_path = Path(file.stem + "_compressed" + file.suffix)
    return save_path


def compress_single_image_from_command_line(command_line_file):
    file = Path(command_line_file)
    save_path = get_default_save_path(file)
    print(f'Compressing {file.as_posix()} to {save_path.as_posix()}')
    compress_single_image(file, save_path)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--file', help="The single image file to compress")

    args = p.parse_args()

    if args.file:
        compress_single_image_from_command_line(args.file)
    else:
        print("Not yet implemented yet, still a work in progress. Try the --file flag")
