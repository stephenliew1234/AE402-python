file=open("dream-giveaway-tesla-model-s-p100d (1).jpg")
img=file.read()
file.close()
file=open("copy image.jpg","wb")
file.write(img)
file.close()
