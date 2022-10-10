#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
__version__ = "$Revision: 0.9.3 $"
__date__ = "$Date: טו  תשרי  $"


* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License version 2
* as published by the Free Software Foundation.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
*
* Authors: Ilan Shavit <ilan.shavit@gmail.com> http://ilsh.info
*          Moshe Wagner <moshe.wagner@gmail.com>, http://dosilinux.wordpress.com
*          Meir Kriheli <meir@mksoft.co.il>, http://mksoft.co.il
*          Amiad Bareli <b@hatul.info>, https://hatul.info
"""

import subprocess
import time
from itertools import chain

ENG = """w/qtcdsvuzjyhlfkonibxg;p.mera,'"""
HEB = """'./אבגדהוזחטיךכלםמןנסעףפץצקרשת,"""

ENG_RANGE = chain(range(65, 90), range(97, 122)) # English letters
HEB_RANGE = range(1488, 1514)           # Hebrew letters

def get_selection():
    """Get the current selection"""

    time.sleep(0.3)
    proc = subprocess.Popen('xsel', shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode('utf-8')


def set_selection(content):
    """Put content in clipboard"""

    proc = subprocess.Popen('xsel -b -i', shell=True, stdin=subprocess.PIPE)
    proc.communicate(content.encode('utf-8'))


def translate(content, table=None, title_case=False):
    """Translates with optional translation table"""

    if not table:
        # create translataion dictionary, we map each char to it's order,
        # zip them and create a dict from the result.
        # The table is built base upon the 1st matching char

        # look for 1st english or hebrew
        first_eng = False
        for each_char in content:
            if ord(each_char) in ENG_RANGE:
                first_eng = True
                break
            if ord(each_char) in HEB_RANGE:
                break

        # compose the table depending on first english charr
        if first_eng:
            table = dict(zip(map(ord, HEB+ENG), map(ord, ENG+HEB)))
        else:
            table = dict(zip(map(ord, ENG+HEB), map(ord, HEB+ENG)))

    translated = content.lower().translate(table)

    if title_case:
        translated = translated.title()

    return translated


def send_paste():
    """Send CTRL+V combo to the window"""

    subprocess.call(r"xvkbd -text '\Cv'", shell=True)


if __name__ == '__main__':
    SELECTION = get_selection()
    SEL_TRANSLATED = translate(SELECTION)
    set_selection(SEL_TRANSLATED)
    send_paste()
