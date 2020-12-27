import requests
r = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
# get google logo image to r, use with open to create a writable binary file and write the r into the image file to generate 
with open('google.png', 'wb') as fp:
     fp.write(r.content)