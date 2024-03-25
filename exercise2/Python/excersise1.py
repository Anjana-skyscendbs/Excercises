# todo 1. Create a Integer Variable and convert it to Float, Boolean, String.
   #    todo  **** integer variable ****
# a =10
# x=float(a)
# y=bool(a)
# z=str(a)
#
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))

# todo 2. Create a Float Variable and convert it to Integer, Boolean and String.
   #   todo ****  float variable  ****
# a = 10.3

# x=int(a)
# y=bool(a)
# z=str(a)
#
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))

# todo 3. Create a Boolean Variable and convert it to Integer, Float and String.
    #   todo **** boolean variable ****
# a = True
#
# x=float(a)
# y=int(a)
# z=str(a)
#
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))


# todo 4. Create a String Variable and convert it to Integer, Float and Boolean
    #   todo **** string variable ****
#a = "anjana"

#x=float(a)
#y=bool(a)
#z=int(a)

#print(x,type(x))# ERROR ValueError: could not convert string to float: 'anjana'
#print(y,type(y))
#print(z,type(z))# ERROR ValueError: invalid literal for int() with base 10: 'anjana'

#  todo 5. Find out values in String, Integer and Float when converting to Boolean it gives False

# a = "anjana"
# b = 10
# c = 10.4
#  ALL ARE TRUE
# print(bool(a))
# print(bool(b))
# print(bool(c))


# print(bool(""))       # False
# print(bool("   "))     # False
# print(bool("False"))   # True (as a string)
# print(bool(0))         # False
# print(bool(0.0))       # False


# todo 6. Perform operations with all the Arithmetic Operators

# x = 10
# y = 20
# print(x + y)
# print( x - y)
# print( x * y)
# print( x / y)
# print(x % y)
# print( x ** y)
# print( x // y)


# todo  7. Perform operations with all the Bitwise Operators
#
# x = 6
# y = 3
# print(x & y)#2
# print(x  | y) # 7
# print(x ^ y)# 5
# print(x << y) # 48
# print(x >> y) # 0


# todo 8. Perform operations with all the Relational Operators

# x = 10
# y = 20
# z = 30
# a = 30
#
# if x <= y:
#     print("x is less than equals to y")
# if x >= y:
#     print("x is greater than equals to y")
# if z == a:
#     print("z and a are equals ")
# if x != y:
#     print("x is not equals to y")
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than equals")

# todo 9. Perform operations with all the Logical Operators

# x = 20
# y = 10
#
# print(x > y and y < x)
# print(x > y or x < y )
# print(not(x < y  and x > y))

# todo 10. Create a python script/program that will take input from the user for 3 numbers
# todo and result will print the biggest number and the smallest number using 'input' and 'print'.

# numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(3)]
#
# max_num = numbers[0]
# min_num = numbers[0]
#
# for num in numbers:
#     if num > max_num:
#         max_num = num
#     elif num < min_num:
#         min_num = num
#
# print("The biggest number is:", max_num)
# print("The smallest number is:", min_num)


# todo 11. Create another script/program using 'input' and pass all the three parameters as a
# todo single input and execute the same program as mentioned above.

# user_input = input("Enter three numbers separated by spaces: ")
# numbers = [float(num) for num in user_input.split()]
#
# numbers.sort()
#
# print("The biggest number is:", numbers[-1])
# print("The smallest number is:", numbers[0])


# todo 12. Print odd numbers between 1 to 10 in reverse order using while.


# num = 10
# while num >= 1:
#     if num % 2 != 0:
#         print(num)
#     num -= 1


# todo 13. Perform the same operation with for loop.


# for i in range (1,11):
#     if i % 2 != 0:
#         print(i)
#     i -=1

# for num in range(10, 0, -1):
#     if num % 2 != 0:
#         print(num)


# todo 14. Print odd numbers between 1 to 10 using continue in both for and while loop.

# for i in range (1,11):
#     if i % 2 != 0:
#         print(i)

#  While Loop
# num = 1
# while num <= 9 and num % 2 != 0:
#     print(num)
#     num += 2


#  todo 15. Take 10 numbers in a list(array) and print only first 3 numbers using loop.

# l =[4,5,6,1,2,3,7,8,9,10]
# print(l[0:3])

