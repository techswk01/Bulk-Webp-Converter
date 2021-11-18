[Webptools v0.0.7](https://pypi.org/project/webptools/)

webptools is a Webp image conversion package for the python.

Convert JPG,PNG.. images to webp image format

This library uses precompiled executables of WebP(v1.1.0) for more info
visit [WebP](https://developers.google.com/speed/webp)

For converting other image formats to webp, please read this
documentation  [cwebp Encoder](https://developers.google.com/speed/webp/docs/cwebp)

For converting webp image to other image format, please read this
documentation  [dwebp Encoder](https://developers.google.com/speed/webp/docs/dwebp)

For converting gif image to webp, please read this
documentation [gif2webp Converter](https://developers.google.com/speed/webp/docs/gif2webp)

For creating animated webp image using webp images, please read this
documentation [webpmux Muxer](https://developers.google.com/speed/webp/docs/webpmux)


# How to use

## Installation

```shell
$ pip install webptools
```

## Fix Permission Issue (if not using external executables)

```python

from webptools import grant_permission

# this will grant 755 permission to webp executables
grant_permission()

```

### Using External executables

```python

bin_path="libwebp_linux/bin/cwebp"

```

## The script will scan the (./images) folder for webp files. 
## You can change the image folder to your desired folder.

os.chdir("./images")  

```
