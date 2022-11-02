
import os 
import glob
import json
import shutil

# Creating a directory for the files, if the directory already exists, the funtcion will return an error status
try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):# Using the 'glob' function to find the receipts inside the 'processed directory' that match the pattern name established in the function (Ex: 'Finds receipts 1 through 9) 
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed') # this changes from the 'new' to the 'processed' directories
    shutil.move(path, destination)
    print (f"moved '{path}' to '{destination}'") # Using the 'shutil' library to move the file

#using 'round' function to calculate the sum of all the receipts and round them up to a currency friendly format (ex:$00.00)

print(f"Receipt subtotal: ${round(subtotal, 2)}")# The number 2 is telling python to round up the sum to '2' decimal places