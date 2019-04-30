# TSU-Spring2019-CS456-Thomas2.0
fileName = raw_input('Enter the file name you would like to read ') #This line ask the user what file they would like to open.
try:
    fileHandler = open(fileName)  #This file opens the file that the user enters.
except:
    print 'File cannot be opened:', fileName    #If the files doesnt open then the message will pop up.
    exit()
counts = dict()      #This creates the dictionary for the the words.
for line in fileHandler:    #This loops through the file and finds the words and keep count if them in the dictoinary.
    words = line.split()      #This takes the word and stores it into a variable.
    for word in words:       #If the word is in the dictionary or if it isnt
        if word not in counts:       #Keep count of the added word.
            counts[word] = 1
        else:
            counts[word] += 1       #Keep count of the word if its already stored.
print counts                           #Prints the dictionary.
#To fulfill enhancement: Give the count and length of each word, as well as if it starts with a digit or alpha.
