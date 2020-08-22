import os
import cv2
import getpass

user = getpass.getuser()

path = "/home/" + user + "/다운로드/"

file = open("document/list.txt", 'w')
file.write("filename,label\n")

for d1 in os.listdir("/home/" + user + "/다운로드/"):
    r1 = path + d1
    
    if d1 == "음식물쓰레기":
        num = 0
    else:
        num = 1
        
    for d2 in os.listdir("/home/" + user + "/다운로드/" + d1):
        r2 = r1 + '/' + d2
        
        for d3 in os.listdir("/home/" + user + "/다운로드/" + d1 + '/' + d2):
            r3 = r2 + '/' + d3
            file.write(r3 + "," + str(num) + "\n")

file.close()
