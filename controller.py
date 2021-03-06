# coding=utf8
from __future__ import unicode_literals, absolute_import, division, print_function

import random
import re
import operator
import sopel.module
import operator
import sopel.module
import os
import sys
import landrushared

import sopel.module
from sopel.tools.calculation import eval_equation


moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)

@sopel.module.commands("restart")
def restartbot(bot, trigger):
    bot.say("restartbot")
    nick = trigger.nick
    if bot.channels[trigger.sender].privileges[nick] < sopel.module.HALFOP:
        return bot.reply("You are not a channel operator!")
    bot.say("Restarting")
    landrushared.restart(bot,trigger)
