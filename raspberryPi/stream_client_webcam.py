import pygame.camera
import socket

host='192.168.178.72'
port=8080

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(352,288),'RGB')
cam.start()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

def send_image():
    img = cam.get_image()
    img_str = pygame.image.tostring(img,"RGB")
    s.sendall(img_str)

while True:
    send_image()

    while True:
        confirm_message = s.recv(8)
        if confirm_message == "Received":
            break

s.close()
