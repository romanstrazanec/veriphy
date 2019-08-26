# Veriphy

Python script to verify file integrity.

## Usage

python -m veriphy [-h] [-i INPUT | -s SIGN] [-a ALGORITHM] file

positional arguments:

- file: file to verify

optional arguments:

- -h, --help: show this help message and exit
- -i INPUT, --input INPUT: file containing signature
- -s SIGN, --sign SIGN: direct signature
- -a ALGORITHM: hash function to use

If one of `-s` or `-i` (`--sign` or `--input`) options is not given, script asks for a signature.

If no algorithm is given (with option `-a`)

### Available algorithms

List of python's `hashlib.algorithms_guaranteed`:

- md5
- sha384
- sha1
- shake_256
- shake_128
- sha3_384
- sha3_256
- blake2b
- sha3_512
- blake2s
- sha3_224
- sha256
- sha224
- sha512

## Installation

Run: `pip install veriphy`
