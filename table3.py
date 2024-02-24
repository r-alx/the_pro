def function(j):
    counter = 1
    while counter <= 30:
        print(j,"*",counter,"=",j* counter)
        counter = counter + 1
table = int(input("enter the number:"))
function(table)