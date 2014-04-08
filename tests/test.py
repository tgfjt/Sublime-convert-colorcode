# -*- coding: utf-8 -*-

import doctest
import sys
import os

sys.path = [os.path.abspath("../project")] + sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

try:
    from .convert import convert
except:
    from convert import convert


def _test(text, upper=True):
    """
    >>> _test('background: #FFF; color: #00AACC', False)
    'background: #fff; color: #00aacc'
    >>> _test('background: #fff; color: #00aacc')
    'background: #FFF; color: #00AACC'
    """
    return convert(text, upper)

if __name__ == '__main__':
    doctest.testmod()
    if doctest.testmod().failed:
        sys.exit(doctest.testmod()[0])
