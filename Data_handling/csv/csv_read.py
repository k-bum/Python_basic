line_counter = 0
data_header = []
customer_list = []

with open("customers.csv", "r") as customers_data :
    while 1 :
        data = customers_data.readline()
        if not data :
            break
        if line_counter == 0 :
            data_header = data.split(",")
            line_counter += 1
            print(data_header)
        else :
            customer_list.append(data.split(","))
            line_counter += 1

print("Header : \t", data_header)
for i in range(0, 10) :
    print("Data ", i + 1, ":\t\t", customer_list[i])
print(len(customer_list))