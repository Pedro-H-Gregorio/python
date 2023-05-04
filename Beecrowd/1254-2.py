# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"<([^>]*?)abc(.*?)>"

test_str = "<dont ABC replace abc>experience abc<replace abc abc>"

subst = "<\\1ZZZ\\2>"

# You can manually specify the number of replacements by changing the 4th argument
last = ""
#result = re.sub(regex, subst, test_str, 0, re.IGNORECASE)
result = test_str
while last != result:
	last = result
	result = re.sub(regex, subst, result, 0, re.IGNORECASE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

