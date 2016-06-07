# -*- coding:utf8
class simplecashcard:

    def __init__(self):
        print "SimpleCashCard __init__()" #함수 호출 표식
        #클래스 생성자 (컨스터럭터)
        #멤버 변수 초기화
        #각 카드 별로 따로 잔고를 기록
        self.balance_won = 0

    def deposit(self, amount_won):
        print "SimpleCashCard deposit()"
        self.balance_won += amount_won

    def withdraw(self, amount_won):
        print "SimpleCashCard withdraw()"
        self.balance_won += (-amount_won)

    def check_balance(self):
        print "SimpleCashCard check_balance()"
        return self.balance_won
#simplecashcard 클래스 정의 끝
#아래 내용은 import 될때는 실행되지않음
if "__main__"==__name__:
    from cashcard_user import chk_bal

    # mycard 객체를 simplecashcard클래스에 정한대로 만듬
    mycard = simplecashcard()

    mycard.deposit(10000)
    chk_bal("입금후 잔고 확인", mycard)

    mycard.withdraw(1000)
    chk_bal("출금후 잔고 확인", mycard)

    #카드 여러장만들기
    mysisterscard = simplecashcard()
    chk_bal("잔액 확인 mycard", mycard)
    chk_bal("잔액 확인 mysisterscard", mysisterscard)

    print('mycard: %s' % mycard )
    print('mysisterscard: %s' % mysisterscard )