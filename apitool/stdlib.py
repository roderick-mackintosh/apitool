
import argparse
import sys


class ApiToolParser(object):
    """ apitool class """

    def __init__(self, args):
        """
        Initialiser function
        :param argv: command line argument
        """
        self.parser = argparse.ArgumentParser(prog='api-tool')

        subparsers = self.parser.add_subparsers(
            help='sub-command help',
            dest='subparser_name'
        )

        self.notify_parser = subparsers.add_parser(
            'notify',
            help="Send notification"
        )
        self.notify_parser.add_argument('-l', dest='login', help='Login help')
        self.notify_parser.set_defaults(func=self.notify)

        self.push_parser = subparsers.add_parser(
            'push',
            help="push notification"
        )
        self.push_parser.add_argument('-l', dest='login', help='Login help')
        self.push_parser.set_defaults(func=self.push)

        if len(sys.argv) == 1:
            self.parser.print_help(sys.stderr)
            sys.exit(1)

        self._args = self.parser.parse_args()
        self._args.func(self._args)

    def notify(self, args):
        """
        Notify function
        :param args: command line arguments
        :return: tba
        """
        if args.login:
            print("Notify login %s" % args.login)
        else:
            self.notify_parser.print_help(sys.stderr)
            sys.exit(1)

    def push(self, args):
        """
        Push function
        :param args: command line arguments
        :return: tba
        """
        if args.login:
            print("Push login %s" % args.login)
        else:
            self.push_parser.print_help(sys.stderr)
            sys.exit(1)
