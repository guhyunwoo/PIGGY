import torch
import cv2
import subprocess
import numpy as np
import requests

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/hyunwoo/PIGGY/best.pt')

server_url = "http://10.150.151.236/log"

# FFmpeg로 카메라 스트림 가져오기
ffmpeg_command = [
    'ffmpeg',
    '-i', '/dev/video0',  # 라즈베리파이 카메라 입력 (USB 카메라라면 경로 확인 필요)
    '-f', 'image2pipe',
    '-pix_fmt', 'bgr24',
    '-s', '640x480',
    '-vcodec', 'rawvideo', '-'
]

process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, bufsize= 4 * (10**8))

try:
    while True:
        raw_frame = process.stdout.read(640 * 480 * 3)
        if not raw_frame:
            break
        
        frame = np.frombuffer(raw_frame, np.uint8).reshape((480, 640, 3))
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # YOLOv5 모델로 예측
        results = model(image)
        
        # 예측 결과 처리
        for result in results.xywh[0]:
            x, y, w, h, conf, cls = result.tolist()
            if conf > 0.1:
                object_info = {
                    "coin": int(results.names[int(cls)])
                }
                
                try:
                    response = requests.post(server_url, json=object_info)
                    if response.status_code == 200:
                        print("Object data successfully saved.")
                    else:
                        print(f"Failed to save object data: {response.status_code}, coin : {object_info}")
                except Exception as e:
                    print(f"Error sending request: {e}")
        
        # 결과 화면 표시
        results.render()
        output_image = results.ims[0]
        cv2.imshow("YOLO Detection", output_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("사용자로 인한 종료.")
finally:
    process.terminate()
    cv2.destroyAllWindows()
