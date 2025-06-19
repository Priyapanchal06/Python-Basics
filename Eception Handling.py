try:
    num=(int(input("enter a number:")))
    result=10/num

except ZeroDivisionError:
    print("cant divide by zero.")
except ValueError:
    print("Invalid input!")
else:
    print("Result is :",result)
finally:
    print("Excecution finished")