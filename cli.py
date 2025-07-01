#!/usr/bin/env python3

import requests
import sys


def main():
    # location = sys.argv[1] if len(sys.argv) > 1 else 'Bucuresti'
    location = "Bucuresti"
    if len(sys.argv) > 1:
        location = sys.argv[1]
    url = f"https://wttr.in/{location}"
    response = requests.get(url)
    print(response.text)


if __name__ == "__main__":
    main()
