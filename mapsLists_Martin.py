#!/usr/bin/python

#  Name: Michael Martin
#  Date: 2.1.2018
#  Assignment: Lists and Maps

##In this assignment you will use maps and list at an introductory level.  You are to do the following:
##
##Create a list instance ( you can initialize or add values to it).  - 2 points
##
##Print out the list of elements from the list instance.    - 2 points
##
##Create a map instance ( you can initialize or add values to it ). - 2 points
##
##Print out each key value pair from the map - 4 points
##
##The assignment is available at the github classroom link:  https://classroom.github.com/a/dL3L1Ily

#######

word_list = []

word_list = ['every', 'good', 'boy','does', 'fine', 'FACE']

print(word_list)

for index in range(len(word_list)):
    print("Music Treble Cleft (lines):  ", word_list[index])
    
word_map = { 1 : 'know', 2 : 'show', 3 : 'do'}

print(word_map)

for index in word_map:
    wdMp = word_map[index]
    print(wdMp)


    
    





