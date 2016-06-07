# -*- coding:utf8
balance_won =0 #카드잔고
# 입금, 출금, 잔고 확인
def deposit(amount_won):
    global balance_won

    #deposit 함수 안의 balance_won 이
    #전역변수임을 표시

    #입금시 잔고증가
    balance_won += amount_won

def withdraw(amount_won):

    #withdraw 함수 안의 balance_won 이
    #전역변수임을 표시
    global balance_won

    #출금시 잔고감소
    balance_won += (-amount_won)

def check_balance():

    #통장 잔고를 반환한다
    return balance_won


