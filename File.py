myfile = open('myfile.txt')
s = myfile.read()
print(s)

#seek set to 0 to put cursor at start of file again
myfile.seek(0)
s2 = myfile.readlines()
print(s2)

#close file after opening to avoid bullshit later using computer
myfile.close()

#use this to not worry about closing the file
with open('myfile.txt', mode='r+') as file1:
    content1 = file1.readlines()
    print(content1)

with open('myfile.txt', mode='a') as f:
    f.write('\nFIVE ON FIFTH')
