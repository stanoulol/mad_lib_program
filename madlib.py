import os
from pathlib import Path
import string


p = Path('madlib.txt')
p.mkdir(exist_ok=True)

text = ''

with open(p, 'r') as f:
    text = f.read()
    print(text)


raw_text_list = text.split()

clean_text = text.translate((str.maketrans('','',string.punctuation)))
#Removing punctuation from the 'text' as without removing it, the text_list would contain elements like 'VERB.' and 'events.'


text_list = clean_text.split()

keyword_list = []

for element in text_list:
    if element in ['ADJECTIVE','NOUN','VERB','ADVERB'] :
        keyword_list.append(element)


word_list = []

for element in keyword_list:

    if element.startswith('A'):
        word = input(f'Enter an {element.lower()}\n')
        word_list.append(word)

    else:
        word = input(f'Enter a {element.lower()}\n')
        word_list.append(word)

i = -1

for text_element in text_list:

    if text_element in ['ADJECTIVE','NOUN','VERB','ADVERB']:
            index = text_list.index(text_element)
            i += 1
            text_list[index] = word_list[i]

    else:
        pass



punctuation_list = []



for element in raw_text_list:


    if element.endswith(tuple(string.punctuation)):
        punctuation_list.append(raw_text_list.index(element))


def punctuation_check_return(word):
    if word.endswith(tuple(string.punctuation))==True:
        return word[-1]



for index in punctuation_list:

    end = punctuation_check_return(raw_text_list[index])
    text_list[index] = f'{text_list[index]}{end}'


mad_lib_text = ' '.join(text_list)


with open('madlib_output.txt','w') as f:
    f.write(mad_lib_text)

