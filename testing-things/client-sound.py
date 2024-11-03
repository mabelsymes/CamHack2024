import socketio

# Example usage
sio = socketio.Client()

@sio.event
def connect():
    print("Successfully connected to the server!")

    # Emit the trigger to play sound after connecting
    sio.emit('play_sound_trigger', {'data': 'Triggering sound playback'})
    print("finished sound emitting")

    # Disconnect after emitting
    sio.disconnect()

@sio.event
def connect_error(data):
    print("The connection failed:", data)

# Connect to the Flask server
sio.connect('http://10.253.121.208:5000')
