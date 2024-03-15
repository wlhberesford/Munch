"""
This file takes in a txt that is a copy 
out your commits, and formats the links 
for mid year report

For easy use, download to this file to a 
different folder and use there. 


"""


input_file=""




in_f=open(input_file)
out_f=open("format.txt")


for line in in_f:
    words=line.split(" ")
    if(words.count("commit")==1):
        loc=words.index("commit")
        loc+=1
        in_f.write("https://github.com/wlhberesford/Munch/commit/{}".format(words[loc]))
    else:
        pass
        
        
