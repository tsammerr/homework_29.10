def pal():
    try:
        wordText = input('words -> ')
        wordText.replace(' ', '')
        wordTextCopy = wordText[::-1]
        if wordText == wordTextCopy:
            print('pallindrom')
        else:
            print('not pallindrom')
    except Exception as ex:
        print(f'Error: {ex}')

pal()