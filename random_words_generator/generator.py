#ccode for approx  4000 words words

import random
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

def get_words():
    url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        return [word.strip().lower() for word in content.splitlines()
                if len(word) > 2 and "'" not in word and not word[0].isupper()]

all_words = random.choices(get_words(), k=4000)
print("Generated " + str(len(all_words)) + " words!\n")

# splitted the output into parts because VS code can't process such long lines
size = 1000
part1 = all_words[0:size]
part2 = all_words[size:size*2] 
part3 = all_words[size*2:size*3]
part4 = all_words[size*3:]

print(f"const list1 = {json.dumps(part1)};")
print()
print(f"const list2 = {json.dumps(part2)};")
print()
print(f"const list3 = {json.dumps(part3)};")
print()
print(f"const list4 = {json.dumps(part4)};")
print()
