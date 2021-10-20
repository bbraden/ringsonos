import re
 
# string for passing
text = "Welcome to geeks for geeks [GFG] A (computer scienc{e p}ortal)"
 
# creating the regex pattern & use re.sub()
# [\([{})\]] is a RE pattern for selecting
# '{', '}', '[', ']', '(', ')' brackets.
patn = re.sub(r"[\[\]]", "", text)
 
print(patn)