    import tkinter as tk
    from tkinter import messagebox
    from PIL import ImageGrab
    import easyocr
    import pyperclip

    def capture_screen_and_recognize_text():
        # 전체 화면 캡처
        screen_capture = ImageGrab.grab()
        screen_capture.save("screen_capture.png")  # 필요하다면 이미지를 저장

        # easyocr을 사용하여 텍스트 인식
        reader = easyocr.Reader(['en'])  # 영문 인식을 위해 'en' 사용
        result = reader.readtext('screen_capture.png', detail=0)  # detail=0, 인식된 텍스트만 반환

        # 6자리인 영어 대문자 단어 찾기
        found_text = ""
        for text in result:
            if len(text) == 6 and text.isupper() and text != int:
                found_text = text
                break

        if found_text:
            print(found_text)  # 콘솔에 인식된 텍스트 출력
            pyperclip.copy(found_text)  # 클립보드에 텍스트 복사
            messagebox.showinfo("인식된 텍스트", f"인식된 텍스트: {found_text}\n클립보드에 복사되었습니다.")
        else:
            messagebox.showinfo("알림", "6자리의 영어 대문자 단어가 없습니다.")

    # tkinter GUI 생성
    root = tk.Tk()
    root.title("캡처 및 텍스트 인식")

    capture_button = tk.Button(root, text="화면 캡처 및 텍스트 인식", command=capture_screen_and_recognize_text)
    capture_button.pack(pady=20)

    root.mainloop()
