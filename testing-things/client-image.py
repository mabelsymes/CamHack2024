import socketio
from PIL import Image

def compress_image(input_image_path, output_image_path, quality=20):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, 'JPEG', quality=quality)

sio = socketio.Client()

@sio.event
def connect():
    print("Successfully connected to the server!")

    image_data =

    # Emit the image data
    sio.emit('send_image', {'filename': 'computer-vision.jpg', 'image_data': image_data})
    print("sent live image data")

    # Disconnect after emitting
    sio.disconnect()

@sio.event
def connect_error(data):
    print("The connection failed:", data)

# Connect to the Flask server
sio.connect('http://10.253.121.208:5000')
