import sys
from PIL import Image, ImageDraw, ImageFont

path = 'ADD YOUR PATH HERE'

if (len(sys.argv) == 3):
	fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 28)
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	try:
		dims = sys.argv[1] +"x" +sys.argv[2]
		name = "%s.jpg" %dims
		path = path + "/" + name
		#print(path)
		img = Image.new('RGB', (a, b), color = (200, 200, 200))
		d = ImageDraw.Draw(img)
		d.text((25, 25), dims, font=fnt, fill=(0,0,0))
		
    	
		img.save(path)
	except:
		print("Invalid arguments")
else:
	print("Invalid arguments")
