"""
Create a code to print a receipt for a retail business. The receipt will display: name of the store; address; type of transaction: sales, return, or void; itemization of purchased items; detail of the dolar amount paid by customers; and the store return policy 
""" 

#create a dictionary with all the stores names and addresses to be display in the receipt. 
#The name of the store will be capitalized for marketing reasons and be positioning at the center of the receipt with (*) to catch people attention
#I will add two empty lines for easy reading purpose.
stores = {'Ann Grace':'10428 2nd Av. New York, NY 23754', 'Ann Grace UWS': '5673 82nd St. New York, NY 21065','Ann Grace UES': '5683 alphabet st, New York, NY 23456'} 
#print(([key for key in stores.keys()][0].upper().center(32, '*')) + ("\n") + ([value for value in stores.values()][0])+ ("\n"))

#Create a variable that holds all the different kinds of receipts to be able to print the one that correspond to sales.It will be printed below the store nsme and address 
receipt_type = ["sales receipt", "return", "void"]
#print (receipt_type[0].upper().center(32)+ ("\n"))

#create two list, one will holds the item description and the second one will hold the item price
garments_description = ["Linen Blend Shirtdress", "Gathered Neck Top", "Palazzo pants", "Linen Shirt", "Eyelet Dress"]
garments_price = [159, 54.50, 119, 98, 198]

#create a variable that holds the sales tax
percentage_sales_tax = 0.06

#create a variable that holds the customer's order amount and adds up the total purchase to be displayed on the receipt. For this example the customer bought item 0 and 2 on the list.
customer_one_total = 0
customer_one_total += garments["Linen Blend Shirtdress"] + garments["Palazzo pants"]

#calculate de sale tax for the order and add it to the customer total
customer_one_tax = customer_one_total * percentage_sales_tax
customer_one_total += customer_one_tax

purchase_before_tax = "Subtotal $" + str(customer_one_total - customer_one_tax)
total_sales_tax = "Sales tax: $" + str(customer_one_tax)
#print("Total purchased: $" + (customer_one_total))


#itemized items on the receipt
customer_one_itemization = ''
customer_one_itemization += garments_description[0] + ("\n") + garments_description[2]

#create a variable that hold the cutomers return Police
return_policy = "Thank you for visiting AnnGrace!" + ("\n") + "Items in unsused and original condition may be retruned to Ann Grace stores for a refund or exchanged."

receipt = ([key for key in stores.keys()][0].upper().center(32, '*')) + ("\n") + ([value for value in stores.values()][0])+ ("\n") + ("\n") + (receipt_type[0].upper().center(32)) + ("\n")+ ("\n") + customer_one_itemization + ("\n") + ("\n") + purchase_before_tax + ("\n") + total_sales_tax + ("\n")+ ("Total purchased: $" +str(customer_one_total)) + ("\n") + ("\n") + return_policy
print(receipt)
