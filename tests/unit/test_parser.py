from apitool.stdlib import *
import unittest
import sys
from contextlib import contextmanager
from StringIO import StringIO


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
    def setUp(self):
        print(self._testMethodName)
        self.parser = create_parser()

    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output():
                self.parser.parse_args([])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 2)

    def test_with_dash_h(self):
        """
        User passes -h args, should fail with help
        """
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output():
                self.parser.parse_args(['-h'])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 0)

    def test_with_dash_dash_help(self):
        """
        User passes --help args, should succeed with help
        """
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output():
                self.parser.parse_args(['--help'])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 0)

    def test_with_notify(self):
        """
        User passes notify arguments,cat
        """
        args = self.parser.parse_args(['notify'])
        result = notify(args)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()