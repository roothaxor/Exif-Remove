from PIL import Image
import os
os.system('cls')
os.system('title JPG/PNG Exif Remove ( CLI UI ) v.1.2 ~ @root_haxor')
print("\n\nInitiating exif data removing sequence...\n")
relevant_path = os.getcwd()
extensions = ['jpg', 'png']
listfiles = [file for file in os.listdir(relevant_path) if any(file.lower().endswith(ext) for ext in extensions)]
newlist = [x for x in listfiles if not x.startswith('ex_')]
if len(newlist) == 0:
	os.system('cls')
	print("\n\nError! Either Exif data is already removed or No jpg/png files found")
for image_file in newlist:
	image  = Image.open(image_file)
	data = list(image.getdata())
	image_without_exif = Image.new(image.mode, image.size)
	image_without_exif.putdata(data)
	directory = os.getcwd()
	image_without_exif.save(directory + "/ex_" + image_file)
	print("Exif Removed, saved as \ex_%s" % (image_file))
	delete = os.remove(image_file)
print("\n\n+-----------------------------------+")
print("  Exif Removed from %s file or files"%len(newlist))
print("+-----------------------------------+")
