file = open("MyOutputFile.txt", "w")

stringOut1 = "The quick brown fox \n"
stringOut2 = "jumped over the lazy dog \n"

file.writelines([stringOut1,stringOut2])

file.close()
