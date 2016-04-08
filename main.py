# -*- coding: utf-8 -*-

""" Exercise 2
Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they
consist of can be found at
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
The API that this library provides is your choice.

** API **

Library is located in check_postcodes module. It offers next API:

is_valid_postcode(postcode) : Check if a string has a valid UK postcode
get_info(postcode): Get info like geo, lng, lat, etc. from a postcode

Examples:

from check_postcodes import is_valid_postcode, get_info

print is_valid_postcode('M1 1AE')
print get_info('W1A 2XX')

Run the examples with `python main.py`

** Requirements **
Postcodes==0.1

Install dependencies using `pip install -r requirements.txt`

** Test **
Run test doing `python test.py`
"""


from check_postcodes import is_valid_postcode, get_info


def main():
    """ Run some use cases check_postcodes"""

    print is_valid_postcode('W1A 2XX')
    print is_valid_postcode('W1A 2X!')  # Invalid
    print is_valid_postcode('SW1A 1AA')

    print is_valid_postcode('M1 1AE')
    print is_valid_postcode('B33 8TH')
    print is_valid_postcode('CR2 6XH')
    print is_valid_postcode('DN55 1PT')
    print is_valid_postcode('BFPO 11')
    print is_valid_postcode('AA1 1AA')  # True in format but No data

    print get_info('W1A 2XX')
    print get_info('W1A 2X!')  # Invalid
    print get_info('SW1 A1AA')

    print get_info('M1 1AE')
    print get_info('B33 8TH')
    print get_info('CR2 6XH')
    print get_info('DN55 1PT')
    print get_info('BFPO 11')  # True in format but No data
    print get_info('AA1 1AA')  # True in format but No data


if __name__ == "__main__":
    main()
