import importlib
import json
import utility

actions=[
 {"name":"activate","arguments":[{"required":True,"type":"variable","values":["room object","inventory item"]},{"required":False,"type":"variable","values":["inventory item"]}],"synonyms":["use","pick","unlock","lock","walk through","open","activate"]},
 {"name":"look","arguments":[{"required":False,"type":"variable","values":["room object","inventory item"]}],"synonyms":["look","walk * to","run * to","search","observe","go * to"]},
 {"name":"attack","arguments":[{"required":True,"type":"variable","values":["room object"]}],"synonyms":["hit","punch","attack","whack"]},
 {"name":"move","arguments":[{"required":True,"type":"string","values":[("north",["north","northern","up","top"]),("south",["south","southern","lower","bottom"]),("east",["east","eastern","right"]),("south",["west","western","left","sinister"])]}],"synonyms":["move","go","walk","run"]},
 {"name":"create","arguments":[{"required":True,"type":"variable","values":["non object"]}],"synonyms":["create","build","add"]},
 {"name":"edit","arguments":[],"synonyms":["edit","editroom"]},
 {"name":"remove","arguments":[{"required":True,"type":"variable","values":["enviroment object"]}],"synonyms":["destroy","remove","delete"]},
 {"name":"pickup","arguments":[{"required":True,"type":"variable","values":["enviroment item"]}],"synonyms":["pickup","take","pick up"]},
 {"name":"drop","arguments":[{"required":True,"type":"variable","values":["inventory item"]}],"synonyms":["drop","let go"]}
]
actionnames={}
actionids=[]
actionidspair=[]
def bar():#build action reverse search; allows for search action by synonym
 idtuple=[]
 tempids=[]
 tempidspair=[]
 for act in actions:
  for syn in act["synonyms"]:
   tempids.append(syn)
   tempidspair.append(act["name"])
   idtuple.append((len(syn),len(idtuple)))
 idtuple.sort()
 idtuple.reverse()
 for leng,index in idtuple:
  actionids.append(tempids[index])
  actionidspair.append(tempidspair[index])
bar()
def bar2():#build second action reverse search; allows for search index by name
 for i in range(len(actions)):
  actionnames[actions[i]["name"]]=i
bar2()

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

def runworld(player,layer,request):#directly called by client; processes world interaction #WIP; should check action list for the given action and execute code accordingly. it should then process the passive actions of the other objects in the room.
 playing=True
 if player["room"]>=0:
  if request["action"]=="activate":
   postar=[]
   tar={}
   obj,ident=request["arguments"][0]
   for thing in layer[player["room"]]["contents"]:
    if thing["name"]==obj:
     postar.append(thing)
   if len(postar)<1:
    print("I'm sorry. I didn't understand that.")
   elif len(postar)==1:
    tar=postar[0]
   else:
    for thing in postar:
     if(thing["identifier"]==ident):
      tar=thing
   cos(tar,player,layer)
  elif request["action"]=="look":
   obj,ident=request["arguments"][0]
   if(obj==""):
    print(layer[player["room"]]["look"])
   else:
    postar=[]
    tar={}
    obj,ident=request["arguments"][0]
    for thing in layer[player["room"]]["contents"]:
     if thing["name"]==obj:
      postar.append(thing)
    if len(postar)<1:
     print("I'm sorry. I didn't understand that.")
    elif len(postar)==1:
     tar=postar[0]
    else:
     for thing in postar:
      if(thing["identifier"]=="ident"):
       tar=thing
    print(tar["description"])
  elif request["action"]=="attack":
   postar=[]
   tar={}
   obj,ident=request["arguments"][0]
   for thing in layer[player["room"]]["contents"]:
    if thing["name"]==obj:
     postar.append(thing)
   if len(postar)<1:
    print("I'm sorry. I didn't understand that.")
   elif len(postar)==1:
    tar=postar[0]
   else:
    for thing in postar:
     if(thing["identifier"]=="ident"):
      tar=thing
   tar["health"]-=player["attack"]
  elif request["action"]=="move":
   obj,ident=request["arguments"][0]
   newrequest={"action":"activate","arguments":[("door",obj)]}
   runworld(player,layer,newrequest)
  elif request["action"]=="stop":
   playing=False
  elif request["action"]=="create":
   arg,ident=request["arguments"][0]
   layer[player["room"]]["contents"].append(ccs(arg,player,layer))
  elif request["action"]=="edit":
   obj,ident=request["arguments"][0]
   if(obj==""):
    desc=input("What would you like as the new room description? (leave blank to not change):\n")
    if desc!="":
     layer[player["room"]]["description"]=desc
    desc=input("What would you like as the new room search description? (leave blank to not change):\n")
    if desc!="":
     layer[player["room"]]["look"]=desc
   else:
    postar=[]
    tar={}
    for thing in layer[player["room"]]["contents"]:
     if thing["name"]==obj:
      postar.append(thing)
    if len(postar)<1:
     print("I'm sorry. I didn't understand that.")
    elif len(postar)==1:
     tar=postar[0]
    else:
     for thing in postar:
      if(thing["identifier"]=="ident"):
       tar=thing
    desc=input("What you like tike to change the "+tar["name"]+"'s name to? (leave blank to not change):\n")
    if desc!="":
     tar["name"]=desc
    desc=input("What would you like as the new description? (leave blank to not change):\n")
    if desc!="":
     tar["description"]=desc
  elif request["action"]=="remove":
   postar=[]
   tar={}
   obj,ident=request["arguments"][0]
   for i in range(len(layer[player["room"]]["contents"])):
    if layer[player["room"]]["contents"][i]["name"]==obj:
     postar.append(i)
   if len(postar)<1:
    print("I'm sorry. I didn't understand that.")
   elif len(postar)==1:
    tar=postar[0]
   else:
    for i in postar:
     if(layer[player["room"]]["contents"][i]["identifier"]==ident):
      tar=i
   objscr=importlib.import_module("objectScripts."+layer[player["room"]]["contents"][tar]["creation"])
   objscr.remove(layer[player["room"]]["contents"][tar],player,layer)
   del layer[player["room"]]["contents"][tar]
  #elif request["action"]=="pickup":
  #elif request["action"]=="drop":
 else:
  player["room"]=0
 return player,layer,playing

def takeInput(spoken):#directly called by client; parses player input #WIP
 
# words=spoken.split(" ")
# pact=[]
# parg=[]
# for word in words:
#  if word in actionids:
#   action=actionidspair[actionids.index(word)]
#   for argword in words:
#    if argword in 
# request={"action":"activate","arguments":[("door","north")]}#sample ouput; format:{"action":"action identifier","arguments":[alistofarguments,("argument","identifier"),...]}
 words=spoken.split(" ")
 if(len(words)>=3):
  request={"action":words[0],"arguments":[(words[1],words[2])]}
 elif(len(words)==2):
  request={"action":words[0],"arguments":[(words[1],"")]}
 elif(len(words)==1):
  request={"action":words[0],"arguments":[("","")]}
 
 return request

def outputText(player,layer):#directly called by client; generates output text
 
 if(player["room"]>=0):
  textblock=layer[player["room"]]["description"].split("&",1)
  textblock.insert(1,utility.mtlists(layer[player["room"]]["contents"]))
  txt=""
  for thing in textblock:
   txt+=thing
 else:
  print("You appear to left the map...\nYou will be returned to the center of the map.")

 return txt
