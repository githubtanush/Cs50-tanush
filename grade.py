score = int(input("Score: "))
'''if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score<90:
    print("Grade: B")
elif score >=70 and score<80:
    print("Grade: C")
elif score >=60 and score<70:
    print("Grade: D")
elif score >=50 and score<60:
    print("Grade: E")
else:
    print("Grade: F")'''


'''if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score<90:
    print("Grade: B")
elif 70 <= score <80:
    print("Grade: C")
elif 60 <= score <70:
    print("Grade: D")
elif 50 <= score <60:
    print("Grade: E")
else:
    print("Grade: F")'''

'''if score>=90:
    print("Grade: A")
elif score>=80:
    print("Grade: B")
elif score>=70:
    print("Grade: C")
elif score>=60:
    print("Grade: D")
elif score>=50:
    print("Grade: E")
else:
    print("Grade: F")'''
# when we use if instead of elif else then logically it does not become it mutually exclusive and when we write 95 it would print all the grade like that so turn to mutually exclusive we use elif function because in if it treats only like 1 question not another condition or question

if score>=90:
    print("Grade: A")
if score>=80:
    print("Grade: B")
if score>=70:
    print("Grade: C")
if score>=60:
    print("Grade: D")
if score>=50:
    print("Grade: E")
