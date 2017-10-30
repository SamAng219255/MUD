import json

def tlist(listed):
	finalList=[]
	for i in range(len(listed)):
		if(listed[i][1]>0):
			finalList.append(listed[i])
	textListAND = ""
	if(len(finalList)>1):
		for i in range(len(finalList)-1):
			if(finalList[i][1]==1):
				if finalList[i][0][0] in ["a","e","i","o","u","A","E","I","O","U"]:
					textListAND+="an "
				else:
					textListAND+="a "
			elif(finalList[i][1]>1):
				textListAND+=(str(finalList[i][1])+" ")
			textListAND+=(finalList[i][0]+"")
			if(finalList[i][1]>1):
				if(len(finalList[i])==3 or finalList[i][3] == False):
					lastCharacter=str(finalList[i][0])[len(list(finalList[i][0]))-1];
					slastCharacter=str(finalList[i][0])[len(list(finalList[i][0]))-2];
					if lastCharacter in ["s","S","h","H","ʒ","Ʒ"]:
						textListAND+="es"
					elif (lastCharacter in ["y","Y"]) and not (slastCharacter in ["a","i","o","u","y","A","I","O","U","Y"]):
						textListAND=textListAND[0: -1]
						if slastCharacter in ["e","E"]:
							textListAND=textListAND[0:-1]
						textListAND+="ies"
					else:
						textListAND+="s"
			if type(finalList[i][2]) == type(""):
				textListAND+=finalList[i][2]
			if(len(finalList)>2):
				textListAND+=", "
			else:
				textListAND+=" "
		i+=1
		finalWord=finalList[len(finalList)-1][0]
		textListAND+="and "
		if(finalList[i][1]==1):
			if finalWord[0] in ["a","e","i","o","u","A","E","I","O","U"]:
				textListAND+="an "
			else:
				textListAND+="a "
		elif(finalList[i][1]>1):
			textListAND+=(str(finalList[i][1])+" ")
		textListAND+=finalWord
		if(finalList[i][1]>1):
			if(len(finalList[i])==3 or finalList[i][3] == False):
				lastCharacter=finalWord[len(finalWord)-1];
				slastCharacter=finalWord[len(finalWord)-2];
				if lastCharacter in ["s","S","h","H","ʒ","Ʒ"]:
					textListAND+="es"
				elif (lastCharacter in ["y","Y"]) and not (slastCharacter in ["a","i","o","u","y","A","I","O","U","Y"]):
					textListAND=textListAND[0:-1]
					if slastCharacter in ["e","E"]:
						textListAND=textListAND[0:-1]
					textListAND+="ies"
				else:
					textListAND+="s"
		if(type(finalList[i][2]) == type("")):
			textListAND+=finalList[i][2]
		return textListAND
	elif(len(finalList)==1):
		if(finalList[0][1]==1):
			if(finalList[0][0][0] in ["a","e","i","o","u","A","E","I","O","U"]):
				textListAND+="an "
			else:
				textListAND+="a "
		elif(finalList[0][1]>1):
			textListAND+=(str(finalList[0][1])+" ")
		textListAND+=finalList[0][0]
		if(finalList[0][1]>1):
			if(len(finalList[0])==3 or finalList[0][3] == False):
				lastCharacter=finalList[0][0][len(finalList[0][0])-1]
				slastCharacter=finalList[0][0][len(finalList[0][0])-2]
				if(["s","S","h","H","ʒ","Ʒ"].indexOf(lastCharacter)>=0):
					textListAND+="es"
				elif(lastCharacter in ["y","Y"]) and not (slastCharacter in ["a","i","o","u","y","A","I","O","U","Y"]):
					textListAND=textListAND[0:-1]
					if slastCharacter in ["e","E"]:
						textListAND=textListAND[0:-1]
					textListAND+="ies"
				else:
					textListAND+="s"
		if type(finalList[0][2]) == type(""):
			textListAND+=finalList[i][2]
		return textListAND
	else:
		return "nothing"

def stlist(listed):
	outText=""
	textListAND = ""
	if listed.length>1:
		for i in range(len(listed)-1):
			textListAND+=listed[i]
			textListAND+=", "
		textListAND+="and "
		textListAND+=listed[listed.length-1]
		outText=textListAND
	elif len(listed)==1:
		textListAND+=listed[0]
		outText=textListAND
	else:
		outText="nothing"
	return outText;

if __name__=='__main__':
	print(textList(json.loads(input("Input list: "))))
