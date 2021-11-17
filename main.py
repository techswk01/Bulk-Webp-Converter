from webptools import dwebp
import os, glob

os.chdir("./images")  # working directory

webp_list = []
for file in glob.glob("*.webp"):
    webp_list = file
    print([webp_list])

random_number = random.randint(1,100)
print(random_number)

for files in webp_list:
    print(dwebp(input_image=webp_list, output_image="x.png", option="-o", logging="-v"))

# orignal code allows only 1 input and 1 output
# print(dwebp(input_image="sample.webp", output_image="sample.png", option="-o", logging="-v"))
