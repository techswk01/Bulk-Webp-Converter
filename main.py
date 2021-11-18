import glob, os
from webptools import dwebp  # library to convert webp to png
os.chdir("./images")  # working directory
# scans directory for webp files
webp_list = glob.glob("*.webp")

#using for loop to go through the files in the list
for filename in webp_list:
    # removes the .webp extension and maintain the original filename for output
    outname = filename[:-4] + "png"
    dwebp(input_image=filename, output_image=outname, option="-o", logging="-v")

#single input single output
#print(dwebp(input_image=filename, output_image=outname, option="-o", logging="-v"))


