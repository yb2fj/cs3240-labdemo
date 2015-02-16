__author__ = 'yb2fj'


def greeting(msg):
    print(msg)


def appreciation(msg):
    print(msg + ", Thank you")


def test_greeting():
    msg = "Thank you"
    greeting(msg)


def main():
    test_greeting()

if __name__=='__main__':
    main()