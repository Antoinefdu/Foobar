># Braille Translation  
>
>Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic
 standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will
> help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion. 
>
>Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can
 either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander
> Lambda's command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print the bumps onto the
> signs expects the dots in the following order:  
>
>1 4  
>2 5  
>3 6  
>
>So given the plain text word "code", you get the Braille dots:

>11 10 11 10  
>00 01 01 01  
>00 10 00 00  
>
>where 1 represents a bump and 0 represents no bump. Put together, "code" becomes the output string "100100101010100110100010".
>
>Write a function answer(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps
 in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization
> mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and
> use only letters and spaces. 
 

# Reasoning:

This one is pretty straightforward: just create a dictionary for each letter and the corresponding code (see braille_no_import.py).  
So I included a slightly more challenging version : what if we were asked to solve this without typing any of the braille code ourselves?   
For that, we'll need to do a quick webscraping of a Wikipedia page, extract the code, reformat it to make it correspond to the format required in the
 question, and we've got our code (see braille_using_bs4.py).