from callscripts import *

def main(player,layer,request,playing):
 if request["arguments"][0]==("room",""):
  layer[player["room"]]={"description":"You are in a blank room with & in it.","contents":[],"look":"You look harder but you still can't find much."}
 else:
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
  try:
   arg,ident=request["arguments"][0]
   layer[player["room"]]["contents"].append(ccs(arg,player,layer))
  except:
   print("Unable to find an original copy so object was only destroyed.\nUsually caused by a name change.")
 return playing