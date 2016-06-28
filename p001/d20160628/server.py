#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 ok\r\n\r\n")
    client.send("Hello, World!")


def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8011))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()