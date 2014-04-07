# -*- coding: utf8 -*-

import sublime
import sublime_plugin
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


class ConvertLowerColorcodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, show_regions=True, show_panel=True):
        view = self.view
        context = view.substr(sublime.Region(0, view.size()))
        replace_text = convert(context, False)

        view.replace(edit, sublime.Region(0, view.size()), replace_text)
        print('Converted  lowercase')


class ConvertUpperColorcodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, show_regions=True, show_panel=True):
        view = self.view
        context = view.substr(sublime.Region(0, view.size()))
        replace_text = convert(context)

        view.replace(edit, sublime.Region(0, view.size()), replace_text)
        print('Converted: uppercase')
