# 1. Handling Zero Division Error:-
try:
    x=10/0
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print(("program ended"))

# 2. Multiple Exceptions:-
try:
    num=int("abc")
    result=10/0
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("done")    

#3.Catch any exception
try:
    f=open ("data.txt")
except Exception as e:
    print("error:",e)
finally:
    print("file handling attempted")
