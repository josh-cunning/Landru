from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import os
import sys
moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from ramchips import *

@sopel.module.commands("ram")
def moarram(bot, trigger):
    coms = trigger.group(2)
    #bot.say(str(coms))
    nick = trigger.nick
    if coms == 'add':
        amount = 1
        addram(bot,nick,amount)
        bot.say(nick + " gets " + str(amount) + " ramchips" )
    elif coms == 'balance':
        bl = 0
        bl = getbalance(bot,nick)
        bot.say(nick + " has " + str(bl) + " RAM chips")
    else:
        bot.say("Get your own ram")
