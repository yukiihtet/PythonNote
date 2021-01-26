Conditions
IF Statement
IF statement

Condition Statements တွေကို Comparison operators တွေနဲ့ တွဲသုံးလေ့ရှိတယ်

Example 1 (if)
a = 5
b = 5
c = 10

if a==b:
	print('a and b are same')
	
if a==c:
	print('a and c are same')
Output:
a and b are same
Example 2 (if ... else)
a = 5
b = 5
c = 10

if a==b:
	print('a and b are same')
else:
	print('a and b are not same')

if a==c:
	print('a and c are same')
else:
	print('a and c are not same')
Output:
a and b are same
a and c are not same
Example 3 (if ... elif ... else)
num = 1

if num > 0:
	print('Positive')
elif num < 0:
	print('Negative')
else:
	print('Zero')
Output:
Positive
Example 4 (sample program)
num = int(input('Enter a number: '))

if num > 0:
	print('Positive')
elif num < 0:
	print('Negative')
else:
	print('Zero')
Output 1:
Enter a number: 10
Positive
Output 2:
Enter a number: -2
Negative
Output 3:
Enter a number: 0
Zero

Example 5 (Even? or Odd?)
num = int(input('Enter a number: '))

if num%2 == 0:
	print('Even')
else:
	print('Odd')
Output 1:
Enter a number: 3
Odd
Output 2:
Enter a number: 4
Even

Example 6 (Calculator program)
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
operator = input('Enter a operator (+,-,*,/): ')

ans = 0

if operator == '+':
	ans = a + b
elif operator == '-':
	ans = a - b
elif operator == '*':
	ans = a * b
elif operator == '/':
	ans = a / b
else:
	ans = "Invalid operator"

print(str(a) + operator + str(b) + '=' + str(ans))
Output 1:
Enter first number: 3
Enter second number: 5
Enter a operator (+,-,*,/): +
3+5=8
Output 2:
Enter first number: 10
Enter second number: 3
Enter a operator (+,-,*,/): -
10-3=7
Output 3:
Enter first number: 10
Enter second number: 5
Enter a operator (+,-,*,/): /
10/5=2.0
Output 4:
Enter first number: 4
Enter second number: 9
Enter a operator (+,-,*,/): #
4#9=Invalid operator
Next (Loops)