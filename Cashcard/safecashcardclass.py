# -*-coding:utf8
from cashcardclass import simplecashcard as cashcard

#simplecashcard 클래스를 상속받아 safecashcard 클래스를 정의한다
class safecashcard(cashcard):
    #withdraw만 재정의
    def withdraw(self, amount_won):
        print("SafeCashCard withdraw()")
        if self.check_balance() >= amount_won:
            cashcard.withdraw(self,amount_won)
        else:
            print ("**오류 발생**")
            print ("잔고가 부족합니다")
            print ("인출되지 않았습니다")
#safecashcard 정의 끝

if "__main__"==__name__:
    from cashcard_user import chk_bal

    mycard = cashcard()
    mysafecard=safecashcard()
    #여러장 생성가능한지 확인
    mysisterssafecard = safecashcard()
    #각각만원씩 입금
    mycard.deposit(10000)
    mysafecard.deposit(10000)
    mysisterssafecard.deposit(10000)

    chk_bal("myCard 입금후 잔고확인",mycard)
    chk_bal("mysafecard 입금후 잔고확인", mysafecard)
    chk_bal("mysisterssafecard 입금후 잔고확인",mysisterssafecard)

    #십만원 출금
    mycard.withdraw(100000)
    mysafecard.withdraw(100000)
    mysisterssafecard.withdraw(100000)

    chk_bal("myCard 출금후 잔고확인",mycard)
    chk_bal("mysafecard 출금후 잔고확인", mysafecard)
    chk_bal("mysisterssafecard 출금후 잔고확인",mysisterssafecard)