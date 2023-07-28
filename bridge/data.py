"""
    Fichero para generar random id
"""

import random
import string


def generate_id(length):
    """
        Function to create a random id

        :Params length: length of the string id
        :Type length: int

        :Return str
    """

    ans = ''
    for _ in range(length):
        ans += str(random.choice(string.ascii_letters))
    
    return ans

