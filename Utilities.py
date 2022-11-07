import re


class Utilities:

    @staticmethod
    def cut_first_letter(word):
        word = word[1:]
        return word

    print(cut_first_letter('$33'))

    @staticmethod
    def leave_only_digits(word):
        return re.sub(r'[^0-9.]', '', word)

