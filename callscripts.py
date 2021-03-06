import importlib
import json

def cos(obj,player,layer):#Call Object Script; calls the script of a given enviroment object
 args=[]#initiate "args"
 for arg in obj["args"]:#iterate through object arguments
  args.append(obj[arg])#add argument value to "args"
 objscr=importlib.import_module("objectScripts."+obj["script"])#import object creation script
 objscr.main(args,player,layer)#call object script with "args"

def ccs(obj,player,layer):#Call Creation Script; creates an enviroment object and calls its creation script
 f=open("objects/"+obj+".data","r")#open object template file
 newobj=json.load(f)#initiate object from template
 f.close()#close object template file
 objscr=importlib.import_module("objectScripts."+newobj["creation"])#import object script
 newobj=objscr.main(newobj,player,layer)#call object script on object
 return newobj#return the created object