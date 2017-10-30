def main(obj,player,layer):
 invalidcolor=True
 color="red"
 while invalidcolor:
  color=input("What color is it?\n").lower()
  invalidcolor=not (color in ["red","orange","yellow","white","blue","purple","black"])
 obj["color"]=color
 obj["identifier"]=color
 obj["description"]="It's a "+obj["color"]+" flower."
 return obj

def remove(obj,player,layer):
 return

#09,CA,0B,0F,0C,05,00