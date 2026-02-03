word = input('enter a word (enter nothing to stop):')


while not word == '':
    x = len(word)
    mid = x // 2
    if x % 2 == 0:
        print (word[mid-1:mid+1])
    else:
        print (word [mid])
    word = input('enter a word (enter nothing to stop):')
print('bye')