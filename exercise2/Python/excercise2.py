# todo **** 1. Get me list of odd numbers between 1 to 20 without using if condition. ****
import curses.ascii


# odd_no = [num for num in range(1, 21, 2)]
# print(odd_no)

# todo **** 2. Get a list of 1 to 20 then remove elements from list to get only even elements. ****

# numbers = list(range(1, 21))
# even_no = [num for num in numbers if num % 2 == 0]
# print(even_no)

# todo **** 3. Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list. ****

# list1 = list(range(1, 9))
# list2 = list(range(4, 11))
#
# cmn_ele = list(set(list1) & set(list2))
# print(cmn_ele)


# todo **** 4. Sort a shuffled list of 10 random numbers in descending order. ****

# import random
# rdom_no = random.sample(range(1, 101), 10)
# srted_no_deseding = sorted(rdom_no, reverse=True)
#
# print(srted_no_deseding)

# todo **** 5. x=(1,2,3,4,5), y=(4,5,6,7). Combine these two tuples in a single tuple ignoring the common elements. ****

# x = (1, 2, 3, 4, 5)
# y = (4, 5, 6, 7)
#
# tuple3 = tuple(set(x) | set(y))
# print(tuple3)

# todo **** 6. Define two sets and perform all the set operations and validation operations. ****

# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}
#
# #  todo **** print  ****
# print(f"set A: {set_A}")
# print(f"set B: {set_B}\n")

# # todo ****  perform set operations  ****

# union_set = set_A.union(set_B)
# intersection_set = set_A.intersection(set_B)
# difference_set_A_B = set_A.difference(set_B)
# difference_set_B_A = set_B.difference(set_A)
# symmetric_difference_set = set_A.symmetric_difference(set_B)

# print(f"union of sets A and B: {union_set}")
# print(f"intersection of sets A and B: {intersection_set}")
# print(f"difference of set A - set B: {difference_set_A_B}")
# print(f"difference of set B - set A: {difference_set_B_A}")
# print(f"symmetric difference of sets A and B: {symmetric_difference_set}\n")

#
# # todo ****  validation operations  ****

# is_subset = set_A.issubset(set_B)
# is_supset = set_A.issuperset(set_B)
# is_disjoint = set_A.isdisjoint(set_B)

# print(f"is set A a subset of set B: {is_subset}")
# print(f"is set A a superset of set B: {is_supset}")
# print(f"sets A and B disjoint: {is_disjoint}")

# todo **** 7. Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's method. ****

# my_dict = dict.fromkeys(range(1, 11), 1)
# print(my_dict)

# todo **** 8. Print all the keys and values of a dictionary. ****

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")

# todo **** 9. Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries. ****

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 4, 'd': 5, 'e': 6}
#
# dict1.update(dict2)
# merged_dict = dict1
# # or dict3 = dict1 | dict2
# # print(dict3)
# print(merged_dict)

# todo **** 10. How to check whether a key is existing in a dictionary or not. ****

# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# if 'b' in my_dict:
#     print("'b' exists in  dictionary.")
# else:
#     print("'b' does not exist in the dictionary.")

# todo **** 11. How can we have two variables refering to a single list, set and dictionary. ****

# #  todo *** using List ***

# my_list = [1, 2, 3, 4, 5]
# another_list = my_list
# my_list.append(6)
# print(my_list)
# print(another_list)

# # todo *** using set ***

# my_set = {1, 2, 3, 4, 5}
# another_set = my_set
# my_set.add(6)
# print(my_set)
# print(another_set)

# # todo *** using dictionaries ***

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# another_dict = my_dict
# my_dict['d'] = 4
# print(my_dict)
# print(another_dict)

# todo **** 12. Use all the case methods of strings. ****

  # # todo *** string ***

# string = "Hello, World!"
#
# # todo *** uppercase the  string ***

# upper_str= string.upper()
# print(f"uppercase: {upper_string}")
#
# # todo *** lowercase the  string ***

# lower_str = string.lower()
# print(f"lowercase: {lower_str}")

# # todo *** title case the string ***

# title_str = string.title()
# print(f"Titlecase: {title_str}")


# # todo ***  check if the string is titlecase  ***

# is_title = string.istitle()
# print(f"Is Titlecase: {is_title}")

#str1 = "anjana dafda gordhanbhai dafda"
#res = str1.casefold()# todo return the all character of small
# print(res)

# res = str1.center(40)# todo return the string center
# print(res)

# res = str1.count("dafda")# todo count the world
# print(res)

# res = str1.encode()# todo  return the string encoding
# print(res)

