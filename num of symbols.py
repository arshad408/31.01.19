import re
a = "a s d f # $ & ^ #  @ !"
new = re.sub('[\w]+' ,'', a)
