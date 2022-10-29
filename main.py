def word():
    try:
        text = input('text -> ')
        wordsText = input('words -> ')
        words = wordsText.split()
        print(words)
        for word in words:
          if text.count(word) > 0:
            origen = word
            teep = word.upper()

            text = text = text.replace(origen, teep)
        print(text)
    except Exception as ex:
        print(f'Error: {ex}')

word()