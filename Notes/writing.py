#WG_CP2 writing to files notes
import csv

#with open("Notes/read_file.txt", "a") as file:
 #   file.write("I wrote on my file!")
#with open("Notes/read_file.txt", "r") as file:
 #   print(file.read())
  #  print("The code ended")
with open("Notes/sample.csv", 'r+', newline='') as csvfile:
    feildnames = ['dirk', 'aMagenta']
    reader=csv.reader(csvfile)
    for line in reader:
        print(f"{feildnames[0]}, {line[0]} favorite color {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames=feildnames)
    #writer.writeheader()
    writer.writerow({'dirk':'miria', 'aMagenta':'color'})
