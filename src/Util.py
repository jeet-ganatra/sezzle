import random
import string


class Util:

    @staticmethod
    def generate_unique_key():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))