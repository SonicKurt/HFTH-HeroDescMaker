#!/usr/bin/python3

"""
Holidays For The Heroes Hero Description Maker

Summary: A program that can take in a csv file or inputs to generate
hero descriptions for each hero in the gallery on the website.

Author: Kurt Campbell
Date: 20 November 2021
Version: 1.6

Modifications:
    2022-01-04 - Added condition statements within holiday_filler method
    2022-01-06 - Implemented method for how the mission should be printed
    2022-08-23 - Removed the mission sentence since stating the mission in an
                 hero's statement is unnecessary. Therefore, the mission filler
                 method, variables that store the hero's mission
                 number and sentence, and mission count from csv option has been
                 removed.

                 Added space between the Navy and Coast Guard within the branch prompt
                 when user enters the information manually. 

© Copyright Holidays For The Heroes, Kurt Campbell.
All rights reserved.
"""

import csv

def pick_option():
    print("Please pick an option:")
    print("1 - Generate hero descriptions from a csv file.")
    print("2 - Input hero credentials to generate descriptions.")
    print("3 - Exit the program.")
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

def dest_filler(dest):
    if dest != "":
        return f" to {dest}"
    
    return ""
    
def holiday_filler(holiday_name):
    if holiday_name == "holidays":
        return " for the holidays"
    elif holiday_name == "":
        return ""
    else:
        return f" for {holiday_name}"

results_file = open("results.txt", "a")
another_hero = "Y"

print("Holidays For The Heroes Hero Description Maker")

choice = pick_option()

while choice != "3":
    mission_count = 0
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

                dest = hero[3]
                dest = dest_filler(dest)

                based_name = hero[4]
                based_name = based_filler(based_name)

                holiday_name = hero[5]
                holiday_name = holiday_filler(holiday_name)

                hero_desc = f"Meet {hero_name}! {gender} is a {branch}{based_name} and went home{dest}{holiday_name}!"
                results_file.write(hero_desc + "\n")
                # DEBUGGING PURPOSES
                #print(hero_desc.strip())
            print(f"\nGenerated hero desciptions given the information from {filename}.\nThey are stored in results.txt")
            choice = pick_option()
        except FileNotFoundError:
            print(f"{filename} is not found.")
            choice = pick_option()
    elif choice == "2":
        while another_hero == "Y":
            print("Please enter the hero's information.")
            # Essential inputs for a hero description.
            hero_name = input("Name: ")

            gender = input("Gender (Enter 1-Male or 2-Female): ").capitalize()
            if gender == "1":
                gender = "He"
            else:
                gender = "She"
            
            branch = input("Branch (1-Army, 2-Air Force, 3-Navy, " + 
                "4-Coast Guard, 5-Marine): ").capitalize()

            branch = branch_filler(branch)

            dest = input("Destination: ")
            dest = dest_filler(dest)

            based_name = input("Based: ")
            based_name = based_filler(based_name)

            holiday_name = input("Holidays: ")
            holiday_name = holiday_filler(holiday_name)
            
            hero_desc = f"Meet {hero_name}! {gender} is a {branch}{based_name} and went home{dest}{holiday_name}!"

            print(hero_desc)

            results_file.write(hero_desc + "\n")

            print("Created hero description and stored in results.txt")

            another_hero = input("Want to enter another hero (Y/N)? ").upper()
        choice = "3"
    else:
        print(f"\n{choice} is not an option")
        choice = pick_option()
