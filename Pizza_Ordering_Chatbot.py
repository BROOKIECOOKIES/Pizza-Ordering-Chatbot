print('Hello, my name is Alex your virtual assistant. I will help you order a pizza!')
print('I am going to ask you a few questions. After typing an answer, press enter.')
print('\n')
userName = input ('Enter your name: Brooke ')
print('\n')
print('Hello, Brooke '+ userName +'. Nice to meet you!')
print('\n')
size = input('\nWhat size do pizza do you want? Enter small, medium, or large: ')
flavor = input('\nEnter the flavor of the pizza: ')
crustType = input('\nWhat type of crust do you want: ')
quantity = input('\nHow many of these do you want to order? Enter a numerical value:')
quantity = int(quantity)
method = input('\nIs this carry out or delivery: ')
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print('\n----------------')
print('Thank you, Brooke' , userName, ', for your order.')
print(' Your', quantity, size, flavor, 'pizza with' , crustType, 'crust costs','$($36.99)' .format(total) +'.')
print('\n----------------')

