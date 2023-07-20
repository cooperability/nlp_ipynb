# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

"""
"in" operator evaluates to a truth value for substrings e.g.
"hat" in "five hundred hats"? --> True
"[desired number]" in "patient cellphone: [desired number]" --> True
"""
text = "the phone number you need is 111-111-1111"
"111-111-1111" in text

#import regex library
#Regexes allow us to search for similarly formatted pattern searching in a text document
import re

pattern="phone"

re.search(pattern,text)

my_result=re.search(pattern,text)

my_result.span()

text = "phone home phone home phone home"

result=re.search(pattern,text)

result.span()

all_results = re.findall("phone",text)

len(all_results)

for result in re.finditer("phone",text):
    print(result.span())

text

text = "phone: 555-593-9327"

text

"""
Every character type has a pattern code:
\d for digits, e.g. the phone number below
\w for alphanumeric, e.g. \w-\w\w\w = A-b_1
\s for White space, e.g. a\sb\sc = a b c
\D for non-digit, e.g. \D\D\D = ABC
\W for non-alphanumeric, e.g. \W\W\W = *+_
\S for non-whitespace e.g. \S\S\S\S = yoyo
. for wildcard, can be any character
"""
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

phone_num=re.search(pattern,text)

phone_num

phone_num.group()

#now using quantifiers alongside pattern codes
"""
+ : occurs one or more times
{num} : occurs num times
{num1,num2}: occurs between num1 and num2 times
{num,} : occurs num or more times
*: occurs zero or more times
?: occurs once or zero times
\d$ for "ends with \d", ^\d for "starts with \d" 
square bracket anything which you want to exclude
"""
pattern=r'(\d{3})-(\d{3})-(\d{4})'
mymatch = re.search(pattern,text)
mymatch.group()

mymatch.group(1)

re.search(r"man|woman", "the woman jumped")

re.findall(r"..at", "The cat in the hat sat splat ratatatat")

re.findall(r"^\d", '1 is the loneliest number')

re.findall(r"^\d", 'one is the loneliest number')

re.findall(r"\d$", 'i like 2')



text="this sentence 45 has 10 three numbers 27 in it"
re.findall(r"[^\d]+",text)

text="this . is ? a ! string full of punctuation.?"
mylist=re.findall(r"[^!.? ]+",text)
mylist
' '.join(mylist)

text="only find hyphen-words, where are long-ish dashed-type words?"
re.findall(r'[\w]+-[\w]+',text)


