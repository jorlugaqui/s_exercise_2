# -*- coding: utf-8 -*-

""" Unit tests for check_postcodes """

import unittest
from check_postcodes import is_valid_postcode, get_info


class TestCheckPostCodesModule(unittest.TestCase):

    def test_is_valid_postcode(self):
        """Test is_valid_postcode."""

        self.assertTrue(is_valid_postcode('W1A 2XX'))
        self.assertFalse(is_valid_postcode('W1A 2X!'))  # Invalid
        self.assertTrue(is_valid_postcode('SW1A 1AA'))

        self.assertTrue(is_valid_postcode('M1 1AE'))
        self.assertTrue(is_valid_postcode('B33 8TH'))
        self.assertTrue(is_valid_postcode('CR2 6XH'))
        self.assertTrue(is_valid_postcode('DN55 1PT'))
        self.assertTrue(is_valid_postcode('BFPO 11'))
        self.assertTrue(is_valid_postcode('AA1 1AA'))  # True in format

        self.assertFalse(is_valid_postcode('W1A  2X!'))  # Invalid

    def test_get_info(self):
        """Test get_info."""

        # TODO: To mock get_info function should be considered since the
        # library selected is a wrapper of a web service. Sometimes it takes
        # long time (<=2s), for users it is kind of acceptable but not for
        # tests.
        res = get_info('M1 1AE')
        self.assertTrue('administrative' in res)
        self.assertTrue('geo' in res)

        res = get_info('M1  1AE')  # Notice the extra space
        self.assertTrue('error' in res)

        res = get_info('AA1 1AA')  # Valid in format, but not data
        self.assertIsNone(res)


if __name__ == "__main__":
    unittest.main()
