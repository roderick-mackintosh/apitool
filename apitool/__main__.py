"""    Tool to perform actions in cli-tools    """

from apitool import stdlib
import sys


def main():
    """
    Main function
    :return: nothing
    """
    stdlib.ApiToolParser(sys.argv)


if __name__ == '__main__':
    main()
