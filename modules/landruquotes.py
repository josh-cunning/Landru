from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator

import sopel.module
# from sopel.tools.calculation import eval_equation

@sopel.module.commands("landru")
def qoutes(bot, trigger):
    bot.say("Landru is always watching you.")
