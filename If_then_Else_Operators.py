#If then Else

a = 33

b = 200

if b > a:
  print("b is greater than a")  #WICHTIG!!! Einrücken


a = 33

b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200

b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 200

b = 33

c = 500

if a > b or a > c:
  print("At least one of the conditions is True")



a = 200

b = 33

c = 500

if a > b and a < c:
  print("At least one of the conditions is True")


#Operators for comparison
#
#   < <= => >
#
#   == !=
#
#   and or
