from __future__ import unicode_literals, absolute_import, print_function, division

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


@sopel.module.commands("restart")
def restartbot(bot, trigger):
    bot.say("restartbot")
    nick = trigger.nick
    if bot.channels[trigger.sender].privileges[nick] < sopel.module.HALFOP:
        return bot.reply("You are not a channel operator!")
    bot.say("Restarting")
    landrushared.restart(bot,trigger)
