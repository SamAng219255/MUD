stones=["N","NNE","ENE","E","ESE","SSE","S","SSW","WSW","W","WNW","NNW"]
targets=[-1,-1,-1,64,-1,-1,-1,-1,-1,-1,-1,-1]
stonedata=[("white","cold glyph"),("purple","flowery glyph"),("cyan","glyph which reminds you of rolling waves"),("marbled blue and green","simple glyph which makes you think of home"),("yellow","glyph which seems strangely dry"),("black","dark glyph which scares you"),("marbled red and black","fiery glyph"),("red","hard edged glyph"),("blue","glyph"),("green","glyph which looks like a large tree"),("pink","glyph"),("lime","glyph")]

def main(args,player,layer):
 action=""
 while not action in ["1","2"]:
  action=input("What do you want to do with them?:\n (1): look at them\n (2): activate one")
  if not action in ["1","2"]:
   print("Please choose an option. (1,2)")
 selected=""
 while not selected in stones:
  selected=input("Which stone?\nNorth(N), North North East(NNE), East North East(ENE), East(E), East South East(ESE), South South East(SSE), South(S), etc. (SSW WSW W WNW NNW)")
  if not selected in stones:
   print("Please enter a direction. (N,NNE,ENE,E,ESE,SSE,S,SSW,WSW,W,WNW,NNW)")
 if action=="1":
  color,glyphtxt=stonedata[stones.index(selected)]
  print("You approach the massive stone. There is a "+glyphtxt+" roughly halfway up the stone. In a hole at its top it has a bright disk made of some sort of flourescent "+color+" stone.")
 elif action=="2":
  player["room"]=targets[stone.index(selected)]
  print("As you approach the stone, upon seeing the glyph a word comes to mind. You are not able to describe how it would be pronounced, yet you instinctively speak it.\nIn an instant, the beam from the central pillar swings around and centers on the stone disk, continuing on into the distance now stained with the stone's color and you are drawn up into in a whirl of the same color.\n\nYou awaken before smaller stone with the same glyph.")