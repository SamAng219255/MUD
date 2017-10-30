import json

def psuetrig(x,linelen):
 if(x%4==0):
  return 1
 elif(x%4==1):
  return linelen
 elif(x%4==2):
  return -1
 elif(x%4==3):
  return 0-linelen

def main(door,player,layer):
 wall=input("Which wall should it be on?\n")
 if wall.lower() in ["north","northern","upper","top"]:
  wall=1
  ident="north"
  ident2="south"
 elif wall.lower() in ["south","southern","lower","bottom"]:
  wall=3
  ident="south"
  ident2="north"
 elif wall.lower() in ["east","eastern","right"]:
  wall=0
  ident="east"
  ident2="west"
 elif wall.lower() in ["west","western","left","sinister"]:
  wall=2
  ident="west"
  ident2="east"
 else:
  wall=24
  ident="center"
  ident2="center"
 f=open("objects/openwall.data","r")
 newobj=json.load(f)
 f.close()
 newobj["wall"]=(wall+2)%4
 newobj["identifier"]=ident2
 newobj["name"]=""
 layer[(player["room"]+psuetrig(wall,64))%(64**2)]["contents"].append(newobj)
 door["wall"]=wall
 door["identifier"]=ident
 door["name"]=""
 return door

def remove(door,player,layer):
 ident="center"
 if door["identifier"]=="north":
  ident="south"
 if door["identifier"]=="south":
  ident="north"
 if door["identifier"]=="east":
  ident="west"
 if door["identifier"]=="west":
  ident="east"
 postar=[]
 tar={}
 for i in range(len(layer[(player["room"]+psuetrig(door["wall"],64))%(64**2)]["contents"])):
  if layer[(player["room"]+psuetrig(door["wall"],64))%(64**2)]["contents"][i]["hiddenname"]=="openwall":
   postar.append(i)
 if len(postar)<1:
  print("I'm sorry. I didn't understand that.")
 elif len(postar)==1:
  tar=postar[0]
 else:
  for i in postar:
   if(layer[(player["room"]+psuetrig(door["wall"],64))%(64**2)]["contents"][i]["identifier"]==ident):
    tar=i
 del layer[(player["room"]+psuetrig(door["wall"],64))%(64**2)]["contents"][tar]
