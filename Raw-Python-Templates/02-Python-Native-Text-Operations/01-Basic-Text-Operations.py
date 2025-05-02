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

print("hello")

person = "Cooper"
print(f"my name is {person}")

d={'a':Cooper, 'b':Frank}
print(f"my name is {d['a']}")

d={'a':Cooper, 'b':Frank}
print(f"my name is {d['a']}")

d={'a':'Cooper', 'b':'Frank'}
print(f"my name is {d['a']}")

list=[0,1,2]
print(f"I am {list[0]} years old")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
library

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author,topic,pages in library:
    print(f"Author is {author}; topic is {topic}; pages is {pages}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:{10}}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:>{10}}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:->{10}}")

from datetime import datetime
today=datetime(year=2022,month=7,day=5)
print(f"{today}")

print(f"{today:%B %d, %Y}")
#see strftime.org for https://strftime.org/ cheatsheet


