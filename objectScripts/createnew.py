import json
import importlib

def ccs(obj,player,layer):#Call Creation Script; creates an enviroment object and calls its creation script
 f=open("objects/"+obj+".data","r")#open object template file
 newobj=json.load(f)#initiate object from template
 f.close()#close object template file
 objscr=importlib.import_module(newobj["creation"])#import object script
 newobj=objscr.main(newobj,player,layer)#call object script on object
 return newobj#return the created object

def main(obj,player,layer):
 obj["name"]=input("name:\n")
 obj["description"]=input("description:\n")
 obj["script"]=input("script name:\n")
 if(obj["script"]==""):
  obj["script"]="basic"
 else:
  obj["args"]=input("arguments (comma seperated list):\n").split(",")
  if(obj["args"][0]==""):
   del obj["args"][0]
 obj["creation"]=input("creation script name (leave blank for default):\n")
 if(obj["creation"]==""):
  obj["creation"]="basicreate"
 obj["identifier"]=input("default identifier:\n")
 if(obj["identifier"]!=""):
  obj["identifiers"]=input("identifiers (comma seperated list):\n").split(",")
  if(obj["identifiers"][0]==""):
   del obj["identifiers"][0]
 obj["health"]=int(input("health:\n"))
 while input("Does it have additional data?:\n").lower() in ["y","yes","si","ja"]:
  datnam=input("data name:\n")
  obj[datnam]=input("data value:\n")
 f=open("objects/"+obj["name"]+".data","w")
 json.dump(obj,f)
 f.close()
 return obj
def remove(obj,player,layer):
 return