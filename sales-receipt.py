#The company has multiple stores. First, I created a dictionary that holds the different locations.

#create a dictionary with all the stores names and addresses to be display in the receipt.
stores = {'Ann Grace': '10428 2nd Av. New York, NY 23754', 'Ann Grace UWS': '5673 82nd St. New York, NY 21065', 'Ann Grace MPD': '5683 alphabet st, New York, NY 23456} 
print(([key for key in stores.keys()][0], [value for value in stores.values()][0]))

#Create a variable that holds all the different kinds of receipts to be able to print the one that correspond to sales.It will be printed below the store nsme and address 
receipt_type = ["sales receipt", "return", "void"]
print (receipt_type[0].upper())

#create the items to be sold
garments = ['Linen Blend Shirtdress':159, 'Gathered Neck Top': 54.50,'Palazzo pants': 119, 'Linen Shirt': 98, 'Eyelet Dress': 198]

#create a variable for the sales tax
sales_tax = 0.06

#create a variable that holds the customer's order and adds up the total purchase to be displayed on the receipt. For this example the customer bought item 0 and 2 on the list.
customer_one_total = 0
customer_one_total += garments.['Linen Blend Shirtdress'] + garments.['Palazzo pants']

#calculate de sale tax for the order and add it to the customer total
customer_one_tax = customer_one_total * sales_tax
customer_one_grand_total = customer_one_total += customer_one_tax
 += 
#itemized items on the receipt
customer_one_itemization = ''
customer_one_itemization += garments[0] + ("\n") + garments[2]

receipt = (([key for key in stores.keys()][0], [value for value in stores.values()][0]) + ("\n") + ("\n") + (receipt_type[0].upper()) + ("\n") + ("\n") +customer_one_itemization + ("\n") + ("\n") + "total purchase: "\
+ str(customer_one_total) ("\n")+ "Sales tax (6%): " + str(customer_one_tax) + ("\n") + "Total Sale: " + str(cu)stomer_one_grand_total)

