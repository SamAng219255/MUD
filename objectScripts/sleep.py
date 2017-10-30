def main(args,player,layer):
 sleeps=["attempt to find sleep drifting off occasionally but waking up uncomfortable soon after","struggle to find sleep but you eventually fall asleep","fall asleep though you toss and turn throughout the night","fall asleep","comfortably fall asleep","drift peacefully off to sleep"]
 print("You lay down on the "+args[0]+" and "+sleeps[min(max(int(args[1]/2),0),5)]+".")
 strtenergy=player["energy"]
 player["energy"]=int((2*player["energy"]+(args[1]*2+9))/3)
 if(strtenergy>21):
  outcome="well rested"
 elif(player["energy"]>28):
  outcome="extremely well rested and full of energy"
 elif(player["energy"]>21):
  outcome="quite well rested and having a renewed vigor"
 elif(player["energy"]-strtenergy>14):
  outcome="extremely grateful for the much needed rest"
 elif(player["energy"]-strtenergy>7):
  outcome="quite grateful for the rest"
 elif(player["energy"]-strtenergy>0):
  outcome="well rested"
 elif(player["energy"]-strtenergy>-7):
  outcome="not very well rested"
 elif(player["energy"]-strtenergy>-14):
  outcome="more tired than wehen you went to sleep"
 elif(player["energy"]-strtenergy>=-14):
  outcome="fairly exhausted from a terrible nights sleep"
 print("Upon waking you find yourself "+outcome+".")
 player["health"]=min(player["health"]+int(args[1]/5),player["maxHealth"])