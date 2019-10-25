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
from ramchips import *
from landrushared import *
from latinum import *


@sopel.module.commands("ram")
def moarram(bot, trigger):
    coms =''
    triggerargsarray = spicemanip.main(trigger, 'create')
    maincom = spicemanip.main(triggerargsarray, 1).lower()[1:]
    triggerargsarray = spicemanip.main(triggerargsarray, '2+', "list")
    # bot.say(str(triggerargsarray))
    coms = spicemanip.main(triggerargsarray,1)
    # bot.say(str(coms))
    nick = trigger.nick
    if not coms:
        amount = 1
        addram(bot,nick,amount)
        bot.say(nick + " gets " + str(amount) + " ramchips" )
    else:
        if coms == 'add':
            amount = spicemanip.main(triggerargsarray,2)
            if not is_digit(amount):
                amount =  1
            amount = int(amount)
            addram(bot,nick,amount)
            if int(amount) > 0:
                key = " gets "
            else:
                key = " loses "
            amount = abs(amount)
            bot.say(nick + key + str(amount) + " ramchips" )

        elif coms == 'balance':
            bl = 0
            bl = getbalanceram(bot,nick)
            bot.say(nick + " has " + str(bl) + " RAM chips")

        elif coms == 'stock':
            bl = getbalanceram(bot, 'botstock')
            bot.say("The center warehouse has " + str(bl) + " RAM chips")
            payout = sellram(bot)
            bot.say("Ram is currently selling for " + str(payout))

        elif coms =='ramhouse':
            amount = spicemanip.main(triggerargsarray,2)
            if not is_digit(amount):
                amount =  1
            addram(bot,'botstock',amount)
            bot.say("Bot stock gets: " + amount + " RAM chips")

        elif coms == 'sell':
            payout = sellram(bot)
            sale = getbalanceram(bot,nick)
            if sale > 0
                payment = sale * payout
                addlat(bot, nick, sale)
                bot.say(nick + " sells " + str(sale) + " for " + str(payment))
                addram(bot,'botstock',sale)
                addram(bot,nick,-abs(sale))
            else:
                bot.say(nick + " does not have chips to sell")

        else:
            bot.say("Get your own ram")
