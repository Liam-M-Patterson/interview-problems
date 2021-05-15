import re
def URLify(string, length):
    return re.sub(' ', '%20', string[:length])

name = "Liam Patterson"
print(URLify(name, len(name)))
print(URLify(name + "   d",4+ len(name)))



