# import pandas
# data = pandas.read_csv("C:/Desktop/Downloads/nato_phonetic_alphabet.csv")
# print(data)
# print(data.to_dict())
# phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)
"""updates from day30section274. """
import pandas
data = pandas.read_csv("C:/Desktop/Downloads/nato_phonetic_alphabet.csv")
print(data)
print(data.to_dict())
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry, only alphabets allowed")
    else:
        print(output_list)
generate_phonetic()
