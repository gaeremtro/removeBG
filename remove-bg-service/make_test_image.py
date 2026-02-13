from PIL import Image, ImageDraw

def create_test_image():
    img = Image.new('RGB', (200, 200), color='blue')
    d = ImageDraw.Draw(img)
    d.ellipse((50, 50, 150, 150), fill='red')
    img.save('test_image.jpg')
    print("Created test_image.jpg")

if __name__ == "__main__":
    create_test_image()
