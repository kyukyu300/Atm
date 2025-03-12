# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료 => 글자를 입력 받을지 / 숫자를 입력 받을지
# 숫자로 원하는 기능을 입력할 수 있게 만들어주세요 그리고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount:

balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해주세요(1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료): ")
    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요: ") # "123131313".isdigit() = True
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f'{deposit_amount}원을 입금하셨습니다. 현재 잔액은 {balance}원 입니다.')
        else:
            print("정신차리고, 제대로 된 숫자 형태로 입금액을 입력하세요.")
    if num == "2":
        print("출금 기능입니다.")
    if num == "3":
        print("영수증 보기 기능입니다.")
    if num == "4":
        print("시스템을 종료합니다.")
        break