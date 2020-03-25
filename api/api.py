# -*- coding: utf-8 -*-
"""
PATRICK GASTON 100 Plus Coding Challenge

This API will have 2 endpoints:

/generate (GET)
- A route to generate and return a Medicare Beneficiary Identifier (MBI)

/verify (POST
- A route to verify a passed in MBI


Note: the MBI format (Jan 1, 2020) can be found at:
        https://www.cms.gov/Medicare/New-Medicare-Card/Understanding-the-MBI.pdf
"""

import flask
import random
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

# identify post to type for MBI format
# note: creating a dict to be more modular in case the formatting ever changes
mbi_format_dict = {
    1: 'C',
    2: 'A',
    3: 'AN',
    4: 'N',
    5: 'A',
    6: 'AN',
    7: 'N',
    8: 'A',
    9: 'A',
    10: 'N',
    11: 'N',
}

# define MBI Character group params
alpha_exceptions = ["S", "L", "O", "I", "B", "Z"]


# A route to generate and return a Medicare Beneficiary Identifier (MBI)
@app.route('/generate', methods=['GET'])
def generate_mbi():
    # response object
    response = {
        'mbi': get_random_mbi()
    }
    return jsonify(response)


# A route to verify a passed in MBI
@app.route('/verify', methods=['POST'])
def verify_mbi():
    input_mbi = request.args.get('mbi')

    # return 400 error if there is a bad request
    if input_mbi is None:
        return "You must pass in a valid MBI", 400

    # response object
    response = {
        'isValid': validate_mbi(input_mbi)
    }
    return jsonify(response)


# FUNCTIONS
def get_random_mbi() -> str:
    """ A function to generate a random mbi and return as string
        note: the MBI format (Jan 1, 2020) can be found at:
        https://www.cms.gov/Medicare/New-Medicare-Card/Understanding-the-MBI.pdf

            Returns:
                @return str
        """

    # create mbi as array to add mbi groups
    mbi = []

    for x in range(1, 12):
        # check character groups from mbi_format_dict and
        # append to mbi based on format
        print("loop # {}".format(x))

        # C - Numeric 1 thru 9
        if mbi_format_dict.get(x) == 'C':
            mbi.append(get_random_int(1, 9))

        # N - Numeric 0 thru 9
        if mbi_format_dict.get(x) == 'N':
            mbi.append(get_random_int(0, 9))

        # AN - Either A or N
        if mbi_format_dict.get(x) == 'AN':
            # generate random int
            random_int = random.randint(1, 2)
            # A - Alphabetic Character (A...Z); Excluding (S, L, O, I, B, Z)
            if random_int == 1:
                mbi.append(get_random_alpha(alpha_exceptions))
            # N - Numeric 0 thru 9
            if random_int == 2:
                mbi.append(get_random_int(0, 9))

        # A - Alphabetic Character (A...Z); Excluding (S, L, O, I, B, Z)
        if mbi_format_dict.get(x) == 'A':
            mbi.append(get_random_alpha(alpha_exceptions))

    return ''.join(mbi)


def get_random_int(first: int, second: int) -> str:
    """ A function to generate random int based on passed in params

            Returns:
                @return str
        """
    return str(random.randint(first, second))


def get_random_alpha(exceptions: list) -> str:
    """ A function to generate random alpha with exceptions as parameters

            Returns:
                @return str
        """
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    random_char = random.choice(capital_letters)

    while random_char in exceptions:
        random_char = random.choice(capital_letters)

    return random_char


def validate_mbi(mbi: str) -> bool:
    """ A function to validate format for passed in mbi

            Returns:
                @return bool
        """

    is_valid = True

    # if the input is not the same size of the mbi_formatter, return False
    if len(mbi) != len(mbi_format_dict):
        is_valid = False

    for x in range(0, len(mbi_format_dict)):
        value = mbi_format_dict.get(x + 1)
        # Check C
        if value == 'C':
            if not mbi[x].isnumeric() or mbi[x] == 0:
                is_valid = False
                break
        # Check N
        if value == 'N':
            if not mbi[x].isnumeric():
                is_valid = False
                break
        # Check AN
        if value == 'AN':
            if mbi[x] in alpha_exceptions:
                is_valid = False
                break
        # Check A
        if value == 'A':
            if not mbi[x].isalpha() or mbi[x] in alpha_exceptions:
                is_valid = False
                break

    return is_valid


if __name__ == "__main__":
    app.run(debug=True)
