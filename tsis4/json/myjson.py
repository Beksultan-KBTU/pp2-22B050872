import json

with open("sample-data.json", "r") as file:
	data = json.load(file)

with open("sample-data.json", "w") as file:
    data = json.dump(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", " " * 8,  "speed", " " * 8, "MTU")
print("-" * 42, "-" * 20, " ", "-" * 7, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:        
    	for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t","\t", " " * 8, imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])