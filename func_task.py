# take a number as a parameter and print its multiplication table
# 2 x 1 = 2
# 2 x 2 = 4
# .
# .
# .
# 2 x 10 = 20




def mul_table(number):
    for table in range(1,11):
        print(number," x ",table," = ",(number*table))
        
mul_table(number=int(input("Enter any number: ")))


