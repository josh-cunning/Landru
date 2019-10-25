from __future__ import unicode_literals, absolute_import, print_function, division

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
        else:
            bot.say("Try checking again later")
