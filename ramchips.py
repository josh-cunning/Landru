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

moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)

import landrushared
import latinum

#____________CHIPS
def getbalanceram(bot,nick):
    bl=0
    bl = bot.db.get_nick_value(nick, 'rambank')
    return bl


def makeram(bot,nick):

    ###delay repeat by x secconds
    bl = 0
    supplies = supplybalance(bot,nick)
    lvl = getbotlvl(bot,nick)
    amount = 1
    cost = 2
    result = '0'
     #supply check
    if lvl ==2:
        cost = 1
    if cost > supplies:
        result = "You don't have enough supplies to make a chip"
        return result
    else:
        rams = getbalanceram(bot,nick)
        ramtot = rams + amount
        bl = bot.db.set_nick_value(nick, 'rambank', ramtot)
        addsupply(bot,nick,-abs(amount))
    return result

def addram(bot,nick,amount):
     ###Amount admin only
     ###delay repeat by x secconds
    bl = 0
    if not landrushared.is_digit(amount):
        amount = 1
    amount = int(amount)
    bl = bot.db.get_nick_value(nick, 'rambank') or 0
    bl = int(bl)
    bl =amount
    if bl<0:
        bl =0
    bot.db.set_nick_value(nick,'rambank',bl)


def sellram(bot):
     #limit how soon you can sell
    payout = 1
    stock = bot.db.get_nick_value('botstock', 'rambank') or 0
    if stock <=10:
        payout = 20
    elif (stock >10 and stock <=20):
        payout = 10
    elif (stock >20 and stock <=100):
        payout = 5
    return payout

def ramstock(bot):
    # random change to sell stockpile at some points
    bl = bot.db.get_nick_value('botstock', 'rambank') or 0
    return bl


#____________BOTS
def setrambots(bot,nick,amount):
    if not landrushared.is_digit(amount):
        amount = 1
    bot.db.set_nick_value(nick,' rambots ',amount)


def getrambot(bot,nick):
    ramworkers = 0
    ramworkers = bot.db.get_nick_value(nick, 'rambots') or 0
    return ramworkers

def addrambot(bot, nick, amount):
    bl = 0
    if not landrushared.is_digit(amount):
        amount = 1
    amount = int(amount)
    if amount <= 0:
        amount = 1
    totalbots = 0
    totalbots = bot.db.get_nick_value(nick, 'rambots') or 0
    cash =  latinum.getbalancelat(bot,nick)
    costbot = int(totalbots) + int(amount)
    if costbot <= cash:
        bl = totalbots + amount
        bot.db.set_nick_value(nick,'rambots',bl)
        latinum.addlat(bot,nick,-(costbot))
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



def supplybalance(bot, nick):

    bl = bot.db.get_nick_value(nick, 'supplies') or 0
    return bl

def addsupply(bot,nick,amount):
    bl = 0
    if not landrushared.is_digit(amount):
        amount = 1
    amount = int(amount)
    bl = supplybalance(bot,nick)
    bl = int(bl)
    bl = bl + amount
    bot.db.set_nick_value(nick,'supplies',bl)

def buysupplies(bot,nick,salesprice):
    cost = 0
    supplestock = supplybalance(bot,nick)
    cash = latinum.getbalancelat(bot,nick)
    lvl = getbotlvl(bot,nick)

    if lvl == 1:
        supplystorage = 50
    else:
        supplystorage = 100
    buying = supplystorage - supplestock
    cost = buying * salesprice
    if cash < cost :
        return 'Not enough cash'
    bot.db.set_nick_value(nick, 'supplies',supplystorage)
    latinum.addlat(bot,nick,-(cost))
    return cost
