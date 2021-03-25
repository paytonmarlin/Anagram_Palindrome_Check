# Palindrome and Anagrams - Checking and Comparing Two Strings

## The What?
This is a program in python that checks if two strings are either a palindrome (same way spelled forwards and backwards) or an anagram (words with the same letters but arranged differently).

I used two different functions to split up the program into two separate parts.

## The Why?
This is a challenge in IT 4320 - Software Engineering to see if we can utilize and find out the 'Big-O' of a certain solution of code.

## The Who?
This is created by Payton Marlin with the help of some googling for Python syntax.

---
### **The Palindome Function**

Below is the code that I have implemented in my python file for the palindrome function...

``` python
# Define a function that takes two parameters for Palindrome Check
#This has a Big-O running time of O(n)
def isPalindrome(string1, string2):
    leftIdx = 0
    rightIdx = len(string2) - 1
#Compare the two strings, one character at a time from the left and right
    while leftIdx < rightIdx:
#If the two characters are not the same, 
        if string1[leftIdx] != string2[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
```
In the above code, I check the indexes of both the strings. The first string that is passed, I start at the beginning. In the second string, I start at the last character (the length -1 since indexes start at zero). Then, I just check each character to make sure it matches.

**This solution has a Big-O of O(n)** since the solution is linear and depends on how long the strings are. It should only 'loop' through once to check each character.

---
### **The Anagram Function**
Below is the code that I have implemented for the anagram function in the same python file as above...
``` python
#Define an anagram function
#This has a Big-O complexity of O(n)
def isAnagram(string1, string2):
    string1_dict = {}
    string2_dict = {}
    count1 = 1
    count2 = 1
#iterate over a character in each word
    for char in string1:
#if character is already found (inserted in dictionary), add 1 to the value
        if char in string1_dict:
            string1_dict[char] = string1_dict.get(char, 0) + 1
#if character is NOT in dictionary, add it as a key with a value of 1
        else:
            string1_dict.update({char: count1})
#repeat for the second string
    for char in string2:
        if char in string2_dict:
            string2_dict[char] = string2_dict.get(char, 0) + 1
        else:
            string2_dict.update({char: count1})
#if dictionaries are equal, return True
    if string1_dict == string2_dict:
#else return False
        return True
    else:
        return False
```
This function was a little longer than the palindrom function. I take two empty dictionaries, one for each string passed from the function call, and put each character as a key and its count as the value. Then I simply compare the dictionary's key and values and, if they match, it returns true. 

**This anagram function has a Big-O of O(2n) or O(n)** because, while it has two serperate for loops, they act in unison together instead of being nested. This allows for less iterations and less time for the program to take. 

---
## The How?
Assuming you have downloaded the python files, you can either open it up in IDLE and run it using F5 or navigate to your terminal/command line and run it through there. This tutorial will walk through how to run it through the powershell (which acts more as a linux environment than command line on Windows.)

**Step 1:** Navigate to the location of the folder or file in your terminal/powershell. If you don't know the terminal command line there are many cheatsheets online such as [this one](https://www.comparitech.com/net-admin/powershell-cheat-sheet/).

**Step 2:** Assuming you have Python installed (if not, look [here](https://www.python.org/downloads/)) on your machine you can use the command 
```
python [filename]
```
to run the file.

![Running Python](/assets/Run_python.gif)

**Step 3:** You are done! If you want to change the strings inputted, you can navigate to the python file and change
```python
print("Test Palindrome #1: ", isPalindrome("Kristofferson", "nosreffotsirK"))
print("Test Palindrome #2: ", isPalindrome("peter", "parker"))

...

print("Test Anagram #1: ",isAnagram("state", "taste"))
print("Test Anagram #2: ", isAnagram("payton", "taycan"))
```
To any two strings that you want. Play around and have fun!!
