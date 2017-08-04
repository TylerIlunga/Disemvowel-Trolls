import re

def disemvowel(string):
    vowels = "aeiouAEIOU"
    for c in vowels:
        pass
        string = re.sub(c, "", string)
    return string

print disemvowel("This website is for losers LOL!")
