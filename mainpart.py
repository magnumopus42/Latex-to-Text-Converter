"""Text to LaTeX converter supporting comments, lists, varsub, and basic centered and noncentered latex code"""
# MCS 260 Fall 2020 Project 4
# Mustafa Nawaz
# Declaration: I, Mustafa Nawaz, am the sole author of this code , which
# was developed in accordance with the rules in the course syllabus.

#import the various things we need
import sys
import varsub
import os
from datetime import date

#An error message if the inputs are not properly entered
if len(sys.argv) != 4:
    print("Usage: {} INFILE OUTFILE".format(sys.argv[0]))
    print("The text file INFILE is then converted to an Latex file OUTFILE.")
    sys.exit()

#assigning values
varfn = sys.argv[1]
infn = sys.argv[2]
outfn = sys.argv[3]

# open input and output files
fin = open(infn,"r")
fout = open(outfn,"w")
fvar = open(varfn, "r")

#a dictionary for vars.dat
varsdictionary={}

#read vars.dat, remove the = sign, and add the first word for each
#line as a key, and the second word as a value

for line in fvar:
    key, values = line.strip().split("=")
    varsdictionary[key] = values

# print header; copied from latexbase.com for standard Latex heading
fout.write("\\documentclass[12pt]{article}\n")
fout.write("\\usepackage{amsmath}\n")
fout.write("\\usepackage{graphicx}\n")
fout.write("\\usepackage{hyperref}\n")
fout.write("\\title{Insert your title}\n")
fout.write("\\author{Insert your name}\n")
today= date.today()
fout.write("\\date{"+ str (today)+"}\n")
fout.write("\\begin{document}\n")
fout.write("\\maketitle (enter title)\n")

opentags = []  # Stack used for lists inside document
for line in fin:
    #substitute everything at the beginning
    line=varsub.substitute(varsdictionary, line)
    line=varsub.centeredlatexslash(line)
    line=varsub.latexslash(line)

    isblank = not bool(line.strip()) #remove whitespace

    if not isblank:   
        #get rid of comments
        if line[0]=="#":
            continue
        
        #if we see a <, we start a list
        if line[0]=="<":
            fout.write("\\begin{itemize}\n")
            opentags.append("itemize")
            #if we see the < we must not include it in the out.txt
            if opentags and line.startswith("<"):
                continue
        #if we see the >, we comment it out and end the list
        elif line[0]==">":
            fout.write("\\end{itemize}\n")
            opentags.pop()
            if line.startswith(">"):
                continue
        #after we make a list, we will have newlines so skip those
        if opentags and line[0]!=" ":
            fout.write("\\item "+line) #but write the lines that are not empty

        elif not opentags:
            fout.write(line)

# done reading from input file
fin.close()
#print the end tag for the document and close it
fout.write("\n\end{document}")
fout.close()