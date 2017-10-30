def main(args,player,layer):
 if "bucket" in player["inventory"]:
  player["inventory"].remove("bucket")
  player["inventory"].append("water bucket")
  print("You draw up water and fill your bucket.")
 else:
  print("You don't have anywhere to put the water.")