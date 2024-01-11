"""
Moduły to pliki zawierające kod Pythona, natomiast pakiety to foldery, 
które zawierają moduły oraz specjalny plik __init__.py. 
Python ma również wiele modułów i pakietów wbudowanych, 
które są dostępne bez konieczności instalacji. 
"""

# Oblicz różnicę pomiędzy datami w dniach 
import datetime 
first_day = '2024-06-01'
second_day = '2024-07-18'

different_day = datetime.datetime.strptime(second_day, '%Y-%m-%d').date() - datetime.datetime.strptime(first_day, '%Y-%m-%d').date()

print(different_day)

print('---')

# znajdź wszystkie cyfry w podanym tekście
import re

string = 'Python 3.8'
numRe = r'\d'

onlyNumber = re.findall(numRe, string)

print(onlyNumber)

# znajdź wszystkie znaki alfanumeryczne w podanym tekście:
stringTwo = '!@#$%^&45wc'

searchLetter = r'\w'
pattern = re.compile(searchLetter)

myResult = pattern.findall(stringTwo)

print(myResult)

print('---')

import re

# znajdź wszystkie adresy email w podanym tekście:
raw_text = (
    'Send an email to: info@template.com or sales-info@template.it'
)

firstEmail = 'info@template.com'
secondEmail = 'sales-info@template.it'

onlyEmail = []


firstMatch = re.search(firstEmail, raw_text).group()
secondMatch = re.search(secondEmail, raw_text).group()

onlyEmail.append(firstMatch)
onlyEmail.append(secondMatch)


print(onlyEmail)

# II sposób
email = r'\b\w+[\w.-]*@\w+\.\w+\b'

searchEmail = re.findall(email, raw_text)

print(searchEmail)

print('---')

# podziel poniższy tekst względem białych znaków (spacji):
text = 'Programowanie w języku Python - od A do Z'

reText = r'\s+'

textNext = re.sub(reText, ",", text)

word = textNext.split(',')

print(word)

print('---')

# wydrukuj do konsoli ciąg znaków małych i dużych liter tak jak pokazano poniżej
import string

print(string.ascii_letters)

print('---')

# częstość występowania elementów w poniższej liście items:
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

yes = [(it) for it in items if it == 'YES']
no = [(it) for it in items if it == 'NO']
empty = [(it) for it in items if it == 'EMPTY']


print(f"YES: {yes.count('YES')}")
print(f"NO: {no.count('NO')}")
print(f"EMPTY: {empty.count('EMPTY')}")

# II SPOSÓB
import collections

countItems = collections.Counter(items)

print(countItems)

print('---')

# wybierz losowo (pseudolosowo) element z poniższej listy
import random
language = ['python', 'java', 'sql', 'c++', 'c']

random.seed(12)

randLanguage = random.choice(language)

print(randLanguage)

print('---')

# przestaw losowo (pseudolosowo) elementy z poniższej listy
items = ['python', 'java', 'sql', 'c++', 'c']
random.seed(15)
random.shuffle(items)
print(items)

print('---')