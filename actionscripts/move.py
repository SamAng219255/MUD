from callscripts import *

def main(player,layer,request,playing):
 obj,ident=request["arguments"][0]
 newrequest={"action":"activate","arguments":[("door",obj)]}
 runworld(player,layer,newrequest)
 return playing