correct_username = 'python'
correct_password = 'rules'

attempts = 0

while attempts < 5:
    username = input('enter username:')
    password = input('enter password:')

    if username == correct_username and password == correct_password:
        print('welcome')
        break
    else:
        print('incorrect username or password')
        attempts = attempts + 1
        if attempts == 5:
            print ('Access denied')