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
  playerInput=takeInput(input(""))
  player,layer,playing=runworld(player,layer,playerInput)
  statuswrite(player,layer,userId,layerId)
