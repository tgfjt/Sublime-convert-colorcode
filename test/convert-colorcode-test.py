# -*- coding: utf-8 -*-

import doctest
import re


def convert(text, upper=True):
    """
    >>> convert('background: #FFF; color: #00AACC', False)
    'background: #fff; color: #00aacc'
    >>> convert('background: #fff; color: #00aacc')
    'background: #FFF; color: #00AACC'
    """
    target = re.findall('\#[0-9a-fA-F]{3,6}', text)
    replace_text = text

    for i in range(len(target)):
        if upper is True:
            replace_text = replace_text.replace(target[i], target[i].upper())
        else:
            replace_text = replace_text.replace(target[i], target[i].lower())

    return replace_text


if __name__ == '__main__':
    doctest.testmod()
    if doctest.testmod().failed:
        import sys
        sys.exit(doctest.testmod()[0])
