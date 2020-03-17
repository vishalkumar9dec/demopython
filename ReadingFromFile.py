appendMe = 'Appending Text'

saveFile = open('exampleWrite.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()
