Our original project 3 involved making an HTML document. For project 4, I modified the code of the original
project so that it makes a proper LaTeX document with certain special functions for the in.txt file.

When a line in in.txt begins with a # it is commented out. If a word is put in between percent symbols
such as %hi% and it appears in vars.dat, it will be substituted by its appropriate substitute. 

My python code also supports lists and nested lists by placing < at the beginning of a line,
then the items that want to be inside the list on the next line, and finally it
terminates a list by seeking a > on a line by itself. The < and > are not written to the out.txt file.

The program also supports LaTex. It will take any int or frac and depending on the amount of $ signs 
surrounding the word it will either center it on its own line and center it with 2 dollar signs
or make it into a proper LaTeX formatting such as $\frac {}{}$ with the empty brackets
having something inside, which correspond to a numerator and a denominator. For $$int$$ it turns into $\int_{}^{}$ which has a lowerbound and upperbound.
It will take something like $$$int$$$ and turn it into $$\int_{}^{}$$ on a newline by itself so it can be centered on its own line.
The format must be $$int x y$$ with one space between the lower and the upper bound x,y respectively (similar for frac).

These are all the functions that the python code supports. The code does not support nested
frac or int so it will not handle frac int frac frac. 

Finally, to actually and grade the assigned project, I have provided in.txt files each of which test a specific
part of the program with a similar way that I was tested on my functions for project 3.

The intended output is also provided. If the intended output does not match the input, then the
program has failed. To use the program, type the following command after downloading all text files from Gradescope:

python mainpart.py vars.dat in.txt out.txt

where mainpart.py is the longest part of the code, vars.dat is a dictionary that you can make, and in.txt is provided (but might need to be renamed).
out.txt is made by the program, so it is not provided, but the intended out.txt will be given for confirmation that the
program works and it will be numbered.
 
This program demonstrates knowledge of regex, the time date module, input and output files, list appending and popping
as well as functions and dictionaries. 

I got the standard Latex heading from:
https://latexbase.com/d/aafb020b-28a3-4ea1-8e39-8a239f0bdabf
and the out.txt file can be copied and pasted there to see what the output will
look like on a Latex paper. 