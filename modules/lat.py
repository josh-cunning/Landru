# coding=utf8
from __future__ import unicode_literals, absolute_import, division, print_function

import random
import re
import operator
import sopel.module
import os
import sys
import spicemanip

moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from landrushared import *
from latinum import *


@sopel.module.commands("lat")
def moarlat(bot, trigger):
        coms =''
        triggerargsarray = spicemanip.main(trigger, 'create')
        maincom = spicemanip.main(triggerargsarray, 1).lower()[1:]
        triggerargsarray = spicemanip.main(triggerargsarray, '2+', "list")
        coms = spicemanip.main(triggerargsarray,1)
        nick = trigger.nick
        if not coms:
            bl = 0
            bl = getbalancelat(bot,nick)
            bot.say(nick + " has " + str(bl) + " bars of latinum")
        elif coms == 'balance':
            bl = 0
            bl = getbalancelat(bot,nick)
            bot.say(nick + " has " + str(bl) + " bars of latinum")
        elif coms == 'setlats':
            if bot.channels[trigger.sender].privileges[nick] < sopel.module.HALFOP:
                return bot.reply("Unauthorized access detected!")
            target = spicemanip.main(triggerargsarray,3) or 0
            amount = spicemanip.main(triggerargsarray,2)
            if not landrushared.is_digit(amount):
                amount =  1
            if not target == 0:
                nick = target
            latinum.setlats(bot,nick,amount)
            key = " now has: "
            #amount = abs(amount)
            bot.say(nick + key + str(amount) + " latinum bars" )



        else:
            bot.say("Try checking again later")
