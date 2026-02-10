reg=int(input("Enter Register Number: "))
last_digit=reg%10
n=int(input("Enter number of students: "))
marks=[]
for i in range(n):
    m=int(input("Enter mark: "))
    marks.append(m)
valid=0
fail=0
print("\n--- Student Results ---")
for m in marks:
    if m<0 or m>100:
        result="Invalid"
    else:
        valid+=1
        if m==40 and last_digit%2==1:
            result="Average"
        elif m>=90:
            result="Excellent"
        elif m>=75:
            result="Very Good"
        elif m>=60:
            result="Good"
        elif m>=40:
            result="Average"
        else:
            result="Fail"
            fail+=1
    print(m,"→",result)
print("\nTotal Valid Students:",valid)
print("Total Failed Students:",fail)
