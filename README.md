# Holidays For The Heroes Hero Description Maker
Author: Kurt Campbell<br>
Date: 20 November 2021
Modified: 30 August 2022

© Copyright Holidays For The Heroes, Kurt Campbell. All rights reserved.

The Hero Description Maker is a Python program that generates hero descriptions from a given csv file or user inputs. A hero description will be used for the hero's picture on the website's [Gallery](https://www.holidaysfortheheroes.org/gallery).

## Option 1 - Generating hero descriptions from a csv file
If you have a csv file filled with the hero's credentials, you can specify the filename of the csv and it will automatically generate all the hero descriptions to be printed to the terminal screen and stored in results.txt.

Your records within the csv file should be as followed:<br>
Name,Gender,Branch,Location,Based,Holiday

Gender field should be "He" or "She" (without double quotations).<br>
Branch should be "Army", "Air Force", "Navy", "Coast Guard", or "Marine" (wihtout double quotations).<br>
If no location or based is specified, please leave them blank (i.e., "Name,Gender,Branch,,,Christmas").<br>
If no holiday is specified, please enter "holidays" (without double quotations) for that field.

## Option 2 - Input hero credentials to generate descriptions
You have the option of entering the hero's credentials by inputting directly within your Python console or terminal. Theinformation you will need is the hero's name, gender, branch, their destination location, base location, and holiday. The required fields are their name, gender, and branch. The destination location, base location, and holiday are optional.

Once you entered the hero's information, the generated sentence will be stored in results.txt.

Input Shortcuts:

Gender<br>
1 - Male<br>
2 - Female

Branch<br>
1 - Army<br>
2 - Air Force<br>
3 - Navy<br>
4 - Coast Guard<br>
5 - Marine

Holidays<br>
holidays - " for the holidays"<br>
