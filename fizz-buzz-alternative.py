#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program prints 1000 to 2000 with 5 of numbers each line


def main():
    # This function prints 1000 to 2000 with 5 of numbers each line
    one = 1

    # Process
    for one in range(1000, 2000 + 1):
        if one % 5 == 0:
            # Output
            print("")
            print(one, "", end="")
        else:
            print(one, "", end="")


if __name__ == "__main__":
    main()
