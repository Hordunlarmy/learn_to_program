try:
    myFile = open("mydata3.txt")

except FileNotFoundError:
    print("File is not found")

else:
    print(myFile.read())
    myFile.close()

finally:
    print("I always execute")
