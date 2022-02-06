import csv

def main():
    customer_infile = open('customers.csv', 'r') # Reading customer.csv file
    csv_reader = csv.reader(customer_infile)

    customer_country_outfile = open('customer_country.csv', 'w', newline='') #create new file 'custoemr_country.csv'
    csv_writer = csv.writer(customer_country_outfile)
    
    for line in csv_reader:
        customer = [line[0], line[1], line[2], line[4]]
        csv_writer.writerow(customer)

    customer_infile.close()

main()