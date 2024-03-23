#Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89
#output- B
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59
#If, elif, else

num = int(input("enter your grade"))

if num >= 90:
    print("Your Grade is A Grade ",num)
elif num >= 80 and num <90:
    print("Your grade is B grade",num)
elif num >= 70 and num <80:
    print("Your grade is C grade",num)
elif num >= 60 and num < 70:
    print("Your grade is D grade", num)
elif num>=0 and num<60:
    print("your grade is F grade")
else:
    print("invalid input ",num)