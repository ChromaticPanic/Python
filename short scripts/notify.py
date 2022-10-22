import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="send notification via apprise docker")
    parser.add_argument('-m', metavar='--msg', type=str, nargs='?', default="", action='store', help='message')
    parser.add_argument('-t', metavar='--tag', type=str, nargs='?', default="", action='store', help='service tag')

    args = parser.parse_args()
    if args.t and args.m:
        if args.t == "discord":
            os.system("curl -X POST -d \"tag={}&body=@monke {}\" http://localhost:6868/notify/apprise".format(args.t, args.m))
    else:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
