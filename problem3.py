#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""

List = []
y = 2
for i in range(y):
    x = int(input("Enter an integer: "))
    if x != -1:
        List.append(x)
        y = y + 1
else:
    List.sort()
    z = List[-1]
    print(f"The largest number you entered was {z}")

