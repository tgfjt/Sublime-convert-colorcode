# -*- coding: utf8 -*-

import sublime
import sublime_plugin

try:
    from .convert import convert
except:
    from convert import convert


class ConvertLowerColorcodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, show_regions=True, show_panel=True):
        selected = True

        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                replaced = convert(s, False)
                self.view.replace(edit, region, replaced)
            else:
                selected = False

        if selected is False:
            view = self.view
            context = view.substr(sublime.Region(0, view.size()))
            replace_text = convert(context, False)

            view.replace(edit, sublime.Region(0, view.size()), replace_text)

        print('Converted: lowercase')


class ConvertUpperColorcodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, show_regions=True, show_panel=True):
        selected = True

        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                replaced = convert(s)
                self.view.replace(edit, region, replaced)
            else:
                selected = False

        if selected is False:
            view = self.view
            context = view.substr(sublime.Region(0, view.size()))
            replace_text = convert(context)

            view.replace(edit, sublime.Region(0, view.size()), replace_text)

        print('Converted: uppercase')