# res = str1.endswith('a')# todo return true or false
# print(res)


# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(2)# todo return the space of character
# print(x)

#text = "Hello, welcome to my world."
# x = text.find("welcome")# todo return the index of strings  same as index method
# print(x)

# txt = "for only {price:.2f} rupees!"
# print(txt.format(price = 49))

# myTuple = ("anjana", "kamlesh", "vikas")
# x = "#".join(myTuple)
# print(x)

# text = "banana"
# x = text.ljust(20) # todo return space after banna is print
# print(x, "is my favorite fruit.")


# text = "Hello my FRIENDS"
# x = text.lower()# todo return lowercase string
# print(x)


# txt = "     anjana     "
# x = txt.lstrip()
# print("i am ", x, "trainne in skyscend business solutions")

# text = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(text.translate(mytable))


# str = "I could eat bananas all day"
# x = str.partition("bananas") # todo ('I could eat ', 'bananas', ' all day')
# print(x)


# str = "anjana dafda "
# x = str.replace("dafda","solanki")
# print(x)

# str = "anjana dafda "
# x = str.rfind("dafda") # todo return the index of dafda
# print(x)

# str = "anjana dafda"
# x = str.rindex("jana") # todo return the index value of the string
# print(x)

# str = "anjana ,dafda, anjana ,dafda ,gordhanbhai"
# x = str.rsplit(", ") # todo  return in list
# print(x)

# text = "welcome to the jungle"
# x = text.split() # todo split the string
# print(x)

# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# s = "Hello, welcome to my world."
# x = s.startswith("Hello") # todo return true or false
# print(x)


# txt = "Hello My Name Is PETER"
# x = txt.swapcase() # todo output is : - hELLO mY nAME iS peter
# print(x)




# todo **** 13. How to split a string with a substring? ****

# string = "This is a string to be split."
# substr = "to be"
# split_string = string.split(substr)
# print(split_string)  # ['This is a string ', ' split.']


# todo **** 14. How to replace a string with a substring? ****

# org_str = "This is a string with apple."
# rep_str = "banana"
# replaced_str = org_str.replace("apple", rep_str)
# print(replaced_str)  #  todo "This is a string with banana."

# todo *** 15. How to join multiple strings with a substring? ***

# strings = ["apple", "banana", "cherry"]
# delimiter = ", "
# join_str = delimiter.join(strings)
# print(join_string)  # todo  "apple, banana, cherry"

# todo *** 16. How to make partition of a string? ***
#
# string = "This,is,a,string"
# par_li = string.split(",")
# print(par_li)  # ['This', 'is', 'a', 'string']

# todo *** 17. How to find the no of occurences of a substring? ***

# string = "This is a string with multiple occurrences of the word 'the'."
# substr = "the"
# occur = string.count(substr)
# print(f"The substring '{substr}' appears {occur} times in the text.")

# todo *** 18. Use all the validation methods used with string.***


#str1 = "anjana dafda gordhanbhai dafda"
# res = str1.capitalize()# todo return the first charcter of capital
# print(res)

# x = text.isalnum()# todo is false because space is not alphanum
# print(x)

# s = "hello"
# x = s.isalpha() # todo True
# print(x)

# s = "hello123"
# x=s.isascii()# todo return true
# print(x)


# n = "1234"
# x = n.isdecimal() # todo  true
# print(x)

# n = "1234"
# x = n.isdigit() # todo true
# print(x)


# txt = "1232"
# x = txt.isidentifier() # todo false only get alpha value
# print(x)

# s = "anju"
# x = s.islower() # todo true
# print(x)

# s = "ANJANA"
# x = s.isupper() # todo true
# print(x)

# n = "1234"
# x = n.isnumeric() # todo true
# print(x)

# txt = "Hello! Are you #1?"
# x = txt.isprintable() # todo true
# print(x)

# x = txt.isspace() # todo if string is only space than return true other wise false
# print(x)

# txt = "Hello, And Welcome To My World!"
# x = txt.istitle() # todo return true if all world first character is capital
# print(x)

# txt = "Hello, And Welcome To My World!"
# x = txt.isupper()# todo  if all world are capital than return true other wise false
# print(x)




# todo *** 19. Convert all the data structures to other data structures. ***

# l=[1,2,3,4,5]
# print(set(l))
# print(tuple(l))
# print(dict(l)) # todo TypeError: cannot convert dictionary update sequence element #0 to a sequence

# t = (1,2,3,4,5)
# print(list(t))
# print(set(t))
# # todo dictionary same as above

