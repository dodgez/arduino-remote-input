from argparse import ArgumentParser
from json import load
from pyautogui import keyDown, keyUp, press
from serial import Serial, SerialException
from sys import stderr

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        action='store_true', help="verbose logging")
    parser.add_argument('-p', '--port', nargs='?',
                        default='COM1', help="the serial port to listen on")
    parser.add_argument('-f', '--file', nargs='?',
                        default='example_keys.json', help="the json key mapping file")
    args = parser.parse_args()

    try:
        mappings = load(open(args.file, 'r'))
        if args.verbose:
            print("Loaded key mappings:", mappings)
        with Serial(args.port) as s:
            print("Listening on", args.port)
            while True:
                data = str(s.read(), 'utf-8')
                try:
                    key_info = mappings[data]
                except KeyError:
                    print("No mapping found for key", data, file=stderr)
                    continue

                type = key_info["type"]
                char = key_info["char"]
                if type == "keyDown":
                    keyDown(char)
                elif type == "keyUp":
                    keyUp(char)
                elif type == "press":
                    press(char)

                if args.verbose:
                    print(type, char)
    except SerialException as e:
        print(e, file=stderr)
    except FileNotFoundError as e:
        print(e, file=stderr)
