import tensorflow as tf
print(tf.__version__)
# import cv2
# import pyvirtualcam
# from pyvirtualcam import PixelFormat

# vc = cv2.VideoCapture(0)

# if not vc.isOpened():
#     raise RuntimeError('Could not open video source')

# pref_width = 1280
# pref_height = 720
# pref_fps = 30
# vc.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
# vc.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
# vc.set(cv2.CAP_PROP_FPS, pref_fps)

# # Query final capture device values
# # (may be different from preferred settings)
# width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = vc.get(cv2.CAP_PROP_FPS)

# with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR) as cam:
#     print('Virtual camera device: ' + cam.device)
#     while True:
#         ret, frame = vc.read()
#         cv2.putText(frame,"This is opencv's work",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)

#         cam.send(frame)
#         cam.sleep_until_next_frame()