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
 if args[1]==1:
  ident="north"
 elif args[1]==3:
  ident="south"
 elif args[1]==0:
  ident="east"
 elif args[1]==2:
  ident="west"
 else:
  ident="center"
 print("You travel "+ident+".")
 player["room"]+=offset
 player["room"]%=64**2
