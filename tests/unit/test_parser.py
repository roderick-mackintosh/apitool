from apitool.stdlib import *
import unittest
import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err


class CommandLineTestCase(unittest.TestCase):
    """
    CommandLine TestCase sets up a CLI parser
    """

    def test_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output():
                ApiToolParser([])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 1)


if __name__ == '__main__':
    unittest.main()
