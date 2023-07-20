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

# %%writefile test.txt
Hello, this is the introduction to 2030 prediction.
This is the second line of the experiment. 
The possibilities of this are pretty endless near as I can tell. I'm actually really digging python.

pwd

myfile = open('test.txt')

myfile

myfile.read()

myfile.read()

myfile.seek(0)

myfile.read()

myfile.seek(0)

content = myfile.read()

print(content)

myfile.close()

myfile = open('test.txt')

mylines = myfile.readlines()
myfile.seek(0)
for line in mylines:
    print(line.split()[0])

myfile = open('test.txt','w+')
#opening with w or w+ tags causes the original file to be COMPLETELY overwritten

myfile.read()

myfile.write('positivity is the cream of the crop of reality')

myfile.seek(0)

myfile.read()

myfile.close()

myfile = open('test.txt','a+')
#if a+ ("append") can't find the stated file, it will create the file

myfile.write('A+ TIME')

myfile.close()

newfile = open('test.txt')

newfile.read()

myfile = open('oops.txt', mode='a+')

myfile.read()

myfile.write('adding a line using a+ mode')

myfile.seek(0)

myfile.read()

myfile.write('\nThis is a separated new line.')

myfile.seek(0)

myfile.read()

myfile.seek(0)

print(myfile.read())

myfile.close()

with open('oops.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()

myvariable


