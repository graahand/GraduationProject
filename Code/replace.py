import os

# specify the directory
directory = '../femaletxtfiles'

# iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        
        # read the file
        with open(filepath, 'r') as file:
            filedata = file.read()

        # replace [Her Name] with [NAME]
        filedata = filedata.replace('[Her Name]', '[NAME]')

        # write the file back
        with open(filepath, 'w') as file:
            file.write(filedata)
