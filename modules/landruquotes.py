# coding=utf8
from __future__ import unicode_literals, absolute_import, division, print_function

import random
import re
import operator

import sopel.module
import operator

import sopel.module
from sopel.tools.calculation import eval_equation

@sopel.module.commands("landru")
def qoutes(bot, trigger):
        answer = ["More RAM is better", "Please insert 5 quarts of blood for moar ram", "It's my ram and you can't have any"," I checked and we don't care what you want"]
        max = len(answer)
        txt = random.randint(0, max)
        quote = answer[txt]
        bot.say(quote)
