import re

text = '''
666-666-666
698.054.102
159.474.813
'''
text2 = '666-666-666'
pattern = r'\d{3}[.-]\d{3}[.-]\d{3}'

me1 = re.finditer(pattern, text)
z = me1.__next__().string
print(z.split())

me2 = re.search(pattern, text)
print(me2)

me3 = re.findall(pattern, text)
print(me3)

me4 = re.split(r'[.]', text)
print(me4)

me5 = re.match(r'666', text2)
print(me5)

me6 = re.fullmatch(r'666', text2)
print(me6)

me7 = re.sub(r'666', '999', text)
print(me7)

me8 = re.subn(r'666', '999', text)
print(me8)