import json
import random

def main(obj,player,layer):
 obj["caveid"]=random.randint(1,2**16)
 obj["name"]=input("What should it be called?\n")
 obj["description"]=input("What should the description be?\n")
 obj["target"]=int(input("Which room should it go to?\n"))
 obj["txt"]=input("What should it say when in use?\n")
 f=open("objects/cave.data","r")
 newobj=json.load(f)
 f.close()
 newobj["name"]=obj["name"]
 newobj["target"]=player["room"]
 newobj["description"]=obj["description"]
 newobj["txt"]=obj["txt"]
 newobj["caveid"]=obj["caveid"]
 layer[obj["target"]]["contents"].append(newobj)
 return obj

def remove(obj,player,layer):
 for thing in layer[obj["target"]]["contents"]:
  if "caveid" in thing:
   if thing["caveid"]==obj["caveid"]:
   	del thing
   	break
