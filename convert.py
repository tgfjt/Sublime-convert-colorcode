# -*- coding: utf8 -*-

import re


def convert(text, upper=True):
    target = re.findall('\#[0-9a-fA-F]{3,6}', text)
    replace_text = text

    for i in range(len(target)):
        if upper is True:
            replace_text = replace_text.replace(target[i], target[i].upper())
        else:
            replace_text = replace_text.replace(target[i], target[i].lower())

    return replace_text
