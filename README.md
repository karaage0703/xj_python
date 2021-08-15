# XJ System
xj system

## Dependency

- Pyxel
- Pygame

## Setup

Execute following command for installing xj_python library:

```sh
$ pip3 install xj_python
```

Recommended input device is X-TOUCH MINI(MIDI).

You can operate XJ system with normal keyboard.


## Usage

Test commands:

```sh
$ git clone https://github.com/karaage0703/xj_python
$ cd xj_python/examples
$ python3 color.py
```

If you can see black window, program is OK.

Press 'E' or 'R' of keyboard button. You can see changing color of window.

Custom and hack and enjoy XJ system!

## Update PyPI package

1. Change version of `setup.py`

2. Build pip package:

```sh
$ ./build_pip_package.sh
```

3. Upload pip package to PyPI

```sh
$ twine upload --repository pypi dist/xj_python-*.tar.gz
```

## License
This software is released under the MIT License, see LICENSE.

## Authors
karaage0703

## References

- https://tkitao.hatenablog.com/entry/2019/09/03/010514
- [日経ソフトウエア 2021年7月号](https://amzn.to/3zvlfzI)
