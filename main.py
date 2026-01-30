import cv2
import face_recognition
import pickle
import numpy as np
from datetime import datetime
import os
import sys

try:
    if os.path.exists("encodings.pickle"):
        with open("encodings.pickle", "rb") as f:
            data = pickle.load(f)
        known_encodings = data["encodings"]
        known_names = data["names"]
    else:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "HATA: encodings.pickle dosyası bulunamadı!\nLütfen bu dosyayı .exe'nin yanına koyun.", "Eksik Dosya", 16)
        sys.exit()
except Exception as e:
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, f"Bir hata oluştu: {e}", "Hata", 16)
    sys.exit()

filename = 'Attendance.csv'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write('Isim,Zaman\n')

button_pressed = False

def mouse_handler(event, x, y, flags, param):
    global button_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        if x > param['w'] - 150 and y < 60: 
            button_pressed = True

def mark_attendance(name):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        name_list = [line.split(',')[0] for line in lines]
        if name not in name_list:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            f.write(f'{name},{dt_string}\n')

window_name = "Yuz Tanima Sistemi V2.0"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(window_name, mouse_handler, param={'w': 640}) 

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success: break

    try:
        prop = cv2.getWindowImageRect(window_name)
        win_w, win_h = prop[2], prop[3]
    except:
        win_w, win_h = 640, 480
    
    cv2.setMouseCallback(window_name, mouse_handler, param={'w': win_w})

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
    
    faces_cur_frame = face_recognition.face_locations(img_rgb)
    encodes_cur_frame = face_recognition.face_encodings(img_rgb, faces_cur_frame)

    img_display = cv2.resize(img, (win_w, win_h))
    
    scale_x = win_w / img.shape[1]
    scale_y = win_h / img.shape[0]

    detected_name = ""

    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        matches = face_recognition.compare_faces(known_encodings, encode_face, tolerance=0.5)
        face_dis = face_recognition.face_distance(known_encodings, encode_face)
        match_index = np.argmin(face_dis)

        if matches[match_index]:
            name = known_names[match_index].upper()
            color = (0, 255, 0)
        else:
            name = "BILINMIYOR"
            color = (0, 0, 255)
        
        detected_name = name
        
        y1, x2, y2, x1 = face_loc
        x1 = int(x1 * 4 * scale_x)
        y1 = int(y1 * 4 * scale_y)
        x2 = int(x2 * 4 * scale_x)
        y2 = int(y2 * 4 * scale_y)

        cv2.rectangle(img_display, (x1, y1), (x2, y2), color, 3)
        
        text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        cv2.rectangle(img_display, (x1, y2 - 35), (x1 + text_size[0] + 10, y2), color, cv2.FILLED)
        cv2.putText(img_display, name, (x1 + 5, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if name != "BILINMIYOR":
            mark_attendance(name)

    overlay = img_display.copy()
    cv2.rectangle(overlay, (0, win_h - 80), (win_w, win_h), (0, 0, 0), -1)
    
    cv2.rectangle(overlay, (win_w - 150, 0), (win_w, 60), (0, 0, 200), -1)
    
    alpha = 0.6
    cv2.addWeighted(overlay, alpha, img_display, 1 - alpha, 0, img_display)

    info_text = f"Sistem Aktif | Tespit: {detected_name if detected_name else 'Bekleniyor...'}"
    cv2.putText(img_display, info_text, (30, win_h - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    cv2.putText(img_display, "CIKIS", (win_w - 110, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow(window_name, img_display)

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break
    
    if button_pressed:
        break
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()