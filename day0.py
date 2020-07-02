
name="rahul"
name2="tridib"

print(name2)
if 2>0:
	print('true')

print(type(name))
print(type(name2))

var1,var2,var3='hello',20,30
print(var1)
print(var2)
print(var3)
x=y=z=3

var1='komal'
print("my name is"+var1)

var2=20
var3=21
text="this is a number that is {} and {}"
print(text.format(var2,var3))

a="global variable"
def func():
	print(a)

print(a)
func()

def func1():
	global ab
	ab="global variable"

func1()
print(ab)


print(id(name2))


def famname():
	anshu=input("what is your bros name?")
	print(anshu)

famname()


def famname1(str):
	print(str)
	return


famname1('harsh')