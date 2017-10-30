import json
import sys

def genBlankRegion():
 region=[{"description":"You are in a blank room with & in it.","contents":[],"look":"You look harder but you still can't find much."}]*(64**2)
 return json.dumps(region)

if __name__=='__main__':
 regionstr=genBlankRegion()
 if len(sys.argv)==1:
  rangstr=input("Which layers which would like to create/reset?\n")
  ranglst=rangstr.split(",")
  if len(ranglst)==1:
   ranglst=[ranglst[0],ranglst[0]]
 elif len(sys.argv)==2:
  ranglst=[sys.argv[1],sys.argv[1]]
 else:
  ranglst=[sys.argv[1],sys.argv[2]]
 for i in range(int(ranglst[0]),int(ranglst[1])+1):
  f=open("region/layer"+str(i)+".data","w")
  f.write(regionstr)
  f.close()
