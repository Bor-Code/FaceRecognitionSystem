import cv2
import face_recognition
import pickle
import numpy as np
from datetime import datetime
import os
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

path = 'ImagesAttendance'
if not os.path.exists(path):
    os.makedirs(path)

encodings_file = "encodings.pickle"
attendance_file = 'Attendance.csv'

if not os.path.exists(attendance_file):
    with open(attendance_file, 'w') as f:
        f.write('Isim,Zaman\n')

known_encodings = []
known_names = []

if os.path.exists(encodings_file):
    try:
        with open(encodings_file, "rb") as f:
            data = pickle.load(f)
        known_encodings = data["encodings"]
        known_names = data["names"]
    except:
        pass

def save_encodings():
    data = {"encodings": known_encodings, "names": known_names}
    with open(encodings_file, "wb") as f:
        f.write(pickle.dumps(data))

def add_new_face(frame, face_loc):
    name = simpledialog.askstring("Yeni Kayıt", "Kişinin İsmini Giriniz:")
    if name:
        clean_name = "".join([c if c.isalnum() else "_" for c in name])
        img_name = f"{path}/{clean_name}.jpg"
        cv2.imwrite(img_name, frame)
        
        rgb_small = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_small, [face_loc])[0]
        
        known_encodings.append(encoding)
        known_names.append(clean_name)
        save_encodings()
        messagebox.showinfo("Başarılı", f"{clean_name} başarıyla kaydedildi!")

def delete_face(name):
    if name == "BILINMIYOR":
        return
    
    response = messagebox.askyesno("Sil", f"{name} kişisini silmek istiyor musun?")
    if response:
        if name in known_names:
            index = known_names.index(name)
            known_names.pop(index)
            known_encodings.pop(index)
            save_encodings()
            
            file_path = f"{path}/{name}.jpg"
            if os.path.exists(file_path):
                os.remove(file_path)
            
            messagebox.showinfo("Silindi", f"{name} sistemden silindi.")

def mark_attendance(name):
    with open(attendance_file, 'r+') as f:
        lines = f.readlines()
        name_list = [line.split(',')[0] for line in lines]
        if name not in name_list:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            f.write(f'{name},{dt_string}\n')

click_event = None

def mouse_handler(event, x, y, flags, param):
    global click_event
    if event == cv2.EVENT_LBUTTONDOWN:
        click_event = (x, y)

window_name = "Gelismis Yuz Tanima Paneli"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(window_name, mouse_handler)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success: break

    try:
        prop = cv2.getWindowImageRect(window_name)
        win_w, win_h = prop[2], prop[3]
    except:
        win_w, win_h = 640, 480

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_rgb = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
    
    faces_cur_frame = face_recognition.face_locations(img_rgb)
    encodes_cur_frame = face_recognition.face_encodings(img_rgb, faces_cur_frame)

    img_display = cv2.resize(img, (win_w, win_h))
    scale_x = win_w / img.shape[1]
    scale_y = win_h / img.shape[0]

    current_face_name = "BILINMIYOR"
    current_face_loc = None

    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        matches = face_recognition.compare_faces(known_encodings, encode_face, tolerance=0.5)
        face_dis = face_recognition.face_distance(known_encodings, encode_face)
        
        match_index = -1
        if len(face_dis) > 0:
            match_index = np.argmin(face_dis)

        if match_index != -1 and matches[match_index]:
            name = known_names[match_index]
            color = (0, 255, 0)
        else:
            name = "BILINMIYOR"
            color = (0, 0, 255)
        
        current_face_name = name
        
        y1, x2, y2, x1 = face_loc
        y1, x2, y2, x1 = int(y1 * 4), int(x2 * 4), int(y2 * 4), int(x1 * 4)
        
        current_face_loc = (y1, x2, y2, x1)

        disp_x1 = int(x1 * scale_x)
        disp_y1 = int(y1 * scale_y)
        disp_x2 = int(x2 * scale_x)
        disp_y2 = int(y2 * scale_y)

        cv2.rectangle(img_display, (disp_x1, disp_y1), (disp_x2, disp_y2), color, 3)
        cv2.putText(img_display, name, (disp_x1 + 5, disp_y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if name != "BILINMIYOR":
            mark_attendance(name)

    overlay = img_display.copy()
    
    btn_w = 150
    btn_h = 50
    margin = 20

    exit_x1, exit_y1 = win_w - btn_w - margin, margin
    cv2.rectangle(overlay, (exit_x1, exit_y1), (exit_x1 + btn_w, exit_y1 + btn_h), (0, 0, 200), -1)
    
    add_x1, add_y1 = margin, win_h - btn_h - margin
    cv2.rectangle(overlay, (add_x1, add_y1), (add_x1 + btn_w, add_y1 + btn_h), (200, 100, 0), -1)

    del_x1, del_y1 = win_w - btn_w - margin, win_h - btn_h - margin
    cv2.rectangle(overlay, (del_x1, del_y1), (del_x1 + btn_w, del_y1 + btn_h), (0, 0, 0), -1)

    alpha = 0.7
    cv2.addWeighted(overlay, alpha, img_display, 1 - alpha, 0, img_display)

    cv2.putText(img_display, "CIKIS", (exit_x1 + 35, exit_y1 + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(img_display, "KAYIT ET", (add_x1 + 15, add_y1 + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(img_display, "SIL", (del_x1 + 50, del_y1 + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    if click_event:
        cx, cy = click_event
        click_event = None
        
        if exit_x1 < cx < exit_x1 + btn_w and exit_y1 < cy < exit_y1 + btn_h:
            break
            
        if add_x1 < cx < add_x1 + btn_w and add_y1 < cy < add_y1 + btn_h:
            if current_face_loc:
                y1, x2, y2, x1 = current_face_loc
                face_img = img[y1:y2, x1:x2]
                if face_img.size > 0:
                    add_new_face(face_img, (0, face_img.shape[1], face_img.shape[0], 0))
            else:
                messagebox.showwarning("Hata", "Yüz algılanamadı! Kameraya bakınız.")

        if del_x1 < cx < del_x1 + btn_w and del_y1 < cy < del_y1 + btn_h:
            if current_face_name != "BILINMIYOR":
                delete_face(current_face_name)
            else:
                messagebox.showwarning("Hata", "Silinecek kayıtlı bir yüz bulunamadı.")

    cv2.imshow(window_name, img_display)

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break
        
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
root.destroy()