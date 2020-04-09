# coding=utf8
from __future__ import unicode_literals, absolute_import, division, print_function
"""
dice.py - Dice Module
Copyright 2010-2013, Dimitri "Tyrope" Molenaars, TyRope.nl
Copyright 2013, Ari Koivula, <ari@koivu.la>
Licensed under the Eiffel Forum License 2.

https://sopel.chat/
"""


import random
import re
import operator

import sopel.module
from sopel.tools.calculation import eval_equation


@sopel.module.commands("dice")
def roll(bot, trigger):
    bot.say("Get your only damn dice")
