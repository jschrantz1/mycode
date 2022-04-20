#!/usr/bin/env python3
"""Morning Slicing Challenge!"""

challenge= [
        "science", 
        "turbo", 
        ["goggles", "eyes"], 
        "nothing"
        ]

trial= [
        "science", 
        "turbo", 
        {"eyes": "goggles", "goggles": "eyes"}, 
        "nothing"
        ]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name":{"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
    """My eyes! The goggles do nothing!"""

eyes= challenge[2][1]
goggles= challenge[2][0]
nothing= challenge[3]

print(f"My {eyes}! The {goggles} do {nothing}!")

eyes= trial[2]["goggles"]
goggles= trial[2]["eyes"]
nothing= trial[3]

print(f"My {eyes}! The {goggles} do {nothing}!")


eyes= nightmare[0]["user"]["name"]["first"]
goggles= nightmare[0]["kumquat"]
nothing= nightmare[0]["d"]

print(f"My {eyes}! The {goggles} do {nothing}!")

if __name__ == "__main__": # <-- what is this??? we will review later :)
    main()
