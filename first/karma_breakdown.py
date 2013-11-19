#!/usr/bin/python
import praw

user_agent = ("Karma breakdown 1.0 by /u/eldhom" 
				"github.com:Yoggiburken/RedditBots.git")
r = praw.Reddit(user_agent=user_agent)
user_name = "eldhom"
user = r.get_redditor(user_name)
thing_limit = 100
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) 
									+ thing.score)
	print(karma_by_subreddit)

