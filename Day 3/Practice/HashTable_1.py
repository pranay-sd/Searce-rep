#Implemention using python list (or array)
stock_price=[]
with open("Hash.csv","r") as f:
    for line in f:
        #print(line)
        data = line.split(',')

        day = data[0]
        price = float(data[1])
        stock_price.append ([day, price])

print(stock_price)

#Retrieving an element from the list
for ele in stock_price :
    if ele[0] == "06-Mar":
        print(ele[1])

#Implemention using python dictionery
stock_prices = {}
with open("Hash.csv","r") as f:
    for line in f:
        tokens = line.split(',')

        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices)

#Retrieving an element from the dictionery
stock_prices['06-Mar']