import collections

"""CareerCup Questions
    Function to check if a word has guplicate letters"""
def hasDuplicateLetters(word):
    letterArray = []
    for letter in word:
        if letter in letterArray:
            return True
        letterArray.append(letter)
    return False

"""Function to reverse a string"""
def reverseString(string):
    mid = len(string)//2 - 1
    reversedString = ""
    leftCounter = mid
    rightCounter = mid + 1
    if len(string)%2  == 1:
        mid = mid + 1
        rightCounter = rightCounter + 1
    while leftCounter >= 0:
        reversedString = reversedString + string[leftCounter]
        reversedString = string[rightCounter] + reversedString
        leftCounter = leftCounter - 1
        rightCounter = rightCounter + 1
    return reversedString

"""Verifies if a string is a permutation of another"""
def verifyPermutation(stringA, stringB):
    stringA = ''.join(sorted(stringA))
    stringB = ''.join(sorted(stringB))
    return collections.Counter(stringA) == collections.Counter(stringB)

"""Replaces stringA with stringB"""
def replaceSpaces(string):
    charArray = []
    charArray.extend(string)
    for char in charArray:
        if char == ' ':
            index = charArray.index(char)
            charArray[index] = '%'
            charArray.insert(index + 1, '2')
            charArray.insert(index + 2, '0')
    return ''.join(charArray)

"""Compresses  a string by replacing the repeated characters with count"""
def compressString(string):
    charCount = 0
    initChar = ''
    compressedString = ""
    for char in string:
        if charCount == 0:
            initChar = char
            compressedString = char
        if char == initChar:
            charCount = charCount+1
        else:
                compressedString = compressedString + str(charCount) + char
                initChar = char
                charCount = 1
    if charCount > 1:
        compressedString = compressedString + str(charCount)
    return compressedString

def execute():
    print("Anu " + str(hasDuplicateLetters("Anu")))
    print("Ananthu" + str(hasDuplicateLetters("Ananthu")))
    print("A mouse with a jam is reversed as " + reverseString("A mouse with a jam"))
    print("Dasa is a permutation of asaDa " + str(verifyPermutation("Dasa", "asaDa")))
    print("HTML Encoded - Mr. John Smith" + replaceSpaces("Mr. John Smith"))
    print("aaabbbcccccddeeeeeeggg is compressed as " + compressString("aaabbbcccccddeeeeeeggg"))
        
        
    


