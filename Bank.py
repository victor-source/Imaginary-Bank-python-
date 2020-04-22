import random
profile=[]
bankName=('webminizer PLC')
print (f'welcome to {bankName} press o to (o)pen an account and q to (q)uit')
user_input=input('')
if user_input=='o':
	print('pls fill the form below \n')
	name=input('what is your name:--  ')
	date_of_birth=(input(f'{name} when were you born:--  '))
	phone_number=(input('Enter your phone number'))
	total=10
	number="".join(random.sample(phone_number,total))
	profile.append(name)
	profile.append(date_of_birth)
	profile.append(phone_number)
	profile.append(number)
	user_input= (input('your account is ready!! type l to login to your account and \'q\' to (q)uit. '))
	if user_input == 'l':
		input=input('enter your account number: \n')
		if input == (profile[3]):
			print(f'===={bank name}====\n')
			print (f'your details are :\n Name:  {profile[0]} \n date of birth:{profile[1]} \n Phone number:{profile[2]} \n Account number: {profile[3]}')
		else:
			print('wrong number combination!!')
	elif user_input == q:
		print ('ended')