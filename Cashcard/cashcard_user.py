# -*- coding:utf8
import cashcard as cashcard_module

def chk_bal(message, account):
    print("%s : %d" % (message, account.check_balance()))

# 아래의 내용은 이 .py 파일이 import 될 때는 실행되지않음

if '__main__' ==__name__:
    #잔액확인
    chk_bal("CashCard_module 잔액확인", cashcard_module)
    #10000원 입금
    print("10000원 입금")

    cashcard_module.deposit(10000)

    chk_bal("입금 후 잔고 확인", cashcard_module)

    print("1000원 출금")
    cashcard_module.withdraw(1000)

    chk_bal("출금 후 잔고 확인", cashcard_module)
    #다른 카드를 만들수 있을까?
    import cashcard as mysisterscard_module

    chk_bal("CashCard_module 잔액확인", cashcard_module)
    chk_bal("mysisterscard_module 잔액확인", mysisterscard_module)

    #그러나 이런 식으로는 한장의 카드만 만들 수 있다
    print("CashCard_module : %s" % cashcard_module)
    print("mysisterscard_module : %s" % mysisterscard_module)