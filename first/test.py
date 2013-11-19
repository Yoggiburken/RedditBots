#!/usr/bin/python

import time
import praw

r = praw.Reddit('Test program by /u/eldhom')
r.login('fire_bot', 'firebotbot')
r.user.send_message('eldhom', 'HELLO! :D')
