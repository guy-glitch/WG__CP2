#WG_CP2 writing to files notes
import csv

#with open("Notes/read_file.txt", "a") as file:
 #   file.write("I wrote on my file!")
#with open("Notes/read_file.txt", "r") as file:
 #   print(file.read())
  #  print("The code ended")
feildnames = ['dirk', 'aMagenta']

# Read and display existing rows
with open("Notes/sample.csv", 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if line:
            print(f"{feildnames[0]}, {line[0]} favorite color {line[1]}")

# Append a new row at the end of the file
with open("Notes/sample.csv", 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=feildnames)
    writer.writerow({'dirk':'miria', 'aMagenta':'color'})
