import csv

def main():
    employee_pay_infile = open('EmployeePay.csv', 'r') # Reading customer.csv file
    csv_reader = csv.reader(employee_pay_infile)
    csv_reader.__next__() #skipping first line

    
    for line in csv_reader:
        print('First name:', line[1])
        print('Last name:', line[2])
        print('Salary:', line[3])
        print('Bonus:',    round(int(line[3]) * float(line[4]), 2)  )



    employee_pay_infile.close()

main()

