from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS with specified origins
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, max_http_buffer_size=70 * 1024 * 1024)

@app.route('/')
def index():
    return render_template('index.html')  # Render the webpage

@app.route('/criminal')
def criminal_page():
    return render_template('criminal.html')  # Create this HTML file in the templates folder

# Receive message from client, then emit to trigger sound
@socketio.on('play_sound_trigger')
def handle_play_sound_trigger(data):
    print('Received trigger from client:', data)
    socketio.emit('play_sound')  # Emit event to play sound on the webpage

@socketio.on('send_image')
def handle_send_image(data):
    print('Received image data from client:')

    filename = data['filename']
    image_data = data['image_data']
    
    # Ensure the uploads folder exists
    os.makedirs('static/uploads', exist_ok=True)
    
    # Save the image to the uploads folder
    filepath = os.path.join('static/uploads', filename)
    with open(filepath, 'wb') as f:
        f.write(image_data)

    print("WRITTEN IMAGE")

if __name__ == '__main__':
    socketio.run(app, host='10.253.121.208', port=5000, debug=True)
