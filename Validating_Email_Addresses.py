# Given n pairs of names and email addresses as input, print each name and 
# email address pair having a valid email address on a new line.

import email.utils
import re

pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

N = int(input().strip())
for i in range(N):
    name, email_addr = email.utils.parseaddr(input().strip()) 
    if re.fullmatch(pattern, email_addr): 
        print(email.utils.formataddr((name, email_addr))) 