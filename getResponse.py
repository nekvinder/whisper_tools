from multiprocessing.connection import Client

def send_message(message):
    address = ('localhost', 6000)
    with Client(address) as conn:
        conn.send(message)
        response = conn.recv()
        return response

print(send_message("hi how are you?"))