# s ={1,2,3,4,5,6}
# print(list(s))
# print(tuple(s))
# # todo dictionary same as above

# todo *** 20. Get the last element of the list, tuple and string. ***

# l =[1,2,3,4,5,6]
# t =(7,8,9,4,5,6,2)
# s =("anjana","dafda","gordhanbhai")
#
# print(l[-1])
# print(t[-1])
# print(s[-1])

# todo **** 21. Get last 3 elements of the list, tuple and string. ****

# l =[1,2,3,4,5,6]
# t =(7,8,9,4,5,6,2)
# s =("vikas","anjana","dafda","gordhanbhai")
#
# print(l[-3:])
# print(t[-3:])
# print(s[-3:])

# todo *** 22. Get first 5 elements of list, tuple and string. ***

# l =[1,2,3,4,5,6,7,8,9,4,5,6,1,12]
# t =(7,8,9,4,5,6,2,78,45,69,1,2,3)
# s =("vikas","anjana","dafda","gordhanbhai","kamlesh","mithapara","solanki")
#
# print(l[:5])
# print(t[:5])
# print(s[:5])

# todo *** 23. Get all the elements excluding first and last elements from list, tuple and string. ***


# l =[1,2,3,4,5,6,7,8,9,4,5,6,1,12]
# t =(7,8,9,4,5,6,2,78,45,69,1,2,3)
# s =("vikas","anjana","dafda","gordhanbhai","kamlesh","mithapara","solanki")
#
# print(l[1:-1])
# print(t[1:-1])
# print(s[1:-1])

# todo *** 24. Get all the elements in a list using : operator. ***

# l =[1,2,3,4,5,6,7,8,9,4,5,6,1,12]
# t =(7,8,9,4,5,6,2,78,45,69,1,2,3)
# s =("vikas","anjana","dafda","gordhanbhai","kamlesh","mithapara","solanki")
#
# print(l[:])
# print(t[:])
# print(s[:])

# todo *** 25. Get last 5 elements from a list of 1 to 10 using negative indexing. ***

# l = [1,2,3,4,5,6,7,8,9,10]
# l2=l[-5:]
# print(l2)

# todo *** 26. Get 4 elements of the list excluding last 2 elements using negative indexing. ***

# l = [1,2,3,4,5,6,7,8,9,10]
# l2=l[:-2]
# print(l2)

# todo *** 27. Convert a list of tuple to dictionary. ***

# li_tuples = [('a', 1), ('b', 2), ('c', 3)]
# res_dict = dict(li_tuples)
# print(res_dict)


# todo *** 28. Create a dictionary using range() as following. {'a':1, 'b':2, 'c':3, 'd':4, 'e':5....'y':25,'z':26}.***

# res_dict = {}
# for i in range(ord('a'), ord('z') + 1):
#     res_dict[chr(i)] = i - ord('a') + 1
# print(res_dict)


# todo *** 29. There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20].***
#   *** Get a third list from these two lists as [12,14,16,18,20,22,24,26,28,30].***

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# res_list = [x + y for x, y in zip(list1, list2)]
# print(res_list)


# todo *** 30. Get Square of all the elments in a list from 1 to 10 numbers.***

# res_list = [x ** 2 for x in range(1, 11)]
# print(res_list)

# todo *** 31. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7]. ***

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# res_list = [x for x in list1 if x not in list2]
# print(res_list)

# todo *** 32. Fetch the data from the following. ***

#   32-1. Fetch 5 which is the value of ‘e’ from below which is marked in red.
# x = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4, (5, 6, 7, {'e': 5})]}
# e = x['d'][4][3]['e']
# print(e)

# todo 32-2. Fetch 2 from below which is marked in red.

# x = {‘a’:{‘b’:[1,2,(3,4,{‘c’:3,’d’:4,’e’:[1,2,3]})]}}
#
# x = {'a': {'b': [1, 2, (3, 4, {'c': 3, 'd': 4, 'e': [1, 2, 3]})]}}
# ele = x['a']['b'][2][2]['e'][1]
# print(ele)


# todo 32-3. Fetch 6 from below which is marked in red.

#x = [1, 2, (3, 4, 5, {‘a’:1, ‘b’:[2,3,4,(5,6)]})]

# x = [1, 2, (3, 4, 5, {'a': 1, 'b': [2, 3, 4, (5, 6)]})]
# six = x[2][3]['b'][3][1]
# print(six)


# todo 32-4. Fetch 2 from above which is marked in red.

