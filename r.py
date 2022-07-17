import sys

search_text = "DUMMY"
replace_text = sys.argv[1]

with open('dummy.plist', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
with open(r'dummy.plist', 'w') as file:
    file.write(data)
print("Text replaced")
