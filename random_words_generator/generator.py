##used the below code to generate 171000 words for the array in js named as words


""" import random
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

def load_dict():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        return [word.strip().lower() for word in content.splitlines()
                if len(word) > 2 and "'" not in word and not word[0].isupper()]


words = random.choices(load_dict(), k=171000)


js_array = f"const random_words = {json.dumps(words)};\nconsole.log('Loaded', myWords.length, 'words:', myWords);"

print(js_array) """
