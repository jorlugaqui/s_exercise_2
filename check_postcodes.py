# -*- coding: utf-8 -*-

"""Context:
The structure of a postcode is a one or two-letter postcode area code named
for a local town or area of London, one or two digits signifying a district
in that region, a space, and then an arbitrary code of one number and two
letters. For example, the postcode of the University of Roehampton in London
is SW15 5PU, where SW stands for south-west London. The postcode of GCHQ is
GL51 0EX, where GL signifies the postal town of Gloucester.

There is a library which gets info based on postcode, let's use it :)
https://postcodes.readthedocs.org/en/latest/
"""

import re
from postcodes import PostCoder


def is_valid_postcode(postcode):
    """Check if a postcode is valid

    Key arguments:
    postcode    -- The postcode given (string)

    Return True if the post code is valid, otherwise False
    """

    # I found this awesome article:
    # http://tech.marksblogg.com/uk-postcodes.html

    pattern = '^([A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]|[A-HK-Y][0-9]([0-9]|' + \
        '[ABEHMNPRV-Y]))|[0-9][A-HJKS-UW])\ [0-9][ABD-HJLNP-UW-Z]{2}|' + \
        '(GIR\ 0AA)|(SAN\ TA1)|(BFPO\ (C\/O\ )?[0-9]{1,4})|' + \
        '((ASCN|BBND|[BFS]IQQ|PCRN|STHL|TDCU|TKCA)\ 1ZZ))$'

    _POSTCODE_RE = re.compile(pattern)
    _postcode = postcode.strip().upper()
    return _POSTCODE_RE.match(_postcode) != None


def get_info(postcode):
    """Get info from postcode

    Key arguments:
    postcode   --  The postcode given (string)

    Return a dict with the info, and error message if the code is invalid
    """

    if is_valid_postcode(postcode):
        return PostCoder().get(postcode)
    return {'error': 'Your postcode is invalid'}
