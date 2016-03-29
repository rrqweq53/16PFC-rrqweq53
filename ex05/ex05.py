# -*- coding: cp949
name = 'jang woo seung'
age = 21
height_cm = 173
cm_to_inch = 1.0 / 2.54
my_height_inch = height_cm * cm_to_inch
my_weight = 79
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d inch tall." % my_height_inch
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If i add %d, %d, and %d I get %d." % (age, height_cm, my_weight, age + height_cm + my_weight)