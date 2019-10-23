from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import operator
import sopel.module
from sopel.tools.calculation import eval_equation
from sopel.modules.ramchips import *

@sopel.module.commands("ram")
def moarram(bot, trigger):
    coms = trigger.group(2)
    bot.say(str(coms))
    nick = trigger.nick
    if coms == 'add':
        amount = 1
        addram(bot,nick,amount)
        bot.say(nick + " gets " + str(amount) + " ramchips" )
    elif coms == 'balance':
        bl = getbalance(bot,nick)
        bot.say(str(bl))
    else:
        bot.say("Get your own ram")
