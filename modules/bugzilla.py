# coding=utf-8
"""Bugzilla issue reporting module

Copyright 2013-2015, Embolalia, embolalia.com
Licensed under the Eiffel Forum License 2.
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import re
import requests

import xmltodict

from sopel import tools
from sopel.config.types import StaticSection, ListAttribute
from sopel.logger import get_logger
from sopel.module import rule


regex = None
LOGGER = get_logger(__name__)


class BugzillaSection(StaticSection):
    domains = ListAttribute('domains')
    """The domains of the Bugzilla instances from which to get information."""


def configure(config):
    """
    | name | example | purpose |
    | ---- | ------- | ------- |
    | domains | bugzilla.redhat.com,bugzilla.mozilla.org | A list of Bugzilla issue tracker domains |
    """
    config.define_section('bugzilla', BugzillaSection)
    config.bugzilla.configure_setting(
        'domains',
        'Enter the domains of the Bugzillas you want extra information '
        'from (e.g. bugzilla.gnome.org)'
    )


def setup(bot):
    global regex
    bot.config.define_section('bugzilla', BugzillaSection)

    if not bot.config.bugzilla.domains:
        return
    if not bot.memory.contains('url_callbacks'):
        bot.memory['url_callbacks'] = tools.SopelMemory()

    domains = '|'.join(bot.config.bugzilla.domains)
    regex = re.compile((r'https?://(%s)'
                        r'(/show_bug.cgi\?\S*?)'
                        r'(id=\d+)')
                       % domains)
    bot.memory['url_callbacks'][regex] = show_bug


def shutdown(bot):
    try:
        del bot.memory['url_callbacks'][regex]
    except KeyError:
        # bot.config.bugzilla.domains was probably just empty on startup
        # everything's daijoubu
        pass


@rule(r'.*https?://(\S+?)'
      r'(/show_bug.cgi\?\S*?)'
      r'(id=\d+).*')
def show_bug(bot, trigger, match=None):
    """Show information about a Bugzilla bug."""
    match = match or trigger
    domain = match.group(1)
    if domain not in bot.config.bugzilla.domains:
        return
    url = 'https://%s%sctype=xml&%s' % match.groups()
    data = requests.get(url).content
    bug = xmltodict.parse(data).get('bugzilla').get('bug')
    error = bug.get('@error', None)  # error="NotPermitted"

    if error:
        LOGGER.warning('Bugzilla error: %s' % error)
        bot.say('[BUGZILLA] Unable to get infomation for '
                'linked bug (%s)' % error)
        return

    message = ('[BUGZILLA] %s | Product: %s | Component: %s | Version: %s | ' +
               'Importance: %s |  Status: %s | Assigned to: %s | ' +
               'Reported: %s | Modified: %s')

    resolution = bug.get('resolution')
    if resolution is not None:
        status = bug.get('bug_status') + ' ' + resolution
    else:
        status = bug.get('bug_status')

    assigned_to = bug.get('assigned_to')
    if isinstance(assigned_to, dict):
        assigned_to = assigned_to.get('@name')

    message = message % (
        bug.get('short_desc'), bug.get('product'),
        bug.get('component'), bug.get('version'),
        (bug.get('priority') + ' ' + bug.get('bug_severity')),
        status, assigned_to, bug.get('creation_ts'),
        bug.get('delta_ts'))
    bot.say(message)
