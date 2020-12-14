#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program uses a while loop


def main():

    # input
    positive_integer = print("  Enter how many times to repeat ")
    positive_string = input("Enter Here plz : ")
    loop_counter = 0

    # process & output
    try:
        positive_integer = int(positive_string)
        while loop_counter < positive_integer:
            print("{0} time through loop.".format(loop_counter))
            loop_counter = loop_counter + 1
    except Exception:
        print("This was an invalid number ")


if __name__ == "__main__":
    main()
