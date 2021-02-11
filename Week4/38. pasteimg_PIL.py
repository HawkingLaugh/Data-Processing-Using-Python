#%%
from PIL import Image

# Image.open() to open an image, an Image object
im1 = Image.open('1.jpg')
print(im1.size, im1.format, im1.mode)

# Save and image object into another image object
Image.open('1.jpg').save('2.png')
im2 = Image.open('2.png')

size = (288,180)
im2.thumbnail(size)
# counterclockwise
out = im2.rotate(45)

# paste the rotated image into first img
im1.paste(out,(50,50))
im1.show()
# %%
