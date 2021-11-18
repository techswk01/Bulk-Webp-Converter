Main package used: 
[Webptools v0.0.7](https://pypi.org/project/webptools/)
webptools is a Webp image conversion package for the python.
For converting webp image to other image format, please read this
documentation  [dwebp Encoder](https://developers.google.com/speed/webp/docs/dwebp)

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
Credits to [Daweo](https://stackoverflow.com/users/10785975/daweo) for contribution on bug fixing
