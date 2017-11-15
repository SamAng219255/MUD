from callscripts import *

def main(player,layer,request,playing):
 obj,ident=request["arguments"][0]
 if(obj=="room"):
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
  desc=input("What you like like to change the "+tar["name"]+"'s name to? (leave blank to not change):\n")
  if desc!="":
   tar["name"]=desc
  desc=input("What would you like as the new description? (leave blank to not change):\n")
  if desc!="":
   tar["description"]=desc
 return playing