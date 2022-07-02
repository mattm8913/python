#one.py

#if you type "python one.py" into the CMD line, it sets
# __name__ = "__main__"
"""
# typical structure:

def myfunc():
	pass
def myfunc2():
	pass
def myfunc3():
	pass

if __name__ == "__main__":
	# if being called directly, run this script:
	myfunc()
	myfunc2()
	myfunc3()

"""

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
	print("ONE.PY is being run directly!")
else:
	print("ONE.PY has been imported!")