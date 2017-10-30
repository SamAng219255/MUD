def main(obj,player,layer):
 obj["title"]=input("What is the sign titled?\n")
 obj["text"]=input("What does the sign say?\n")
 obj["name"]="sign:"+obj["title"]
 return obj
def remove(obj,player,layer):
 return