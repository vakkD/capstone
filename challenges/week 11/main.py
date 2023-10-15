import mobile

phone =mobile.MobilePhone('Acme Electronics', 'M1000', 199.99)

get_input =lambda prompt: (lambda x: x if x else get_input(prompt))(input(prompt))

manufacturer =get_input('Enter the manufacturer: ')
phone.set_manufact(manufacturer)

model =get_input('Enter the model number: ')
phone.set_model(model)

price =get_input('Enter the retail price: ')
while not price.replace('.', '', 1).isdigit() or float(price)<0:
    print('Please enter a valid non-negative number for price.')
    price =get_input('Enter the retail price: ')
phone.set_retail_price(float(price))

print('\nHere is the data that you entered:')
print('Manufacturer:', phone.get_manufact())
print('Model Number:', phone.get_model())
print(f'Retail Price: ${phone.get_retail_price():,.2f}')