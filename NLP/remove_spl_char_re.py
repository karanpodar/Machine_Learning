import re

text = "@r@n !*v$s $#%"

text = re.sub('[^a-zA-Z0-9]', ' ', text)
text = re.sub('\s+', ' ', text)

print(text)
