writeMe = 'Example Text'

saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()  #closing a file is important otherwise will face an error
