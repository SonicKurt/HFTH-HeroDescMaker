#!/usr/bin/python3

"""
Holidays For The Heroes Hero Desciption Maker

Summary: A program that can take in a csv file or inputs to generate
hero descriptions for each hero in the gallery on the website.

Author: Kurt Campbell
Date: 20 November 2021

© Copyright Holidays For The Heroes, Kurt Campbell
All rights reserved.
"""

import csv

def pick_option():
    print("Please pick an option:")
    print("1 - Generate hero descriptions from a csv file")
    print("2 - Input hero credentials to generate descriptions")
    print("3 - Exit the program")
    return input("Enter your option: ")

def branch_filler(branch):
    if branch == "1" or branch == "Army":
        return "Army Solider"
    elif branch == "2" or branch == "Air Force":
        return "Air Force Airman"
    elif branch == "3" or branch == "Navy":
        return "Navy Sailor"
    elif branch == "4" or branch == "Coast Guard":
        return "Coast Guard Sailor"
    else:
        return "Marine Corps Hero"

def based_filler(based_name):
    if based_name != "":
        return f" based in {based_name}"
    
    return ""

def location_filler(location):
    if location != "":
        return f" to {location}"
    
    return ""
    
def holiday_filler(holiday_name):
    if holiday_name == "" or holiday_name == "holidays":
        return "the holidays"
    
    return holiday_name

results_file = open("results.txt", "a")
another_hero = "Y"

print("Holidays For The Heroes Hero Description Maker")

choice = pick_option()

while choice != "3":
    if choice == "1":
        try:
            filename = input("Enter the file name of your csv: ")
            print()
            csv_file = open(filename)
            heroes_reader = csv.reader(csv_file)
            for hero in heroes_reader:
                hero_name = hero[0]
                gender = hero[1]
                branch = hero[2]
                branch = branch_filler(branch)

                location = hero[3]
                location = location_filler(location)

                based_name = hero[4]
                based_name = based_filler(based_name)

                holiday_name = hero[5]
                holiday_name = holiday_filler(holiday_name)

                hero_desc = f"Meet {hero_name}! {gender} is an {branch}{based_name} and went home{location} for {holiday_name}!\n"
                results_file.write(hero_desc)
                print(hero_desc.strip())
            print(f"\nGenerated all hero desciptions from {filename} and stored in results.txt")
            choice = pick_option()
        except FileNotFoundError:
            print(f"{filename} is not found.")
            choice = pick_option()
    elif choice == "2":
        while (another_hero == "Y"):
            print("Please enter the hero's name, branch, location")
            # Essential inputs for a hero description.
            hero_name = input("Name: ").capitalize()

            gender = input("Gender (Enter 1-Male or 2-Female): ").capitalize()
            if gender == "1":
                gender = "He"
            else:
                gender = "She"

            branch = input("Branch (1-Army, 2-Air Force, 3-Navy," + 
                "4-Coast Guard, 5-Marine): ").capitalize()

            branch = branch_filler(branch)

            location = input("Location: ").capitalize()
            location = location_filler(location)

            based_name = input("Based: ").capitalize()
            based_name = based_filler(based_name)

            holiday_name = input("Holidays: ")
            holiday_name = holiday_filler(holiday_name)
                
            hero_desc = f"Meet {hero_name}! {gender} is an {branch}{based_name} and went home{location} for {holiday_name}!\n"

            print(hero_desc)

            results_file.write(hero_desc)

            another_hero = input("Want to enter another hero (Y/N)? ").upper()
        choice = "3"
    else:
        print(f"\n{choice} is not an option")
        choice = pick_option()