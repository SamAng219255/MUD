import json
import ftplib
import getpass

inDev=True

def statusread(userId):
 player={}
 if not (userId.split(".",1)[0]=="172" or inDev):
  connection=ftplib.FTP(host="10.183.2.9",user=("dungeoneer"+userId.split(".")[3]),passwd=getpass.getpass("Please enter your password for the game:\n"))
  connection.sendcmd("cd MUD/")
  pf=open("player.data","r")
  player=json.load(pf)
  pf.close()
  connection.tranfercmd("put player.data")
  connection.sendcmd("cd region/")
  connection.tranfercmd("put layer"+str(player["layer"])+".data")
 else:
  pf=open("player.data","r")
  player=json.load(pf)
  pf.close()
 lf=open("region/layer"+str(player["layer"])+".data","r")
 layer=json.load(lf)
 lf.close()
 return player,layer

def statuswrite(player,layer,userId,layerId):
 pf=open("player.data","w")
 json.dump(player,pf)
 pf.close()
 lf=open("region/layer"+str(layerId)+".data","w")
 json.dump(layer,lf)
 lf.close()
 if not (userId.split(".",1)[0]=="172" or inDev):
  connection=ftplib.FTP(host="10.183.2.9",user=("dungeoneer"+userId.split(".")[3]),passwd=getpass.getpass("Please enter your password for the game:\n"))
  connection.sendcmd("cd MUD/")
  connection.tranfercmd("put player.data")
  
  connection.sendcmd("cd region/")
  connection.tranfercmd("put layer"+str(player["layer"])+".data")
