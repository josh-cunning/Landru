from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import os
import sys
import spicemanip

@sopel.module.commands("test")
def testbot(bot, trigger):
    triggerargsarray = spicemanip.main(trigger, 'create')
    triggerargsarray = spicemanip.main(triggerargsarray, '2+', "list")
    one = spicemanip.main(triggerargsarray,1)
    two = spicemanip.main(triggerargsarray,2)
    three = spicemanip.main(triggerargsarray,3)
    four = spicemanip.main(triggerargsarray,4)

    #bot.say(str(one) + ' ' + str(two) + " " + str(three) + " " + str(four))

    if one == 'one':
        bot.say("Number One")
        if two == 'two':
            bot.say("Two for One")
        elif two == 'three':
            bot.say("Three for one")
    elif one == 'two':
        bot.say('Number Two')
    elif one  == 'three':
        bot.say('Number Three')
    elif one == 'four':
        bot.say('Number Four')
    else:
        bot.say(str(one) + ' ' + str(two) + " " + str(three) + " " + str(four))
