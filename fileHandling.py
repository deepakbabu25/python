#f1=open("file1.txt","x")#creates a files
#f1=open("file1.txt","r")#opens a file
#d=f1.read()#reads the file
#print(d)
#f1=open("file1.txt","w")#opens a file
#f1.write("welcome topes")#overwrites the file
#print(f1.read())#gives erroe as we are trying to read a file which is opened in write mode
#f1=open("file1.txt","r+")#is used when the process is first read then write
#print(f1.read())
#f1.write("welcome to python")
#f1=open("file1.txt","r+")
#print(f1.tell())
#f1.write("hi")
#print(f1.tell())
#print(f1.read())
#print(f1.tell())
#f1=open("file1.txt","w+")
#print(f1.tell())
#f1.write("welcome to python")
#print(f1.tell())
#f1.write("hi")
#print(f1.tell())
#f1.seek(0)
#print(f1.tell())
#data=f1.read()
#print(f1.tell())
#print(data)


#f1=open("file1.txt","a")
#f1.write("student")
#print(f1.read()) errror

f1=open("file1.txt","a+")
print(f1.tell())
print(f1.read())