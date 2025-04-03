
from PIL import Image, ImageDraw

# Kalibrierte Werte
a_lon = 8.763412756163602
b_lon = 1568.5272737227672
a_lat = -11.122611080927257
b_lat = 1319.0283253564514

def geo_to_pixel(lat, lon):
    x = a_lon * lon + b_lon
    y = a_lat * lat + b_lat
    return int(x), int(y)

def add_spot(lat, lon, image_path="static/map.png", color="#0693E3", radius=4):
    img = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    x, y = geo_to_pixel(lat, lon, img.width, img.height)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    img.save(image_path)
