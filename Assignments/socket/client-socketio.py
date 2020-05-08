import socketio

sio = socketio.Client()


@sio.event
def message(data):
    print('I received a message!')
@sio.event
def connect():
    print("I'm connected!")
@sio.event
def connect_error():
    print("The connection failed!")
@sio.event
def disconnect():
    print("I'm disconnected!")

sio.connect('192.168.1.8:4000')

print('my sid is', sio.sid)
sio.emit('my message', {'foo': 'bar'})
