stones=["N","NNE","ENE","E","ESE","SSE","S","SSW","WSW","W","WNW","NNW"]
targets=[]

def main(args,player,layer):
 selected=""
 while not selected in stones:
  selected=input("Which stone will you activate?\nNorth(N), North North East(NNE), East North East(ENE), East(E), East South East(ESE), South South East(SSE), South(S), etc. (SSW WSW W WNW NNW)")
  if not selected in stones:
   print("Invalid imput.")
 
