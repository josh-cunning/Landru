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
     costbots = int(totalbots) + int(amount)
     if costbot <= cash:
         bl = totalbots + amount
         bot.db.set_nick_value(nick,'rambots',bl)
         addlat(bot,nick,-(costbots))
         return True
     else:
         return False
