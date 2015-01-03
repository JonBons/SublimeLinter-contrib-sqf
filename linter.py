#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Inspiration by Aparajita Fishman's Lua linter
# Written by Samuel Maddock
# Copyright (c) 2014 gmodcoders
#
# License: MIT
#

"""This module exports the SQF plugin class."""

from SublimeLinter.lint import Linter, util


class SQF(Linter):

    """Provides an interface to sqfc -p."""

    syntax = 'sqf'
    cmd = 'sqfc -p * -'
    regex = r'^((?P<error>[E])|(?P<warning>[W])):.+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+?(?:near (?P<near>\'.+\')|$))'
    error_stream = util.STREAM_STDOUT
