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

print("Test Palindrome #1: ", isPalindrome("Kristofferson", "nosreffotsirK"))
print("Test Palindrome #2: ", isPalindrome("peter", "parker"))


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

print("Test Anagram #1: ",isAnagram("state", "taste"))
print("Test Anagram #2: ", isAnagram("payton", "taycan"))