# todo 16. Create a function which will not take any argument but will print numbers from 1 to 10.

# def my_fun():
#     for i in range(1,11):
#         print(i)
# my_fun()


#  todo 17. Create a function which will take 4 arguments where 2 wil be mandatory and 2keyword arguments.

# def operations(a ,b, x=None,y=5):
#     if x is None and y is  5:
#         #  todo Perform multipication if 2 values are passed.
#         result = a * b
#         print("Multiplication result:", result)
#     elif x is not 10 and y is 5:
#         # # todo Perform addition if 3 are passed.
#         result = a +  b  + x
#         print("Addition result:", result)
#     elif x is not 10 and y is not 5:
#         # todo Perform addition of 1 st two operands and 2nd two operands
#         add_res = a + b + x
#         sub_res = x - y
#         print("Addition result (1st two operands):", add_res)
#         print("Subtraction result (2nd two operands):", sub_res)
#     else:
#         print("Invalid number of arguments")
#
# # and then do a subtraction if 4 arguments are passed.
# operations(2, 3)            # Multiplication
# operations(2, 3, x=4)       # Addition
# operations(2, 3,x=4, y=1)  # Addition and Subtraction


# todo 18. Create a function that will take unlimited arguments and should add all then arguments which are passed.

# def add_all(*args):
#     total = sum(args)
#     return total
# res1 = add_all(1, 2, 3, 4, 5)
# res2 = add_all(10, 20, 30, 40, 50)
# print("Result 1:", res1)
# print("Result 2:", res2)


# todo 19. Create a function which will take unlimited arguments both non keyword and  keyword arguments.
# todo Add the values of all non keyword arguments and also the value of keyword arguments.

# def all_values(*args, **kwargs):
#     non_keyword_sum = sum(args)
#     keyword_sum = sum(kwargs.values())
#
#     total_sum = non_keyword_sum + keyword_sum
#     return total_sum
#
# res1= all_values(11, 22, 33, a=44, b=55)
# res2 = all_values(15, 450, c=0, d=74, e=50)
#
# print("Result 1:", res1)
# print("Result 2:", res2)

# todo 20.Write a function with recursion to give the power of a number.
# todo It will be having two parameters no and power.
# todo If no power is passed it should take 0.


# def pow_no(no, power=0):
#     if power == 0:
#         return 1
#     else:
#         return no * pow_no(no, power - 1)
#
# res1 = pow_no(2, 3)  # 2^3 = 8
# res2 = pow_no(5)     # 5^0 = 1 (default power is 0)
#
# print(res1)
# print(res2)


# todo 21. Create a function with recursion which will find the factorial of a given no.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
# print("Factorial of 5:", result)


# todo 22. Create a script/program that will take arguments as 1,2,3,4,5, or 6 and will also
# todo take operands as arguments based on the selection made it will perform the operation and print the result.
# todo 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exponent,
# todo 6=Floor Division. If anything else is passed it should say Invalid argument.
# todo Create a parent function which will accept the options and based on the options
# todo it will call nested functions for each operation. So total 7 functions will be
# todo created one parent and 6 nested functions.
# todo According to the selection made take inputs for the operations. If 1,2,3 are
# todo selected take 3 inputs as operands and if 4,5,6 are selected take 2 inputs as
# todo operands. Perform the operation and print the result.

# def add(a, b, c):
#     return a + b + c
#
# def sub(a, b, c):
#     return a - b - c
#
# def mul(a, b, c):
#     return a * b * c

# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "not divide by zero."
#
# def exp(a, b, c):
#     return a ** b ** c

# def flr_div(a, b):
#     if b != 0:
#         return a // b
#     else:
#         return "cannot divide by zero."
#
# def pfm_opr(option, operands):
#     if option == 1 and len(operands) == 3:
#         return add(*operands)
#     elif option == 2 and len(operands) == 3:
#         return sub(*operands)
#     elif option == 3 and len(operands) == 3:
#         return mul(*operands)
#     elif option == 4 and len(operands) == 2:
#         return div(*operands)
#     elif option == 5 and len(operands) == 2:
#         return exp(*operands)
#     elif option == 6 and len(operands) == 2:
#         return flr_div(*operands)
#     else:
#         return "invalid argument select 1, 2, 3, 4, 5, or 6."
#
# def main():
#     print("select operation:")
#     print("1. addition")
#     print("2. subtraction")
#     print("3. multiplication")
#     print("4. division")
#     print("5. exponent")
#     print("6. floor division")
#
#     option = int(input("Enter option (1-6): "))
#     operands = [float(input(f"Enter operand {i + 1}: ")) for i in range(3 if option in [1, 2, 3] else 2)]
#
#     result = pfm_opr(option, operands)
#     print(f" result: {result}")
# main()


