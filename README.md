# TSU-Spring2019-CS456-Thomas2.0
fileName = raw_input('Enter the file name you would like to read ')
try:
    fileHandler = open(fileName)
except:
    print 'File cannot be opened:', fileName
    exit()
counts = dict()
for line in fileHandler:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts
