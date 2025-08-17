#!/usr/bin/env python3
"""Weather CLI"""

import sys
import requests

def main():
    """Main function of the Weather CLI"""
    # location = sys.argv[1] if len(sys.argv) > 1 else 'Bucuresti'
    location = "Bucuresti"
    if len(sys.argv) > 1:
        location = sys.argv[1]
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=60)
    print(response.text)


if __name__ == "__main__":
    main()
