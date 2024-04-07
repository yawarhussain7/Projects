""" Conditions:
1. [a - z] alphabat with lowercase
2. [0-9] numbers
3. @ use one time 
4. @ use in last 3 or 2 postion

"""

import re

Email_Condition = "^[a-z] + [0-9] + [\._] ? [a-z 0-9] + [@] \w + [.]\w{2,3}$"
