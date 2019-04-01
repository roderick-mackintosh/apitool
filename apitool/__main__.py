"""    Tool to perform actions in cli-tools    """

from apitool import stdlib


def main():
    """    Main function    """
    parser = stdlib.create_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()