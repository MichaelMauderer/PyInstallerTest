from __future__ import unicode_literals, division, print_function

import argparse
import numpy

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true',
                        help='run test suite')
    args = parser.parse_args()
    print(numpy.__version__)
    print("HelloWorld")
