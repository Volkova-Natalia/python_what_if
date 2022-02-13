import unittest
import doctest

import wi_dict
import wi_hash


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(wi_dict))
    tests.addTests(doctest.DocTestSuite(wi_hash))
    return tests


if __name__ == '__main__':
    unittest.main()
