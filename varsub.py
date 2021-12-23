""" MCS 260 Fall 2020 Project 4
Mustafa Nawaz
# Declaration: I, Mustafa Nawaz, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus."""


"""Mustafa Nawaz's varsub which substitutes words and latexifies math code"""
import re

def substitute(vars,s):
    """This function replaces words in percent signs in our in.txt file"""
    #get rid of things in dollar signs and replace with their corresponding key
    for key in vars.keys():
        s = s.replace("%"+key+"%", vars[key])
    return s

def latexslash(s):
    """This deals with latex that is surrounded by 2 dollar signs including fractions and integrals"""
    #get rid of things surrounded by 2 dollar signs and replace them with a slash and dollar signs

    if "frac" or "int" in s:
        fractionname=r"\$\$frac ([a-z0-9A-Z]+) ([a-z0-9A-Z ]+)\$\$"
        intname=r"\$\$int ([a-z0-9A-Z]+) ([a-z0-9A-Z ]+)\$\$"

        for m in re.finditer(fractionname, s):
            numerator="{"+m.group(1)+"}"
            denominator="{"+m.group(2)+"}"
            s=s.replace(m.group(), "$\\frac"+numerator+denominator+"$")

        for m in re.finditer(intname, s):
            lowerbound="{"+m.group(1)+"}"
            upperbound="^{"+m.group(2)+"}"
            s=s.replace(m.group(), "$\\int_"+lowerbound+upperbound+"$")
            

    replacement=r"\$\$([A-Za-z]+)\$\$"
    for m in re.finditer(replacement, s):

        s = s.replace(m.group(), "$"+"\\"+m.group(1)+"$")
    return s

def centeredlatexslash(s):
    """This deals with latex that is surrounded by 3 dollar signs including fractions and integrals"""
    #look for a string fraction and split into 2 groups
    if "frac" in s:
        fractionname=r"\$\$\$frac ([a-z0-9A-Z]+) ([a-z0-9A-Z ]+)\$\$\$"
        for m in re.finditer(fractionname, s): #when you find the fraction
            numerator="{"+m.group(1)+"}"       #split it into a numerator and a denominator
            denominator="{"+m.group(2)+"}"
            s=s.replace(m.group(), "\n$$\\frac"+numerator+denominator+"$$\n") #and format it in a latex way
            
    #look for a string integral and split it into lower and upper bound
    if "int" in s:
        intname=r"\$\$\$int ([a-z0-9A-Z]+) ([a-z0-9A-Z ]+)\$\$\$" 
        for m in re.finditer(intname, s):
            lowerbound="{"+m.group(1)+"}"
            upperbound="^{"+m.group(2)+"}"
            s=s.replace(m.group(), "\n$$\\int_"+lowerbound+upperbound+"$$\n")   #then format it in a latex way   
            

    replacement=r"\$\$\$([A-Za-z]+)\$\$\$"
    for m in re.finditer(replacement, s):

        s = s.replace(m.group(), "\n$$"+"\\"+m.group(1)+"$$\n")
    return s

    return s

