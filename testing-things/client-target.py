import socketio
from PIL import Image

def compress_image(input_image_path, output_image_path, quality=20):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, 'JPEG', quality=quality)

# Example usage
sio = socketio.Client()

@sio.event
def connect():
    print("Successfully connected to the server!")

    image_path = 'static/resources/test.jpg'  # Change this to your image path
    compress_image(image_path, image_path, quality=5)
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Emit the image data
    sio.emit('send_image', {'filename': 'target.jpg', 'image_data': image_data})
    print("sent target image data")

    # Disconnect after emitting
    sio.disconnect()

@sio.event
def connect_error(data):
    print("The connection failed:", data)

# Connect to the Flask server
sio.connect('http://127.0.0.1:5000')