# todo 23 Create a two funcitons. Call one function from another function.

# def function_one():
#     print("function one called.")
# def function_two():
#     print("function two calling function one.")
#     function_one()
# function_two()

# todo 24 Create a function that will take 5 arguments 2 will be mandatory and 3 will be keyword parameters.
# def pfm_opr(a, b, x=None, y=None, z=None):
#     if x is None and y is None and z is None:
#         #  todo If 2 parameters are passed perform multiplication of 2 parameters.
#         res = a * b
#         print("mul res:"9, res)
#     elif x is not None and y is None and z is None:
#         # todo If 3 parameters are passed print all the 3 parameters.
#         print("para 1:", a)
#         print("para 2:", b)
#         print("optional  :", x)
#     elif x is not None and y is not None and z is None:
#         # todo If 4 parameters are passed addition of 4 parameters.
#         res = a + b + x + y
#         print("add res:", res)
#     elif x is not None and y is not None and z is not None:
#         # todo If 5 parameters are passed multiply 2 mandatory parameters and then separately multiply 3 keyword parameters and add both of them.
#         mul_mandatory = a * b
#         mul_keywords = x * y * z
#         res = mul_mandatory + mul_keywords
#         print("mult of 2 mandatory parameters:", mul_mandatory)
#         print("mul of 3 keyword parameters:", mul_keywords)
#         print("Final result (sum of both):", res)
#     else:
#         print("invalid ")
#
# pfm_opr(2, 3)                  # mul
# pfm_opr(2, 3, x=4)              # print 3 parameters
# pfm_opr(2, 3, x=4, y=5)        # add
# pfm_opr(2, 3, x=4, y=5, z=6)  # mul and add


# todo 25. Define a class and define two member variables and two methods inside the class.
# todo One method will have one parameter and other method will not have any parameter.
# todo Create a constructor for the class accepting two parameters and assign them to the class member variables.
#  One of the two methods will perform an operation on the member variables and give result.
#  The second method will print the result.


# class myClass:
#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.var2 = var2

#     def widout_prm(self):
#         # todo  Method without any parameter
#         res = self.var1 * self.var2
#         return res

#     def wid_prm(self, x):
#         # todo Method with one parameter
#         res = self.var1 + x
#         return res

#     def dis_res(self, res):
#         # todo Method to print the result
#         print("Result:", res)
# obj = myClass(5, 10)
# res1 = obj.wid_prm(3)
# res2 = obj.widout_prm()
# obj.dis_res(res1)
# obj.dis_res(res2)


# todo 26. Create a parent class and a child class. Create two methods in the parent class.
# todo Create one method in the child class. Create an object of parent and try to access
# todo the method of parent and child class. Create an object of child class and try to access the method of parent and child class.
#
# class parent:
#     def parent_method1(self):
#         print("This is Parent Method 1")
#     def parent_method2(self):
#         print("This is Parent Method 2")
#
#
# class child(pqarent):
#     def child_method(self):
#         print("This is Child Method")
#
# # todo Create an object of ParentClass
# parent_obj = parent()
#
# # todo Access methods of the ParentClass using the parent object
# parent_obj.parent_method1()
# parent_obj.parent_method2()
#
# # todo  ERROR Try to access the method of childclass using the parent object (will raise an AttributeError)
# # todo parent_obj.child_method()
# print("\n")
# # todo Create an object of ChildClass
# child_obj = ChildClass()
# # todo Access methods of both ParentClass and ChildClass using the child object
# child_obj.parent_method1()
# child_obj.parent_method2()
# child_obj.child_method()

# todo 27. Create a constructor and destructor for the above class.

