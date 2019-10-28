from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import operator
import sopel.module
import os
import sys
import spicemanip

from landrushared import *
from latinum import *

#____________CHIPS
def getbalanceram(bot,nick):
    bl=0
    bl = bot.db.get_nick_value(nick, 'rambank')
    return bl


def addram(bot,nick,amount):
    ###Amount admin only
    ###delay repeat by x secconds
     bl = 0

     if not is_digit(amount):
         amount = 1
     amount = int(amount)
     bl = bot.db.get_nick_value(nick, 'rambank') or 0
     bl = int(bl)
     bl = bl + amount

     if bl<0:
        bl =0
     bot.db.set_nick_value(nick,'rambank',bl)

def sellram(bot):
     #limit how soon you can sell
     stock = bot.db.get_nick_value('botstock', 'rambank') or 0
     if stock <=10:
        payout = 20
     elif (stock >10 and stock <=20):
        payout = 10
     elif (stock >20 and stock <=100):
        payout = 5
     elif (stock >100):
        payout = 1
     else:
        payout = 1
     return payout

def ramstock(bot):
    # random change to sell stockpile at some points
    bl = bot.db.get_nick_value('botstock', 'rambank') or 0
    return bl


#____________BOTS

def getrambot(bot,nick):
    ramworkers = 0
    ramworkers = bot.db.get_nick_value(nick, 'rambots') or 0
    return ramworkers

def addrambot(bot, nick, amount):
     bl = 0
     if not is_digit(amount):
         amount = 1
     amount = int(amount)
     if amount <= 0:
         amount = 1

     totalbots = 0
     totalbots = bot.db.get_nick_value(nick, 'rambots') or 0
     cash =  getbalancelat(bot,nick)
     costbot = int(totalbots) + int(amount)
     if costbot <= cash:
         bl = totalbots + amount
         bot.db.set_nick_value(nick,'rambots',bl)
         addlat(bot,nick,-(costbot))
         return True
     else:
         return False

def rambotwork(bot, nick):
     botcount =getrambot(bot,nick)
     botlvl = getbotlvl(bot,nick)
     ouptut = botcount


#________upgrades___________
def getbotlvl(bot,nick):
     botlvl =  bot.db.get_nick_value(nick, 'botlvl') or 0
     return botlvl

##### Supplies

def supplybot(bot):
    # random change to sell stockpile at some points
    bl = bot.db.get_nick_value('botstock', 'supplyprice') or 1
    return bl

def suppliesbot(bot, nick):

     bl = bot.db.get_nick_value(nick, 'supplies') or 0
     return bl

def buysupplies(bot,nick):
    supplestock = suppliesbot(bot,nick)
    bot.say(str(supplestock))
    if supplestock > 0:
        msg ='You already have: ' + str(supplestock) + ' supplies'
        return msg
    bot.say("cash")
    cash =  getbalancelat(bot,nick)
    lvl = getbotlvl(bot,nick)
    saleprice = supplybot(bot)
    bot.say(str(saleprice))
    cost = (supplestock * saleprice)
    if lvl == 1:
        supplystorage = 50
    else:
        supplystorage = 100
    if cash < cost :
        return 'Not enough cash'
    bot.db.set_nick_value(nick, 'botsupplies',supplystorage)
    addlat(bot,nick,-(cost))
    return '0'
