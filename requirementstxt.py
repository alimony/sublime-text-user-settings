# encoding: utf-8

import os

import sublime_plugin


class RequirementsEventListener(sublime_plugin.EventListener):
    def on_load(self, view):
        fname = view.file_name()
        if not fname:
            return
        basename = os.path.basename(fname)
        if basename == 'requirements.txt':
            view.set_syntax_file('Packages/User/requirementstxt.tmLanguage')
