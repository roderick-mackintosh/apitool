
import argparse
import sys

def notify(args):
    print("Notify login %s" % args.login)


def schedule(args):
    print("Notify login %s" % args.login)


def create_parser():
    parser = argparse.ArgumentParser(prog='api-tool')

    subparsers = parser.add_subparsers(
        help='sub-command help',
        dest='subparser_name'
    )

    notify_parser = subparsers.add_parser(
        'notify',
        help="Send patching notification"
    )
    notify_parser.add_argument('-l', dest='login', help='Login help')
    notify_parser.set_defaults(func=notify)

    schedule_parser = subparsers.add_parser(
        'schedule',
        help="Schedule patching"
    )
    schedule_parser.add_argument('-l', dest='login', help='Login help')
    schedule_parser.set_defaults(func=schedule)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser