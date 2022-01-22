#!/usr/bin/env python
"""
Reads & Prints KISS frames from a TCP Socket.

For use with programs like Dire Wolf.

Use the TCP timeout option to time out and handle other tasks
"""

import sys
import socket
import time

sys.path.append("..")

import kiss

def print_frame(frame):
    print(f"Rx frame: {frame}")

def main():
    ki = kiss.TCPKISS(host='localhost', port=8001, timeout=0)
    ki.start()
    timeout_counter = 0
    while True:
        try:
            ki.read(callback=print_frame)
        except socket.timeout as e:
            print(f"timeout.. {timeout_counter}")
            timeout_counter += 1
            pass
        except BlockingIOError as e:
            print("resource temp unavail")
            time.sleep(1)




if __name__ == '__main__':
    main()
