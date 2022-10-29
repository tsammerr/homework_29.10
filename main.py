def wor():
    try:
        wordsText  = input('enter text -> ')

        res = wordsText.count('.') +wordsText.count('!') + wordsText.count('?')

        print(res)

    except Exception as ex:
        print (f'Error information: {ex}')
wor()
