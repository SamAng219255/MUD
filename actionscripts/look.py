from callscripts import *

def main(player,layer,request,playing):
 obj,ident=request["arguments"][0]
 if(obj=="room"):
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
 return playing