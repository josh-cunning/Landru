from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import os
import sys
import spicemanip

@sopel.module.commands("test")
def testbot, trigger):'
    triggerargsarray = spicemanip.main(trigger, 'create')
    triggerargsarray = spicemanip.main(triggerargsarray, '2+', "list")
    one = spicemanip.main(triggerargsarray, 1)
    amount = spicemanip.main(triggerargsarray,2)
    target = spicemanip.main(triggerargsarray,3)
    some = spicemanip.main(triggerargsarray,4)

    bot.say(str(target) + ' ' + str(amount) + " " + str(one) + " " + str(some))
