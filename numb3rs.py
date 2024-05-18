import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip)
    if match:
        octets = match.groups()
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False


if __name__ == "__main__":
    main()
