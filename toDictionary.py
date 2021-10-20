import re
import json
import ast

def toDict(thing):
    q = re.sub(r"[\[\]]", "", thing)
    f = re.sub(r"[\']", r'"', q)
    o  = ast.literal_eval(f)
    return o