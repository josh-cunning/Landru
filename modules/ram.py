from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator

import sopel.module
import operator

import sopel.module
from sopel.tools.calculation import eval_equation

@sopel.module.commands("ram")
def moarram(bot, trigger):
    answer = ["More RAM is better", "Please insert 5 quarts of blood for moar ram", "It's my ram and you can't have any"," I checked and we don't care what you want"]
    max = len(answer)
    txt = random.randint(0, max)
    bot.say(str(txt))
    quote = answer[txt]    
    bot.say(quote)
