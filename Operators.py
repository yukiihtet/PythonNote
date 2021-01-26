Operators
Python မှာ Operators တွေကို အကြမ်းအားဖြင့် ၇ မျိုးခွဲလို့ရတယ်။

No.	Types
1	Arithmetic operators
2	Assignment operators
3	Comparison operators
4	Logical operators
5	Identity operators
6	Membership operators
7	Bitwise operators
Reference from W3School


Arithmetic Operators
Example 1 (ပေါင်း။ နှုတ်၊ မြှောက်၊ စား)
a = 6
b = 3

print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)
Output:
a + b = 9
a - b = 3
a * b = 18
a / b = 2.0
Example 2 (Modulus)
a = 15
b = 10
print(a%b)
Output:
5
Example 3 (Exponentiation)(Power)
a = 2
b = 5
print(a**b)
Output:
32
Example 4 (Floor division)
a = 20
b = 3
print(a//b)
Output:
6
Note: a//b သည် int(a/b) နဲ့တူ


Assignment operators
Example 5
a = 10
print(a)
Output:
10
= ကိုပဲ Arithmetic Operators(+, -, *, /, %, **, //) တွေနဲ့ တွဲသုံးလို့ရတယ်

Example 6
a = 6
a += 3
print(a)
Output:
9
a += 3 သည် a = a + 3 နဲ့တူ

Example 7
a = 6
a -= 2
print(a)
Output:
4
Example 8
a = 6
a *= 3
print(a)
Output:
18
Example 9
a = 15
a /= 5
print(a)
Output:
3.0
Example 10
a = 13
a %= 5
print(a)
Output:
3
Example 11
a = 2
a **= 4
print(a)
Output:
16
Example 12
a = 13
a //= 3
print(a)
Output:
4
နောက်တမျိုးက Bitwise Operators နဲ့ တွဲပြီးသုံးလို့ရပါတယ်

Bitwise Operators အကြောင်းကိုတော့ အောက်မှာ ဆက်ရှင်းပြပါမယ်

Example 13 (AND)
a = 4
a &= 5
print(a)
Output:
4
Example 14 (OR)
a = 2
a |= 3
print(a)
Output:
3
Example 15 (XOR)
a = 6
a ^= 4
print(a)
Output:
2
Example 16 (Right Shift)
a = 7
a >>= 2
print(a)
Output:
1
Example 17 (Left Shift)
a = 3
a <<= 2
print(a)
Output:
12

Comparison operators
Boolean value ထွက်တယ်

Example 18 (Equal)
a = 5
b = 5
print(a==b)
Output:
True
Example 19 (Not Equal)
a = 5
b = 6
print(a!=b)
Output:
True
Example 20 (Greater than)
a = 100
b = 10
print(a>b)
Output:
True
Example 21 (Less than)
a = 100
b = 10
print(a<b)
Output:
False
Example 22 (Greater than or equal)
a = 100
b = 100
print(a>b)
print(a>=b)
Output:
False
True
Example 23 (Less than or equal)
a = 10
b = 100
print(a<=b)
Output:
True

Logical operators
Comparison Operators တွေနဲ့ တွဲသုံးလေ့ရှိတယ်

တနည်းအားဖြင့် Boolean values တွေနဲ့ အလုပ်လုပ်တယ်

Example 24 (and)
Condition နှစ်ခုစလုံးမှန်မှ True ဖြစ်မယ်

x = 5

print(x>0 and x<10)
print(x>8 and x<10)
Output:
True
False
Example 25 (or)
Condition တစ်ခု မှန်တာနဲ့ True ဖြစ်မယ်

name = "owl"

print(name=="logix" or name=="owl")
print(name=="logix" or name=="zeegwat")
Output:
True
Example 26 (not)
ပြောင်းပြန်ပြောင်းတာ (True ဆို False ဖြစ်မယ်)( False ဆို True ဖြစ်မယ်)

x = 10
print(not (x==10))
Output:
False

Identity operators
Example 27 (is)
is ကို == နဲ့မှားတတ်ပါတယ်။ သူတို့က တူသယောင်နဲ့ မတူကြပါဘူး။

is က same object, same memory location ဖြစ်မှသာ True ဖြစ်တာပါ။

obj1 = ['mgmg','mama']
obj2 = ['mgmg','mama']

obj3 = obj1

print(obj3 is obj1)
print(obj1 is obj2)
print(obj1 == obj2)
Output:
True
False
True
Example 28 (is not)
obj1 = ['mgmg','mama']
obj2 = ['mgmg','mama']

obj3 = obj1

print(obj1 is not obj2)
print(obj3 is not obj1)
Output:
True
False

Membership operators
Example 29 (in)
Sequence တစ်ခုက object တစ်ခုမှာပါနေလား ဆိုတာကို စစ်တာ

text = "A quick brown fox jumps over the lazy dog"

print("dog" in text)
print("owl" in text)
Output:
True
False
Example 30 (not in)
myobj = ['red','green','blue']

print("yellow" not in myobj)
print("red" not in myobj)
Output:
True
False

Bitwise operators
Bitwise Operators တွေက Numbers တွေရဲ့ binary values တွေနဲ့ အလုပ်လုပ်တယ်

Example 31 (AND)
print(4 & 5)
Output:
4
Explanation
4 ရဲ့ binary value က 1 0 0
5 ရဲ့ binary value က 1 0 1

သူတို့ကို AND လုပ်တဲ့ အခါ (1 နဲ့ 1 ဆိုရင် 1, တခြားဟာတွေဆိုရင် 0)

 1 0 0
 1 0 1
-------
 1 0 0 ရတယ်

1 0 0 က 4

Example 32 (OR)
print(2 | 3)
Output:
3
Explanation
2 ရဲ့ binary value က 1 0
3 ရဲ့ binary value က 1 1

သူတို့ကို OR လုပ်တဲ့ အခါ (1 တစ်လုံးပါတာနဲ့ 1, ကျန်တာ 0)

 1 0
 1 1
-----
 1 1 ရတယ်

1 1 က 3

Example 33 (XOR)
print(6 ^ 4)
Output:
2
Explanation
6 ရဲ့ binary value က 1 1 0
4 ရဲ့ binary value က 1 0 0

သူတို့ကို XOR လုပ်တဲ့ အခါ (တူရင် 0, မတူရင် 1)

 1 1 0
 1 0 0
-------
 0 1 0 ရတယ်

1 0 က 2

Example 34 (NOT)
print(~4)
Output:
-5
Explanation
4 ရဲ့ binary value က 1 0 0

  ~ ( 1 0 0 )
= - ( 1 0 0 + 1 )
= - ( 1 0 1 )

- 1 0 1 က -5

Example 35 (Right Shift)
print(7 >> 2)
Output:
1
Explanation
7 ရဲ့ binary value က 1 1 1

Right Shift ကို ၂ ခါ လုပ်တဲ့အခါ 1 1 1 သည် ညာဖက် ၂ လုံးရွေ့သွားမယ်။

 1 1 1 (origin)
 0 1 1 (1 shifted)
 0 0 1 (2 shifted)

001 က 1

Example 36 (Left Shift)
print(3 << 2)
Output:
12
Explanation
3 ရဲ့ binary value က 1 1

Left Shift ကို ၂ ခါ လုပ်တဲ့အခါ 1 1 သည် ဘယ်ဖက် ၂ လုံးရွေ့သွားမယ်။

     1 1 (origin)
   1 1 0 (1 shifted)
 1 1 0 0 (2 shifted)

1100 က 12
Next (Numeric Functions)