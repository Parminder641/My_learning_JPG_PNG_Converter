from sys import argv
import os

from PIL import Image

source = argv[1]
target = argv[2]

# check if destination folder exist or not, create if does not exist
if not os.path.exists(target):
    os.makedirs(target)

# conversion of jpg to PNG
for infile in os.listdir(source):
    if infile.endswith('.jpg'):
        f, e = os.path.splitext(infile)
        outfile = f + ".png"
        if infile != outfile:
            try:
                with Image.open(f'{source}\\{infile}') as im:
                    print(f'converting {infile}')
                    im.save(f'{target}\\{outfile}')

            except FileNotFoundError as err:
                print(err)
            except IndentationError as err:
                print('check empty spaces', err)
    else:
        print(f'No .JPG file/s exist in {source} \nPlease check folder path and run again.')



