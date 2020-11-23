from spellchecker import SpellChecker
import pandas as pd

spell = SpellChecker()
data = pd.read_csv('  ')#Ввести путь до датасета

count=0
misspelled = spell.unknown(data)
for word in misspelled:
    a=(spell.correction(word))
    count = count + 1
print (count)
count=float(count)

def get_words(data):
    with open(data, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def main():
    filename = (r'  ')#Ввести путь до датасета
    words = get_words(filename)
    a=len(words)
    print(a)
    n=0
    while n<=a:
        n = n + 1
    print(float(count / n) * 100,"%")


if __name__ == "__main__":
    main()

