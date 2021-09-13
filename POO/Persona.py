class Person:
    def __init__(self, name, mobile_phone =None, office_phone= None,
                private_phone = None, email = None) -> None:
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self,number):
        self.mobile_phone = number

    def add_office_phone(self,number):
        self.office = number
    
    def add_private_phone(self,number):
        self.private = number
    
    def add_email(self,email):
        self.email = email

    def dump(self):
        s = self.name + "\n"
        if(self.mobile is not None):
            s += f"Mobile phone: {self.mobile}\n"
        if(self.office is not None):
            s += f"Office phone: {self.office}\n"
        if(self.private is not None):
            s += f"Private phone: {self.private}\n"
        if(self.email is not None):
            s += f"Email: {self.email}\n"
        print(s)