# x = {True:[1,2,3,{‘a’:1,’b’:2}],False:[(2,3,4,5,{1:2})]}

# x = {True: [1, 2, 3, {'a': 1, 'b': 2}], False: [(2, 3, 4, 5, {1: 2})]}
# y = x[False][-1][-1]
# print(y)
# z = y.get(1, None)
#
# if z is not None:
#     print(z)
# else:
#     print("Key 1 not found in the last dictionary.")

# todo 5. Fetch 9 from above which is marked in red.

# x = {1:2,2:3,3:4,4:{‘a’:’b’,’c’:’d’,’e’:’f’,’f’:[1,2,3,{1:9,3:8}]}

# x = {1: 2, 2: 3, 3: 4, 4: {'a': 'b', 'c': 'd', 'e': 'f', 'f': [1, 2, 3, {1: 9, 3: 8}]}}
#
# value_9 = x[4]['f'][-1][1]
# print(value_9)

# todo 33. Create a function for string that will check whether a string is having the first
#    letter as Capital and not anyother letter is capital.

# def capital(s):
#     return s[0].isupper() and s[1:].islower()
# st = "Hello"
# res = capital(st)
#
# if res:
#     print(f'string "{st}" first letter capital ')
# else:
#     print(f'string "{st}" first letter is not capital')

# todo 34. Create a class Student and add member variables with False values. The variables are as listed below.
#   Marks will have a default value blank list.
#     1. Name
#     2. Reg No
#     3. Roll No
#     4. Standard
#     5. Admission Year
#     6. Marks
#     7. Result
#    Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission year.
#   In the constructor add validation for Name to be only Alphabetic, Reg No to be alphanumeric, Roll No, Standard nad Admission year to be numeric.
#    All abobve values will be accepted as string only.
#   Add a method that will accept a dictionary for marks containing subject as key and marks as values.
#   It will add the dictionary to the list of marks.
#  Marks list will have multiple elements and each element will be a dictionary only.
#   Here there should be a validation to acccept the marks which are less than or equal to 100 only.
#   If the obtained marks are less than 40 the result willl be fail otherwise pass.
#   In the dictionary the result can be added.
#   Add another method that will generate the result.
#  This method will check if there is any line in the marks having fail as result the result will be Fail and it will print the complete result as following.




class Student:
    def __init__(self, name, reg_no, roll_no, std, admi_year):
        if all(c.isalpha() or c.isspace() for c in name):
            self.name = name
        else:
            print("invalid name")
            return

        if reg_no.isalnum():
            self.reg_no = reg_no
        else:
            print("invalid registration number")
            return

        if roll_no.isdigit() and std.isdigit() and admi_year.isdigit():
            self.roll_no = roll_no
            self.std = std
            self.admi_year = admi_year
        else:
            print("invalid roll number, standard, or admission year")
            return

        self.marks = []
        self.result = "pass"

    def add_mark(self, mark_dict):
        if all(0 <= marks <= 100 for marks in mark_dict.values()):
            result = "fail" if any(marks < 40 for marks in mark_dict.values()) else "pass"
            mark_dict["result"] = result
            self.marks.append(mark_dict)
        else:
            print("invalid marks")

    def generate_result(self):
        total_marks = 0
        total_subjects = 0

        for mark_dict in self.marks:
            for subject, mark in mark_dict.items():
                if subject != "result":
                    total_marks += mark
                    total_subjects += 1

        if total_subjects == 0:
            print("no valid marks calculate result")
            return

        percentage = (total_marks / (total_subjects * 100)) * 100

        print(f"Name..................: {self.name}")
        print(f"Registration number...: {self.reg_no}")
        print(f"Roll number...........: {self.roll_no}")
        print(f"Std ..................: {self.std}")
        print(f"Admision year.........: {self.admi_year}\n")
        print("---------- ********** ----------")
        for index, mark_dict in enumerate(self.marks, start=1):
            print(f"{index} -{self.name} Marks: {mark_dict}")
        print("---------- ********** ----------")
        print(f"\n")
        print(f"total Marks ..........: {total_marks}")
        print(f"percentage ...........: {percentage:.2f}%")
        print("result ...............: PASS" if self.result == "pass" else "result: FAIL")


student = Student("Anjana", "A123", "12101", "12", "2022")
student.add_mark({"Math": 30, "English": 75, "Hindi": 65})
student.generate_result()
print(f"\n")
student2 = Student("Anjum", "B145", "122102", "10", "2019")
student2.add_mark({"Math": 45, "English": 55, "Hindi": 65})
student2.generate_result()












