Exercise 2

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

