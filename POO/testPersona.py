from Persona import Person

p1 = Person('Lola Mento', office_phone='555729600',email='1m2021@alumno.ipn.mx')
p2 = Person('Coloso Rodas', office_phone='555729601',email='uwuiwi2021@alumno.ipn.mx')
p3 = Person('Yo mero', office_phone='5557296011')

p3.add_email('AWAewe@alumno.ipn.mx')
phone_book = [p1,p2,p3]

for person in phone_book:
    person.dump()