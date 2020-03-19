from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import operator
import sopel.module
import os
import sys


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def randprice(max):
    if max < 1:
        max = 5
    price = txt = random.randint(0, max)
    return price


"""
# Bot Restart/Update
"""



def restart(bot, trigger):
    bot.say(bot.nick + "Is Restarting the " + bot.nick + " Service...")
    os.system("systemctl stop sopel.service")
    #bot.say( 'say', "If you see this, the service is hanging. Making another attempt.")
    #bot.say("sudo service " + str(targetbot) + " restart")

"""
def update(bot, botcom, trigger, targetbot):
    # os.system("sudo chown -R spicebot:sudo /home/spicebot/.sopel/")
    joindpath = os.path.join("/home/spicebot/.sopel/", targetbot)
    osd(bot, botcom.channel_current, 'action', "Is Pulling " + str(joindpath) + " From Github...")
    g = git.cmd.Git(joindpath)
    g.pull()
    """
