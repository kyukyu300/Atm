# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료 => 글자를 입력 받을지 / 숫자를 입력 받을지
# 숫자로 원하는 기능을 입력할 수 있게 만들어주세요 그리고 사용자가 입력한 기능은 num 변수에 담아주세요


balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해주세요(1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료)")
    if num == "1":
        print("입금 기능입니다.")
    if num == "2":
        print("출금 기능입니다.")
    if num == "3":
        print("영수증 보기 기능입니다.")
    if num == "4":
        print("시스템을 종료합니다.")
        break