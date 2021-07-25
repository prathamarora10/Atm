class Atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def cashWithDrawl(self):
        print('Draw Cash from bank !!')

    def balanceEnquiry(self):
        print('A Balance Enquiry Will Be Held on 30th of July !!')

person = Atm(1234567890, 2008)

person.cashWithDrawl()
person.balanceEnquiry()