# class class:
#     def __init__(self):
#         print("constructor called")
#
#     def method(self):
#         print("this is a method")
#
#     def __del__(self):
#         print("destructor called")

# object = class()
# object.method()
# del object

# todo 28. Override and Overwrite a method of the parent class in child class.

# class parent:
#     def method(self):
#         print("this is the method from parent ")
# class child(parent):
#     def method(self):
#         print("this is the overridden method in the child")
#
#
# child_obj = child()
# child_obj.method()

# todo 29. Implement multiple inheritance and multi-level inheritance.
#     **** Multiple Inheritance ****
# class grandFather:
#     def method_one(self):
#         print("method  grandfather")

#
# class parent:
#     def method_two(self):
#         print("method parent")
#
#
# class child(grandFather, parent):
#     def child_method(self):
#         print("child method")
#
#
# # todo  Create an object of ChildClass
# child_obj = child()
#
# # todo call methods
# child_obj.method_one()
# child_obj.method_two()
# child_obj.child_method()

#  todo   **** Multi Level Inheritance ****
# class grandParent:
#     def grandparent_method(self):
#         print("grandparent Method")
#
# class parent(grandParent):
#     def parent_method(self):
#         print("parent Method")
#
# class child(parent):
#     def child_method(self):
#         print("child Method")
#
#
# # todo create object of childClass
# child_obj = child()
#
# # todo call methods
# child_obj.grandparent_method()
# child_obj.parent_method()
# child_obj.child_method()


# todo -30. Perform overloading for constructors and methods defined in the class.
       # todo  **** constructor overloading ****
# class test:
#     def __init__(self,x):
#         self.x1=x
#     def __init__(self,x,y):
#         self.x1=x
#         self.y1=y
#     def method(self):
#         print("this is method")
#         self.x1 + self.y1
# ## python was consider last constructor called not first
# obj = test(1,5)
# obj.method()


        #   todo **** method overloading ****
# class test:
#     # def method(self):
#     #     print("Welcome")
#     # def method(self,fname=''):
#     #     print("welcome" ,fname)
#     def method(self,fname='',lname=''):
#         print("welcome" ,fname ,lname)
#
# obj = test()
# obj.method()
# obj.method("anjana")
# obj.method("anjana","dafda")



# todo 31  Define a class(my_parent_class) with 2 variables x,y and 3 methods. add, sub and print_result. Define a child class and override the methods and constructor as
# given below.
    #  todo **** Create parent class ****
# class parent:
        # todo   *** create constructor of parent class ***
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#       # todo  *** create add method ***
#     def add(self, a=0, b=0):
#         self.res1 = self.x + a
#         self.res2 = self.y + b
#         self.print_result()
#      # todo  *** create sub method ***
#     def sub(self, a=0, b=0):
#         self.res1 = self.x - a
#         self.res2 = self.y - b
#         self.print_result()
#      # todo  *** create print method to print the result ***
#     def print_result(self):
#         print(f"result 1: {self.res1}")
#         print(f"result 2: {self.res2}")
##  todo ****  create objects  ****


# obj1 = parent()
# obj2 = parent(5)
# obj3 = parent(10, 20)


#    # todo  **** create child class ****
# class child(parent):
       ## todo *** create constructor for child class and child class is called the parent class constructor using super
        ## todo and python was consider the last constructor is called  ***
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         self.z = z
#
#     def add(self, a=0, b=0, c=0):
#         self.res1 = self.x + a + c
#         self.res2 = self.y + b + self.z
#         self.print_result()
#
#     def sub(self, a=0, b=0, c=0):
#         self.res1 = self.x * a * c
#         self.res2 = self.y * b * self.z
#         self.print_result()
#    # todo *** del method is used to delete/destroy  the object of the class  ***
#     def __del__(self):
#         print("destructor  automatically called ")

# # todo *** call methods on parent class objects  ***
# obj1.add()
# obj2.sub(2, 1)
# obj3.add(5, 5)
#
# # todo *** create child class object ***
# child_obj = child(3, 4, 5)
#
# # todo *** call methods on child class object  ***
# child_obj.add(1, 2)
# child_obj.sub(2, 3)
#
# # todo ***  call destructor   ***
# del child_obj






