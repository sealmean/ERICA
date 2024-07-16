import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import easyocr

def capture_screen_and_recognize_text():
    # 전체 화면 캡처
    screen_capture = ImageGrab.grab()
    screen_capture.save("screen_capture.png")  # 필요하다면 이미지를 저장

    # easyocr을 사용하여 텍스트 인식
    reader = easyocr.Reader(['en'])  # 영문 인식을 위해 'en' 사용
    result = reader.readtext('screen_capture.png', detail=0)  # detail=0, 인식된 텍스트만 반환

    if result:
        recognized_text = "\n".join(result)
        print(recognized_text)  # 콘솔에 인식된 텍스트 출력
        messagebox.showinfo("인식된 텍스트", recognized_text)  # GUI 팝업으로 인식된 텍스트 보여주기
    else:
        messagebox.showinfo("알림", "인식된 텍스트가 없습니다.")

# tkinter GUI 생성
root = tk.Tk()
root.title("캡처 및 텍스트 인식")

capture_button = tk.Button(root, text="화면 캡처 및 텍스트 인식", command=capture_screen_and_recognize_text)
capture_button.pack(pady=20)

root.mainloop()
