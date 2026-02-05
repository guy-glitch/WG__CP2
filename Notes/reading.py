#WG_CP2 Reading a file 
import csv
try:
    with open("individual_projects/Movies list.cvs", "r") as file:
        for line in file:
            print(f"Hello {line.strip()}")
        
except:
    print("That file can't be found.")

else:
    print("Code ends")

try:
    with open("Notes/sample.csv", mode = "r") as sample:
        content = csv.reader(sample)
        headers = next(content)
        rows = []
        for line in content:
           rows.append({headers[0]: line[0], headers[1]: line[1]})

except:
    print("That file can't be found.")
else:
    for line in rows:
        for key in line:
            print(f"{key}: {line[key]}")