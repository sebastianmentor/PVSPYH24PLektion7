def print_age_plus_ten(age):
    print(age + 10)


def number_of_words_in_text(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words


my_age = 30
document = 'Hejsan! Mitt namn är Sebastian\
    och jag skriver massa ord för att det \
        kan vara roligt ibland.'

print_age_plus_ten(my_age)

print(f'Antal ord i texten är {number_of_words_in_text(document)}')