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

x = []
count = 0


while count < len(text):
    #if text[count][0] == 'p' or 'y' or 't' or 'h'or 'o' or 'n':
    if text[count][0] == 'p' or text[count][0] == 'y' or text[count][0] == 't' or text[count][0] == 'h'or text[count][0] == 'o' or text[count][0] =='n':
        x.append(text[count])
    
    #elif text[count][-1] == 'p' or 'y' or 't' or 'h'or 'o' or 'n':
    elif text[count][-1] == 'p' or text[count][-1] == 'y' or text[count][-1] == 't' or text[count][-1] == 'h'or text[count][-1] == 'o' or text[count][-1] == 'n':
        x.append(text[count])
    count = count + 1

print(f'Lista de palavras que começam ou terminam com uma das letras da palavra Python: {x}')
print(len(x))