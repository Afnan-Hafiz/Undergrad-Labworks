def correct_capitalization(sentence):
    corrected_sentence = ''
    capitalize_next = True

    for char in sentence:
        if capitalize_next:
            corrected_sentence += char.upper()
            capitalize_next = False
        else:
            corrected_sentence += char.lower()

        if char in ['.', '!', '?']:
            capitalize_next = True
        elif char == 'i' and (corrected_sentence[-2] in [' ', '.', '!', '?']):
            corrected_sentence = corrected_sentence[:-1] + 'I'

    return corrected_sentence

user_input = input("Enter a sentence: ")
corrected_sentence = correct_capitalization(user_input)
print("Corrected sentence:", corrected_sentence)