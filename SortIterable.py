# sort() method = used with lists
# sort() function = used with iterable

# students= ["Squisward","Sandy","Patrick","Spongebob","Mr.Krabs"]
# students.sort()#method for lists only provided by list
# students.sort(reverse=True)
# for i in students:
#     print(i)


# students= ("Squisward","Sandy","Patrick","Spongebob","Mr.Krabs")
# # sorted_students=sorted(students) #sort iterable like list tuple
# sorted_students=sorted(students,reverse=True)
# for i in sorted_students:
#     print(i)

# students= [("Squisward","F",60),
#                      ("Sandy","A",33),
#                      ("Patrick","D",36),
#                      ("Spongebob","B",20),
#                      ("Mr.Krabs","C",78)]
# grade=lambda grades:grades[1]
# age=lambda ages:ages[2]

# students.sort(key=age,reverse=True)#Passing fn
# for i in students:
#     print(i)


students= (("Squisward","F",60),
           ("Sandy","A",33),
           ("Patrick","D",36),
           ("Spongebob","B",20),
           ("Mr.Krabs","C",78))
age=lambda ages:ages[2]
sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)