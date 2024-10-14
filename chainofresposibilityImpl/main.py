from checker import NameTrueStatusTrue, NameTrueStatusFalse, NameFalseStatusFalse, NameFalseStatusEmpty, NameStatusHandler
from bearer_token import BearerToken

class Main:
    def setup(self):
        handler1 = NameTrueStatusTrue()
        handler2 = NameTrueStatusFalse()
        handler3 = NameFalseStatusFalse()
        handler4 = NameFalseStatusEmpty()

        handler1.set_next(handler2).set_next(handler3).set_next(handler4)

        __header, __payload, __signature = input("Enter the token: ").split('.')

        b = BearerToken(__header, __payload, __signature)

        if b.verify_signature():
            payload_dict = b.decode_payload()
            name = payload_dict.get('name')
            status = payload_dict.get('status')
            print(name)
            print(status)
            handler1.handle(name, status)

if __name__ == '__main__':
    main = Main()
    main.setup()


"""
case1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlN1amkiLCJzdGF0dXMiOiJhY3RpdmUifQ.zSFflmX7TTt9_LOcfPtMpM19fHOuNpcTzDVbwFvn1xg
case2: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsd2luIiwic3RhdHVzIjoiaW5hY3RpdmUifQ.CXTqWjAR4xFrnNuhox3IKR_OU6-FN7yc8YVpDmls13o
case3: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ik1hbnUiLCJzdGF0dXMiOiJpbmFjdGl2ZSJ9.AbHt-i9ByuYqWogjzyFeB9vx0FULEcWSM-nzWc1QMsk
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuanUiLCJzdGF0dXMiOiJhY3RpdmUifQ.8p2dNhmzlh8CHD-3R5HHp7Wmt1umJQvRDftMVBpcDlQ

case4: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuanUiLCJzdGF0dXMiOiIifQ.Pug_zSgTFbHEEvms6XQSW-xSHSgpKbPKeXqBrAElROA

"""