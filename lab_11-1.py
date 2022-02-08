# RTS 2/8/22

my_files = open("alma_mater.txt", "r")
while True:
     line = my_files.readline()
     if len(line) == 0:
           break
     print (line, end="")
     print(" ")
my_files.close()
