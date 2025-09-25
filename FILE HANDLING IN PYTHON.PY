# # writing data to afile:-
# f=open("data.txt","w")
# f.write("Hello,python!/n")
# f.close()

# #write line():-
# f=open ("data.txt","w")
# f.writelines(["line 1/n","line 2/n","line 3/n"])
# f.close()

# # Reading data from a file
# # Read():-
# f=open("data.txt","r")
# print(f.read())
# print(f.read(5))
# f.close()

# #Readline():-
# f=open("data.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()
 
# #Readlines():- 
# f=open("data.txt","r")
# lines=f.readlines()
# print(lines)
# f.close()

# #Random access file operations
# # tell (seek)():-
# f=open("data.txt","r")
# print(f.read(5))
# print("pointer at:",f.tell())
# f.seek(0)
# print(f.read(5))
# f.close()

