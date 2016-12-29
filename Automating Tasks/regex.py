import re
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?      # Area code
(\s|-|\.)?              # Separator(Space or (-) or (.))
\d{3}                   # First 3 Digits
(\s|-|\.)               # Separator(Space or (-) or (.))
\d{4}                   # Last 4 Digits
(\s*(ext|x|ext.)\s*\d{2,5})?        # Extentions
)''', re.VERBOSE)
mo=phoneRegex.search('My number is 989 565 5656ext.')
print('The Number is found at ' + mo.group())