import importlib
import json
from utility import *
from callscripts import *
from os import listdir

actions=[
 {"name":"activate","arguments":[{"required":True,"type":"variable","values":["enviroment object","inventory item"]},{"required":False,"type":"variable","values":["inventory item"]}],"synonyms":["use","unlock","lock","walk_through","go_through","open","activate","enter","check","touch"]},
 {"name":"look","arguments":[{"required":True,"type":"variable","values":["enviroment object","inventory item"]}],"synonyms":["look","walk_to","run_to","search","observe","go_to"]},
 {"name":"attack","arguments":[{"required":True,"type":"variable","values":["enviroment object"]}],"synonyms":["hit","punch","attack","whack","kill"]},
 {"name":"move","arguments":[{"required":True,"type":"string","values":[("north",["north","northern","up","top"]),("south",["south","southern","lower","bottom"]),("east",["east","eastern","right"]),("south",["west","western","left","sinister"])]}],"synonyms":["move","go","walk","run"]},
 {"name":"create","arguments":[{"required":True,"type":"variable","values":["non object"]}],"synonyms":["create","build","add"]},
 {"name":"edit","arguments":[{"required":True,"type":"variable","values":["enviroment object","inventory item"]}],"synonyms":["edit","edit","change","modify","fix"]},
 {"name":"reset","arguments":[{"required":True,"type":"variable","values":["enviroment object"]}],"synonyms":["reset"]},
 {"name":"remove","arguments":[{"required":True,"type":"variable","values":["enviroment object"]}],"synonyms":["destroy","remove","delete"]},
 {"name":"pickup","arguments":[{"required":True,"type":"variable","values":["enviroment item"]}],"synonyms":["pickup","take","pick_up"]},
 {"name":"drop","arguments":[{"required":True,"type":"variable","values":["inventory item"]}],"synonyms":["drop","let_go"]},
 {"name":"stop","arguments":[],"synonyms":["stop","end","leave","suicide"]},
 {"name":"here","arguments":[],"synonyms":["here","where"]}
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

def runworld(player,layer,request):#directly called by client; processes world interaction
 playing=True
 if player["room"]>=0:
  actscr=importlib.import_module("actionscripts."+request["action"])
  playing=actscr.main(player,layer,request,playing)
  for thing in layer[player["room"]]["contents"]:
   if "passive" in thing:
    args=[]
    for arg in thing["passargs"]:
     args.append(thing[arg])
    objscr=importlib.import_module("objectScripts."+thing["passive"])
    objscr.main(args,player,layer)
 else:
  player["room"]=0
 return player,layer,playing

def takeInput(player,layer):#directly called by client; parses player input
# request={"action":"activate","arguments":[("door","north")]}#sample ouput; format:{"action":"action identifier","arguments":[alistofarguments,("argument","identifier"),...]}
 request={}
 found=False
 while not found:
  spoken=input("")
  words=stripstr(spoken).split(" ")
  for word in words:
   if word in actionids:
    action=actions[actionnames[actionidspair[actionids.index(word)]]]
    found=True
    break
  else:
   print("Your input was not understood.")
   found=False
 if found:
  request={}
  request["action"]=action["name"]
  request["arguments"]=[None]*len(action["arguments"])
  argList=[]
  for i in range(len(action["arguments"])):
   arg=action["arguments"][i]
   if arg["type"]=="string":
    data=""
    for thing,syn in arg["values"]:
     for word in words:
      if word in syn:
       data=thing
       break
    request["arguments"][i]=(data,"")
   elif arg["type"]=="variable":
    argData=arg["values"][0].split(" ")
    data=""
    if argData[1]=="object":
     if argData[0]=="enviroment":
      temp=["room","goblin"]#,"space"
      #temppair=["room","room"]
      for thing in layer[player["room"]]["contents"]:#future feature: object synonyms; need to add synonyms to objects, some potential script in comments
       #for syn in thing["synonyms"]:
       # temp.append(syn)
       # temppair.append(thing)
       temp.append(thing["name"])
      for word in words:
       if word in temp:
        data=word
        break
      if data in ["room","goblin"]:
       request["arguments"][i]=(data,"")
      else:
       newobj={}
       try:
        f=open("objects/"+data+".data","r")
        newobj=json.load(f)
        f.close()
       except:
        for obj in layer[player["room"]]["contents"]:
         if obj["name"]==data:
          newobj=obj.copy()
          break
       ident=""
       if len(newobj["identifiers"])>0:
        if newobj["identifiers"][0]=="varying":
         idents=[]
         for thing in layer[player["room"]]["contents"]:
          if thing["name"]==data:
           idents.extend(thing["identifiers"])
           idents.append(thing["identifier"])
         idents=list(set(idents))
         for word in words:
          if word in idents:
           ident=word
           break
        else:
         for word in words:
          if word in newobj["identifiers"]:
           ident=word
           break
       request["arguments"][i]=(data,ident)
     elif argData[0]=="non":
      temp=listdir("./objects")
      things=[]
      data=""
      for f in temp:
       things.append(f.split(".")[0])
      for word in words:
       if word in things:
        data=word
        break
      request["arguments"][i]=(data,"")
  return request

def outputText(player,layer):#directly called by client; generates output text
 
 if(player["room"]>=0):
  textblock=layer[player["room"]]["description"].split("&",1)
  textblock.insert(1,mtlists(layer[player["room"]]["contents"]))
  txt=""
  for thing in textblock:
   txt+=thing
 else:
  txt="You appear to have left the map...\nYou will be returned to the center of the map."

 return txt
