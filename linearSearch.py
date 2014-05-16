testString = ""
newString = ""
searchChar = ""
replaceChar = ""


while testString == "": #Until they enter a string, ask for one
    testString = input("Please enter some text to search : ")

while len(searchChar) != 1: #Until they enter a character, ask for one
    searchChar = input("Enter a character to replace for :")

while len(replaceChar) != 1: #Until they enter a character, ask for one
    replaceChar = input("Enter a character to replace {0} with:".format(searchChar))

for x in testString: #Loop through testString
    if x == searchChar: #If the character is the character to be replaced
        newString += replaceChar #Add the replacement character to the list
    else:
        newString += x #Else add the character

print ("The new string is {0}".format(newString)) #Show the user the string
