# Holidays For The Heroes Hero Description Maker
Author: Kurt Campbell
Date: 20 November 2021

© Copyright Holidays For The Heroes, Kurt Campbell. All rights reserved.

The Hero Description Maker is a Python program that generates hero descriptions from a given csv file or user inputs. A hero description will be used for the hero's picture on the [Gallery page](https://www.holidaysfortheheroes.org/gallery).

## Option 1 - Generating hero descriptions from a csv file
If you have a csv file filled with the hero's credentials, you can specify the filename of the csv and it will automatically generate all the hero descriptions to be printed to the terminal screen and stored in results.txt.

Your records within the csv file should be as followed:
Name,Gender,Branch,Location,Based,Holiday

Gender field should be "He" or "She" (without double quotations).
Branch should be "Army", "Air Force", "Navy", "Coast Guard", "Marine" (wihtout double quotations).
If no location or based is specified, please leave them blank (i.e., Name,Gender,Branch,,,Christmas).
If no holiday is specified, please enter "holidays" (without double quotations) for that field.

## Option 2 - Input hero credentials to generate descriptions
You have the option of entering the hero's credentials by inputting directly within your Python console or terminal.

Input Shortcuts:
Gender
1 - Male
2 - Female

Branch
1 - Army
2 - Air Force
3 - Navy
4 - Coast Guard
5 - Marine