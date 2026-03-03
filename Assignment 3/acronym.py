phrase = input('enter a phrase:')

while not phrase == '':
    words = phrase.split()
    acronym = ""
    for i in words:
        first_word = i[0]
        cap = str.capitalize(first_word)
        acronym = acronym + cap
    print(acronym)
    phrase = input('enter a phrase:')
else:
    print('bye')