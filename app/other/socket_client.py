#!/usr/bin/python3

import socket

# 1.创建socket
socket = socket.socket()

# 2. 连接服务器
socket.connect(('127.0.0.1', 8010))
socket.send(b'connect')

# 3. 接收数据
msg = socket.recv(4096)  # 阻塞
print('Server: ', msg.decode('utf-8'))

# 4. 向服务端发送数据
socket.send("您好，天猫精灵！播放你笑起来真好看！".encode('utf-8'))

# 关闭
socket.close()