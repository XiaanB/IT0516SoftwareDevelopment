
column_number = 0


column_input = input("Please inter your column letter: ")
if column_input.lower() == ("a" or "c" or "e" or "g"):
    column_number = 1


row_input = int(input("Please enter your row number: "))
coordinate_ref = column_number + row_input

if coordinate_ref % 2 == 0:
    print("The square is black")
else:
    print("The square is white")
