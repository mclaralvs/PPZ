text = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''

text = text.lower()
text = text.replace(',', ' ')
text = text.replace('.', ' ')
text = text.replace(':', ' ')
text = text.split()

def tem_em_python(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

v = []

for p in text:
    if tem_em_python(p) and len(p) > 4:
        v.append(p)

print(v)
print(len(v))