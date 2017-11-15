from callscripts import *

def main(player,layer,request,playing):
 arg,ident=request["arguments"][0]
 layer[player["room"]]["contents"].append(ccs(arg,player,layer))
 return playing