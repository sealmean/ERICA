# 사용자 정보를 저장할 파일 경로
USER_FILE = 'loginfile.txt'

# 파일에서 사용자 정보를 로드하는 함수
def load_users():
    users = {}
    try:
        with open(USER_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                users[username] = password
    except FileNotFoundError:
        pass
    return users

# 파일에 사용자 정보를 저장하는 함수
def save_users(users):
    with open(USER_FILE, 'w') as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

# 회원가입 함수
def register():
    users = load_users()
    username = input("아이디를 입력하세요: ").strip()
    if username in users:
        print("이미 존재하는 아이디입니다.")
        return

    password = input("비밀번호를 입력하세요: ").strip()
    users[username] = password
    save_users(users)
    print("회원가입이 완료되었습니다.")

# 로그인 함수
def login():
    users = load_users()
    username = input("아이디를 입력하세요: ").strip()
    if username not in users:
        print("존재하지 않는 아이디입니다.")
        return

    password = input("비밀번호를 입력하세요: ").strip()
    if users[username] == password:
        print("로그인에 성공했습니다.")
    else:
        print("비밀번호가 틀렸습니다.")

# 메인 함수
def main():
    while True:
        print("1. 회원가입")
        print("2. 로그인")
        print("3. 종료")
        choice = input("원하는 작업을 선택하세요: ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
