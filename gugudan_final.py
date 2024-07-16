import tkinter as tk
from tkinter import ttk, Toplevel, Label, StringVar
import random
import time

class gugudanbasic: # 기본 구구단게임
    def __init__(self, master):
        self.master = master
        self.master.title("GUGUDAN Game Basic")
        self.master.geometry("300x170")

        self.score = 0
        self.num1 = 0
        self.num2 = 0
        self.start_time = 0
        self.count = 0
        
        self.label_question = ttk.Label(master, text="", font=("맑은 고딕", 15, "bold"))
        self.label_question.pack(pady=10)

        self.entry_answer = ttk.Entry(master, font=("맑은 고딕", 15, "bold"))
        self.entry_answer.pack(pady=5)
        self.entry_answer.bind('<Return>', self.check_answer_enter) #enter입력<return> 처리,bind 이벤트처리

        self.label_result = ttk.Label(master, text="", font=("맑은 고딕", 15, "bold"))
        self.label_result.pack(pady=5)

        self.start_game()

    def start_game(self):  # 게임 시작
        self.score = 0
        self.start_time = time.time()
        self.entry_answer.configure(state="normal") # 상태 노말로 설정해두기
        self.generate_question()

    def generate_question(self):
        self.num1 = random.randint(2, 9)
        self.num2 = random.randint(2, 9)
        self.label_question.config(text=f"{self.num1} X {self.num2}=?") #질문 라벨 config

    def check_answer_enter(self, event):  # enter 체크
        self.check_answer()

    def check_answer(self):
        user_answer = self.entry_answer.get() #entry_answer에 있는 글자 가져옴
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == self.num1 * self.num2:
                self.score += 1 #점수 올리기
                self.label_result.config(text="정답입니다!", foreground="green",font=("맑은 고딕", 10, "bold")) # 맞았으면
            else:
                self.label_result.config(text="틀렸어요...", foreground="red",font=("맑은 고딕", 10, "bold")) # 틀렸으면
        else:
            self.count -= 1 #다시 입력받아야하니 count -1
            self.label_result.config(text="정수를 입력해 주세요.", foreground="blue",font=("맑은 고딕", 10, "bold")) # 정수 입력이 아니라면
        
        self.entry_answer.delete(0, tk.END) # 답 입력창 삭제
        self.count += 1

        if self.count < 5:
            self.generate_question()  # 문제 재생성
        else:
            self.end_game()  # 다섯 번 푼 후 게임 종료

    def end_game(self): # 종료
        self.entry_answer.config(state="disabled") 
        self.end_time = time.time()
        self.entry_answer.unbind('<Return>')  # Enter 키 unbind
        if self.score == 5: #점수별로 출력 텍스트 변경
            self.label_result.config(text=f"축하합니다. 만점입니다!\n (총 소요시간 {'%.2f'%(self.end_time - self.start_time)} 초)",foreground="green")
        elif self.score == 0:
            self.label_result.config(text=f"모두 틀렸습니다 :(\n (총 소요시간 {'%.2f'%(self.end_time - self.start_time)} 초)",foreground="red")
        else:
            self.label_result.config(text=f"5문제에서 {self.score}문제 맞혔습니다.\n (총 소요시간 {'%.2f'%(self.end_time - self.start_time)} 초)",foreground="green")

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("GUGUDAN Timeattack")
        self.master.geometry("300x320")
        
        self.score = 0
        self.num1 = 0
        self.num2 = 0
        self.end_time = 0
        self.best_score = self.load_best_score()

        self.label_question = ttk.Label(master, text="", font=("맑은 고딕", 15, "bold"))
        self.label_question.pack(pady=10)

        self.entry_answer = ttk.Entry(master)
        self.entry_answer.pack(pady=5)
        self.entry_answer.bind('<Return>', self.check_answer_enter)

        self.label_result = ttk.Label(master, text="", font=("맑은 고딕", 15, "bold"))
        self.label_result.pack(pady=5)

        self.label_score_title = ttk.Label(master, text="Score:", font=("맑은 고딕", 15, "bold"))
        self.label_score_title.pack()

        self.label_score = ttk.Label(master, text="0", font=("맑은 고딕", 15, "bold"))
        self.label_score.pack()

        self.label_best_score_title = ttk.Label(master, text="Best Score:", font=("맑은 고딕", 15, "bold"))
        self.label_best_score_title.pack()

        self.label_best_score = ttk.Label(master, text=str(self.best_score), font=("맑은 고딕", 15, "bold"))
        self.label_best_score.pack()

        self.label_time_title = ttk.Label(master, text="Time left:", font=("맑은 고딕", 15, "bold"))
        self.label_time_title.pack()

        self.label_time = ttk.Label(master, text="30", font=("맑은 고딕", 15, "bold"))
        self.label_time.pack()

        self.start_game()

    def start_game(self):  # 게임 시작
        self.score = 0
        self.end_time = time.time() + 30
        self.entry_answer.configure(state="normal")
        self.update_time()
        self.generate_question()
        self.countdown()

    def generate_question(self):
        self.num1 = random.randint(2, 9)
        self.num2 = random.randint(2, 9)
        self.label_question.config(text=f"{self.num1} X {self.num2}=?") # 질문 라벨 config

    def check_answer_enter(self, event):  # enter 체크
        self.check_answer()

    def check_answer(self):
        user_answer = self.entry_answer.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == self.num1 * self.num2:
                self.score += 1
                self.label_result.config(text="Correct!", foreground="green") # 맞았으면
            else:
                self.label_result.config(text="Wrong!", foreground="red") # 틀렸으면
        else:
            self.label_result.config(text="정수를 입력해 주세요.", foreground="blue") # 정수 입력이 아니라면
        self.entry_answer.delete(0, tk.END) # 답 입력창 삭제
        self.update_score() # 스코어 업데이트
        self.generate_question() # 문제 재생성

    def update_score(self):
        self.label_score.config(text=str(self.score))
        if self.score > self.best_score: #최고기록 갱신
            self.label_best_score.config(text=str(self.score))
            self.save_best_score(self.score)

    def update_time(self):
        remaining_time = int(self.end_time - time.time()) # 남은 시간 체크
        if remaining_time >= 0:
            self.label_time.config(text=str(remaining_time)) # 출력
        else:
            self.label_time.config(text="0")
            self.entry_answer.configure(state="disabled")

    def countdown(self): # 카운트다운
        self.update_time()
        if time.time() < self.end_time:
            self.master.after(1000, self.countdown)
        else:
            self.end_game()

    def end_game(self): # 종료
        self.entry_answer.config(state="disabled")
        self.entry_answer.unbind('<Return>')
        if self.score > self.best_score:
            self.label_result.config(text=f"New Record! You got {self.score} points!",foreground="green")
        else:
            self.label_result.config(text=f"Time Over! You got {self.score} points!",foreground="red")

    def load_best_score(self):
        try:
            with open("best_score.txt", "r") as file: #자동으로 닫게 with
                content = file.read().strip()
                if content:
                    return int(content)
                else:
                    return 0
        except (FileNotFoundError, ValueError): #파일 없거나 값오류나면 0으로 리턴
            return 0

    def save_best_score(self, best_score):
        with open("best_score.txt", "w") as file:
            file.write(str(best_score))
                
class RainingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("GUGUDAN is Raining!!")
        self.canvas = tk.Canvas(root, width=400, height=600)
        self.canvas.pack()

        self.score = 0
        self.best_score = self.load_best_score()  # 최고 기록 로드
        self.problems = []
        self.problem_speed = 500    
        self.create_problem_frequency = 1000

        self.create_problem_id = None
        self.update_game_id = None

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", self.check_answer)

        self.score_label = tk.Label(root, text="Score: 0", font=("맑은 고딕", 15, "bold"))
        self.score_label.pack()

        self.best_score_label = tk.Label(root, text=f"Best Score: {self.best_score}", font=("맑은 고딕", 15, "bold"))
        self.best_score_label.pack()

        self.create_problem()
        self.update_game()

    def create_problem(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        problem = {"text": f"{x} * {y} = ?", "answer": x * y, "y_pos": 0} #문제 맨위에 만들기
        self.problems.append(problem)
        self.create_problem_id = self.root.after(self.create_problem_frequency, self.create_problem)

    def update_game(self):
        self.canvas.delete("all")

        if self.score > self.best_score: #최고기록 업데이트
            self.save_best_score(self.score)
            self.best_score_label.config(text=f"Best Score: {self.score}")

        for problem in self.problems:
            self.canvas.create_text(200, problem["y_pos"], text=problem["text"], font=("맑은 고딕", 24, "bold"))
            problem["y_pos"] += 20

        if any(problem["y_pos"] >= 590 for problem in self.problems):
            self.game_over()
        else:
            self.update_game_id = self.root.after(self.problem_speed, self.update_game)

    def check_answer(self, event):
        user_answer = self.answer_entry.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            for problem in self.problems:
                if user_answer == problem["answer"]:
                    self.problems.remove(problem)
                    self.score += 1
                    self.score_label.config(text=f"Score: {self.score}")
                    break
        self.answer_entry.delete(0, tk.END)

    def game_over(self):
        if self.score > self.best_score:
            self.canvas.create_text(200, 300, text="New Record!", font=("맑은 고딕", 30, "bold"), fill="green")
            self.canvas.create_text(200, 350, text=f"Final Score: {self.score}", font=("맑은 고딕", 30, "bold"), fill="green")
        else:
            self.canvas.create_text(200, 300, text="GAME OVER", font=("맑은 고딕", 30, "bold"), fill="red")
            self.canvas.create_text(200, 350, text=f"Final Score: {self.score}", font=("맑은 고딕", 30, "bold"), fill="red")
        self.answer_entry.config(state='disabled')
        self.answer_entry.unbind('<Return>')
        self.root.after_cancel(self.update_game_id)
        self.root.after_cancel(self.create_problem_id)

    def load_best_score(self):
        try:
            with open("best_score_raining.txt", "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def save_best_score(self, best_score):
        with open("best_score_raining.txt", "w") as file:
            file.write(str(best_score))

def open_basic_game():
    win.withdraw() #윈도우 숨기고 탑레벨적용

    basic_game_win = Toplevel(win)
    gugudanbasic(basic_game_win)

    def on_close():
        basic_game_win.destroy()
        win.deiconify() # 구구단 창 복원

    basic_game_win.protocol("WM_DELETE_WINDOW", on_close) #지우면 닫은걸로

def open_time_attack():
    win.withdraw()

    time_attack_win = Toplevel(win)

    quiz_game = QuizGame(time_attack_win)
    quiz_game.start_game()  # 퀴즈 게임 시작 메서드 호출

    def on_close():
        time_attack_win.destroy()
        win.deiconify()  # 이전 윈도우(구구단) 복원

    time_attack_win.protocol("WM_DELETE_WINDOW", on_close) #창 닫아도 닫은걸로 인식

def open_raining_game():
    win.withdraw()

    raining_game_win = Toplevel(win)

    RainingGame(raining_game_win)

    def on_close():
        raining_game_win.destroy()
        win.deiconify()  # 이전 윈도우(구구단) 복원

    raining_game_win.protocol("WM_DELETE_WINDOW", on_close)  # 창 닫아도 닫은걸로 인식

def open_gugudan():
    global win
    win = tk.Tk()
    win.title("GUGUDAN")

    win.geometry("350x150")  # 창 크기 조정

    ggd = Label(win, text="구구단 게임",font=("맑은 고딕", 20, "bold"))
    ggd.pack(side="top", pady=10)

    button_frame = tk.Frame(win)
    button_frame.pack(pady=20)
    
    ttk.Button(button_frame, text="기본 게임", command=open_basic_game, width=10).pack(side="left", padx=10)
    ttk.Button(button_frame, text="타임어택", command=open_time_attack, width=10).pack(side="left", padx=10)
    ttk.Button(button_frame, text="산성비 게임", command=open_raining_game, width=10).pack(side="left", padx=10)

    win.mainloop()

USER_FILE = 'loginfile.txt'

def load_users(): # 파일에서 유저들 목록 가져와서 딕셔너리로 정렬
    users = {}
    with open(USER_FILE, 'r') as file: # 끝나면 파일 자동으로 닫아줌
        for line in file:
            username, password = line.strip().split(':') #나눠서 딕셔너리로 정렬
            users[username] = password #ex){erica:2024}

    return users

def save_users(users):# 파일에 사용자 정보 저장
    with open(USER_FILE, 'w') as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")#아이디:비번 형태로 저장

def check_data(event=None): # 로그인 확인
    users = load_users()
    if user_id.get() in users and users[user_id.get()] == password.get():
        message_label.config(text="Logged IN Successfully", foreground="green")
        lgin.withdraw()  # 숨기기
        open_gugudan()   # 구구단 메인창 오픈
    else:
        message_label.config(text="Check your Username/Password", foreground="red")

def register(): # 회원가입
    def save_new_user(event=None):
        users = load_users()
        username = new_user_id.get().strip()
        password = new_password.get().strip()

        if not username or not password: #가입시에 아이디 비번 입력못받았으면
            reg_message_label.config(text="Username and Password are required", foreground="red")
        elif username in users: #이미 아이디 있으면
            reg_message_label.config(text="Username already exists", foreground="red")
        else:
            users[username] = password
            save_users(users)
            reg_message_label.config(text="Registration Successful", foreground="green")
            register_win.destroy()

    register_win = tk.Toplevel() #탑레벨 이용해서 로그인창 위에 회원가입 창 생성
    register_win.title("Register")

    new_user_id, new_password = StringVar(), StringVar()

    ttk.Label(register_win, text="New Username: ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(register_win, text="New Password: ").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(register_win, textvariable=new_user_id).grid(row=0, column=1, padx=10, pady=10)
    ttk.Entry(register_win, textvariable=new_password, show="*").grid(row=1, column=1, padx=10, pady=10)
    ttk.Button(register_win, text="Register", command=save_new_user).grid(row=2, column=1, padx=10, pady=10)

    reg_message_label = Label(register_win, text="")
    reg_message_label.grid(row=3, column=0, columnspan=2)
    register_win.bind('<Return>', save_new_user)

def main():
    global lgin, user_id, password, message_label

    lgin = tk.Tk()
    lgin.title("LOGIN")

    user_id, password = StringVar(), StringVar()

    ttk.Label(lgin, text="Username: ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(lgin, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(lgin, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
    ttk.Entry(lgin, textvariable=password, show="*").grid(row=1, column=1, padx=10, pady=10)
    ttk.Button(lgin, text="Login", command=check_data).grid(row=2, column=1, padx=10, pady=10)
    ttk.Button(lgin, text="Register", command=register).grid(row=2, column=0, padx=10, pady=10)

    message_label = Label(lgin, text="")
    message_label.grid(row=3, column=0, columnspan=2)

    lgin.bind('<Return>', check_data)  # Enter 입력 시 check_data 함수 이동
    lgin.mainloop()

if __name__ == "__main__":
    main()