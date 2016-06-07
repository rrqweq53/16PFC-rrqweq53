# -*- coding:utf8
from safecashcardclass import safecashcard
#입출금 시간을 기록하기 위해 time 모듈을 도입
import time

class Historycashcard(safecashcard):
    """
    cash card capable of recording histories
    """ # <-docstring

    def __init__(self):
        print "Historycashcard __init__()"
        # Historycashcard 클래스의 객체는 사용 내역을 담음
        # 별도의 멤버 변수가 필요함 이변수를 준비하려면
        # Historycashcard 클래스의 생성자가 필요함

        # 상위 클래스인 Safecashcard의 생성자를 먼저 호출
        safecashcard.__init__(self)
        # super(Historycashcard.self).__init__() 도 가능할수 있음

        # 입출금 내역을 기록하기 위한 리스트 준비
        self.history = []

    #기록 기능추가를위해 재정의
    def deposit(self, amount_won):
        """
        Historycashcard deposit method
        deposit amount & add record to history
        """ #
        print "Historycashcard deposit()"
        #입금 가능 자체는 이미정해진바를 따름
        safecashcard.deposit(self, amount_won)

        #입금 내역을 기록
        self.record_history('deposit', amount_won)

    def withdraw(self, amount_won):
        """
         Historycashcard withdraw method
         withdraw amount&add record to history
        """ #
        print "Historycashcard withdraw()"
        safecashcard.withdraw(self, amount_won)
        #출금 내역을 기록
        self.record_history('withdraw', amount_won)
    def record_history(self, activity, amount_won):
        record = {
            'time':time.localtime(),
            'balance':self.check_balance(),
            'activity': activity,
            'amount': amount_won,
        }
        self.history.append(record)

    def show_history(self):
        """
         Historycashcard show_history method
         show appended history
        """ #
        print "Historycashcard show_history()"
        #사용내역을 출력
        print ('%25s %10s %10s %10s' %(
            'time and date', 'activity', 'amount', 'balance'))
        for record in self.history:
            print('%25s %10s %10d %10d' %
                  (ti
                   record['activity'], record['amount'], record['balance']))

if "__main__"==__name__:
    print("main 객체 생성".ljust(60, '*'))
    myhistcard = Historycashcard()
    print("main 10000원 입금".ljust(60, '*'))
    myhistcard.deposit(10000)
    print("main 9000원 출금".ljust(60, '*'))
    myhistcard.withdraw(9000)
    print("main 9000원 출금".ljust(60, '*'))
    myhistcard.withdraw(9000) #오류 발생할것임
    print("main 내역 확인".ljust(60, '*'))
    myhistcard.show_history()
    print("main 끝".ljust(60, '*'))