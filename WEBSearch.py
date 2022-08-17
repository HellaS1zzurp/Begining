import os

while True:
    try:
        redirect_to = input('Введите ссылку:\n')
        if redirect_to == 'пока':
            break
            exit()

        if 'https://' in redirect_to:
            os.system ('start ' + redirect_to)

        elif 'www.' in redirect_to:
            redirect_to = 'https://' + redirect_to
            os.system ('start ' + redirect_to)

        else:
            redirect_to = 'https://www.' + redirect_to
            os.system ('start ' + redirect_to)
            
    finally:
        print(redirect_to, ' открылся!')
