from PIL import Image

picture = Image.open("picture1.png")

print("format file: " + picture.format)
print("file size: " + str(picture.size))
print("file mode: " + picture.mode)

picture.show()