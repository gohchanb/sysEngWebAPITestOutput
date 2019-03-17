import os
import time
import numpy as np

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

size = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(size)
        text = data.decode('utf-8')
            # print(text)
        if text.startswith('SIZE'):
            t = text.split(' ')
            size = int(t[1])
            print("got size "+t[1])
            msg = 'Got SIZE'
            conn.sendall(msg.encode('utf-8'))

            tBefore = time.time()
            byteCount = 0
            fullImage = ''.encode('utf-8')
            while byteCount<size:
                data = conn.recv(size)
                byteCount += len(data)
                fullImage += data
                print(byteCount)
                if not data:
                    break
            print(np.frombuffer(fullImage,dtype=int))
            msg = 'GOT IMAGE'
            conn.sendall(msg.encode('utf-8'))
                # conn.sendall(data)
            tAfter = time.time()
            print("Time main: " + str(tAfter-tBefore))
        else:
            msg = 'ERROR with initialising SIZE'
            conn.sendall(msg.encode('utf-8'))




# @app.route('/getDetectionData', methods = ['GET'])
# def getDetectionData():
#
#     data = request.get_json()
#     frame_in_json = data['data']
#     frame = np.asarray(frame_in_json)
#
#     boxes = [[0.0]*4]*200
#     boxes[0] = [0.18,0.05,0.9,0.35]
#     boxes[1] = [0.2,0.4,0.99,0.67]
#     boxes[2] = [0.09,0.74,0.93,0.92]
#     boxes = [boxes]
#     scores = [0.0]*200
#     scores[0] = 0.7
#     # scores[1] = 0.7
#     scores[2] = 0.7
#     scores = [scores]
#     classes = [1.0]*200
#     classes[1] = 2.0
#     classes[2] = 3.0
#     classes = [classes]
#     return jsonify({'boxes' : boxes, 'scores' : scores, 'classes' : classes, 'num' : 200})
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0',debug=True)