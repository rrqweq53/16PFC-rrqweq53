# -*- coding: cp949
from sys import argv

script, user_name, second = argv
prompt = '> '

print "Hi %s, I'm the %s script. and %r version" % (user_name, script, second)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me .
you live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)