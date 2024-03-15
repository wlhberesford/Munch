"""
This file takes in a txt that is a copy 
out your commits, and formats the links 
for mid year report

For easy use, download to this file to a 
different folder and use there. 


"""


input_file="git_log.txt"


git_username="wlhberesford"

in_f=open(input_file)
out_f=open("format.txt","w")

commits=[]

for line in in_f:
    words=line.split(" ")
    if(words.count("commit")>=1):
        loc=words.index("commit")
        commits.append("https://github.com/{}/Munch/commit/{}".format(git_username,words[1]).strip())
        commits.append("\n")
    else:
        pass
        
out_f.writelines(commits)

in_f.close()
out_f.close()
