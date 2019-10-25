from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator

import sopel.module
import operator

import sopel.module

def getbalance(bot,nick):
    bl=0
    bl = bot.db.get_nick_value(nick, 'rambank') or 0
    return bl

def addram(bot,nick,amount):
     bl = 0
     bl = bot.db.get_nick_value(nick, 'rambank') or 0
     bl = int(bl) + amount
     bot.db.set_nick_value(nick,'rambank',bl)
