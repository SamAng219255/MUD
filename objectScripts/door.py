def psuetrig(x,linelen):
 if(x%4==0):
  return 1
 elif(x%4==1):
  return linelen
 elif(x%4==2):
  return -1
 elif(x%4==3):
  return 0-linelen

def main(args,player,layer):
 offset=psuetrig(args[1],64)
 print("You open the "+args[0]+" and enter the room on the other side.")
 player["room"]+=offset
 player["room"]%=64**2
