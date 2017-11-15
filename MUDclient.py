from worldstatus import *
from interface import *
import socket

if __name__=="__main__":
 playing=True
 try:
  userId=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]#WIP
 except:
  print("You are offline.")
  userId="172"
 while playing:
  player,layer=statusread(userId)
  layerId=player["layer"]
  print(outputText(player,layer))
  while True:
   try:
    playerInput=takeInput(player,layer)
    if player["room"]<0:
     player,layer,playing=runworld(player,layer,playerInput)
    elif len(playerInput["arguments"])>0 and playerInput["arguments"][0][0]=="goblin":
     print("There are no more goblins…")
    else:
     player,layer,playing=runworld(player,layer,playerInput)
     statuswrite(player,layer,userId,layerId)
   except:
    print("That target does not exist.")
    raise Exception("stop")#in case of accidental unbreakable infinite loops.
    continue
   break
