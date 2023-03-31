
import daemon
import time
from multiprocessing.connection import Listener

def main_program():
    address = ('localhost', 6000)
    with Listener(address) as listener:
        while True:
            with listener.accept() as conn:
                message = conn.recv()
                # put your message handling logic here
                response = 'Response to ' + message
                conn.send(response)
            time.sleep(1)

def run():
    with daemon.DaemonContext():
        main_program()

if __name__ == '__main__':
    run()