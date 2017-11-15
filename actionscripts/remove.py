from callscripts import *

def main(player,layer,request,playing):
 if request["arguments"][0]==("room",""):
  print("You delete the room.\n\nGood job. you have deleted the space you are inside of. *slow clap*\nNow, as that causes lots of problems because the rooms aren't actually dynamic enough to handle your desire, I'll have to roll back the entire server just because you decided that with infinite creative power YOU wanted to climb into a box and delete it.")
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
 return playing