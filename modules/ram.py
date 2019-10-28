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
            if sale > 0:
                payment = sale * payout
                addlat(bot, nick, payment)
                bot.say(nick + " sells " + str(sale) + " for " + str(payment))
                addram(bot,'botstock',sale)
                addram(bot,nick,-abs(sale))
            else:
                bot.say(nick + " does not have chips to sell")

        elif coms == 'buybot':
            amount = spicemanip.main(triggerargsarray,2)
            if not is_digit(amount):
                amount =  1
            if addrambot(bot,nick,amount):
                key = " buys "
                bot.say(nick + key + " worker bots")

        elif coms == 'supplies':
            purchase = buysupplies(bot,nick)
            if purchase == '0':
                bot.say(" You have filled your supplies")
            else:
                bot.say(purchase)



        elif coms == 'help':
            helpcmd = spicemanip.main(triggerargsarray,2)
            helpfile = "type help command name to see more: stock, add, balance, sell,buy,upgrades"
            if helpcmd == 'stock':
                helpfile = 'The stock command will show you how many ram chips are in the warehouse and what the current sell price is'
            elif helpcmd == 'balance':
                helpfile = 'The balance command will show you how many ram chips you have built'
            elif helpcmd == 'add':
                helpfile = 'The add command will build 1 ram chip, typing without a command also builds a chip. Your storage will only hold 50 at time'
            elif helpcmd == 'sell':
                helpfile = 'The sell command will sell all the ram chips you have in storage for latinum see the stock command for current prices'
            elif helpcmd == 'buy':
                helpfile = 'The buy command will buy factory robots to make chips for you. You can include an amount. Bot prices are based your total bot count'
            elif helpcmd == 'upgrades':
                helpfile = 'The upgrades command with upgrade your factory you. Each lvl gives you more features for a higher cost.'
                #LVL 1: 500 bar: supplies storage goes to 100
                # lvl 2:2500 bars ram uses half suppleis
                #lvl 3: 5000 bars marketingbot your ram sells for 1 extra bar per chips
                #lvl 4: 8000 bars auto buy supplies
                #lvl 5: 12000 bars: supplies          



            else:
                bot.say("Get your own ram")
