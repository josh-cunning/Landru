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
import ramchips
import landrushared
import latinum


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
        result = ramchips.makeram(bot,nick)
        if result == '0':
            bot.say(nick + " gets " + str(amount) + " ramchips" )
        else:
            bot.say(str(result))
    else:

        if coms == 'add':
            if bot.channels[trigger.sender].privileges[nick] < sopel.module.HALFOP:
                return bot.reply("You are not a channel operator!")
            target = spicemanip.main(triggerargsarray,3) or 0
            amount = spicemanip.main(triggerargsarray,2)
            if not target == 0:
                nick = target
            if not landrushared.is_digit(amount):
                amount =  1
            amount = int(amount)
            ramchips.addram(bot,nick,amount)
            if int(amount) > 0:
                key = " gets "
            else:
                key = " loses "
            amount = abs(amount)
            bot.say(nick + key + str(amount) + " ramchips" )

        elif coms == 'balance':
            #bl = 0
            target = spicemanip.main(triggerargsarray,2) or 0
            amount = spicemanip.main(triggerargsarray,3)
            bot.say(str(target) + ' ' + str(amount))
            if not target == 0:
                nick = target
            bot.say(str(nick))
            #bl = ramchips.getbalanceram(bot,nick)
            #bot.say(nick + " has " + str(bl) + " RAM chips")

        elif coms == 'stock':
            bl = ramchips.getbalanceram(bot, 'botstock')
            bot.say("The center warehouse has " + str(bl) + " RAM chips")
            payout = ramchips.sellram(bot)
            bot.say("Ram is currently selling for " + str(payout))

        elif coms =='ramhouse':
            amount = spicemanip.main(triggerargsarray,2)
            if not landrushared.is_digit(amount):
                amount =  1
            ramchips.addram(bot,'botstock',amount)
            bot.say("Bot stock gets: " + amount + " RAM chips")

        elif coms == 'sell':
            payout = ramchips.sellram(bot)
            sale = ramchips.getbalanceram(bot,nick)
            if sale > 0:
                payment = sale * payout
                latinum.addlat(bot, nick, payment)
                bot.say(nick + " sells " + str(sale) + " for " + str(payment))
                ramchips.addram(bot,'botstock',sale)
                ramchips.addram(bot,nick,-abs(sale))
            else:
                bot.say(nick + " does not have chips to sell")

        elif coms == 'buybot':
            amount = spicemanip.main(triggerargsarray,2)
            if not landrushared.is_digit(amount):
                amount =  1
            if ramchips.addrambot(bot,nick,amount):
                if amount == 1:
                    key = " buys a worker bot "
                else:
                    key = " buys " + str(amount) + " worker bots "
                bot.say(nick + key)

        elif coms == 'supplies':
            bl = ramchips.supplybalance(bot, nick)
            action = spicemanip.main(triggerargsarray,2)
            pricing = landrushared.randprice(50)

            if not action == 'buy':
                bot.say(" You have: " + str(bl) + " supplies. supplies currently cost: " + str(pricing))
            else:
                if  (action == 'buy'):
                    purchase = ramchips.buysupplies(bot,nick,pricing)

                    if not purchase == 0:
                        bot.say(" You have refilled your supplies for " + str(purchase) + " bars of latinum")
                    else:
                        bot.says(str(purchase))
                else:
                    bot.say(" You already have: " + str(bl) + " supplies")



        elif coms == 'help':
            helpcmd = spicemanip.main(triggerargsarray,2)
            helpfile = "type help command name to see more: stock, add, balance, sell,buy,upgrades"
            if helpcmd == 'stock':
                helpfile = 'The stock command will show you how many ram chips are in the warehouse and what the current sell price is'
            elif helpcmd == 'balance':
                helpfile = 'The balance command will show you how many ram chips you have built'
            elif helpcmd == 'add':
                helpfile = 'The add command will build 1 ram chip, typing without a command also builds a chip. It takes 2 supply counts'
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
            bot.say(helpfile)




        else:
            bot.say("I don't know what your trying to do. Type !ram help for help")
