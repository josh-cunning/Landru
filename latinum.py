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
import landrushared

def getbalancelat(bot,nick):
    bl=0
    bl = bot.db.get_nick_value(nick, 'latbank') or 0
    return bl

def addlat(bot,nick,amount):

    if not landrushared.is_digit(amount):
        amount = 1
    amount = int(amount)
    bl = 0
    bl = bot.db.get_nick_value(nick, 'latbank') or 0
    bl = int(bl) + amount
    if bl<0:
        bl =0
    bot.db.set_nick_value(nick,'latbank',bl)

def setlats(bot,nick,amount):
    if not landrushared.is_digit(amount):
        amount = 1
    bot.db.set_nick_value(nick,'latbank' ,amount)
