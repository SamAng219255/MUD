import json

def main(door,player,layer):
 reyal=input("Which layer should it go to? (leave blank for this one)\n")
 if reyal=="":
  reyal=player["layer"]
 else:
  reyal=int(reyal)
 door["layer"]=reyal
 moor=input("Which room should it got to? (leave blank for this position)\n")
 if moor="":
  moor=player["room"]
 elif len(moor.split(","))>1:
  mooralt=len(moor.split(","))
  moor=int(mooralt[0])+(64*int(mooralt[1]))
 else:
  moor=int(moor)
 door["room"]=moor
 f=open("objects/portal.data","r")
 newobj=json.load(f)
 f.close()
 lf=open("region/layer"+str(reyal)+".data","r")
 newlayer=json.load(lf)
 lf.close()
 newlayer[moor]["contents"].append(newobj)
 lf=open("region/layer"+str(reyal)+".data","w")
 json.dump(newlayer,lf)
 lf.close()
 newobj["layer"]=player["layer"]
 newobj["room"]=player["room"]
 return door

def remove(door,player,layer):
 lf=open("region/layer"+str(door["layer"])+".data","r")
 newlayer=json.load(lf)
 lf.close()
 postar=[]
 tar={}
 for i in range(len(newlayer[door["room"]]["contents"])):
  if newlayer[door["room"]]["contents"][i]["name"]=="door":
   postar.append(i)
 if len(postar)<1:
  print("Error finding opposite side.")
 elif len(postar)==1:
  tar=postar[0]
 else:
  for i in postar:
   if(newlayer[door["room"]]["contents"][i]["identifier"]==ident):
    tar=i
 del newlayer[door["room"]]["contents"][tar]
 lf=open("region/layer"+str(door["layer"])+".data","w")
 json.dump(newlayer,lf)
 lf.close()
