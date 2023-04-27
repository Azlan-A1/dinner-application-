#Name: Azlan Ahmad
#Date January 28th 2023
#Professor: Abdelkareem Jaradat
#Description: This Python programs helps to organize a dinner meal with friends by asking people about their dietary restrictions and places an order for the food items they have ordered. 
#This is a program to display specific meals costs according to some yes or no questions and revealing the total amount in the end


answer = int(input("Please enter the number of invitees:")) #Asks for user input, this value corresponds to the number of guests there are. a.k.a. the food items ordered. 
print() #prints the number asked

#variables assigned to correspond towards the given menu prices
#There are variables that set to the value of 0 because of the fact that the order starts at $0 until someone places an order for a food item.
#These are the starting values that will increase overtime 
pizzaOrders = 0
pastaOrders = 0
falafelOrders = 0
steakOrders = 0
beverageOrders = 0
totalCostpizza = 0
totalCostpasta = 0
totalCostfalafel = 0
totalCoststeak = 0
totalCostBeverage = 0

#These are the food item prices including beverage if none of the other food items have been picked. 
costPizza = 44.50
costPasta = 48.99
costFalafel = 52.99
costSteak = 49.60
costBeverage = 5.99

for count in range (1,  answer+1): #this for loop allows this sequence of questions to be asked for how many invitees there are invited to the dinner
    print("Please enter the order details for invitee Number",f"{count}/{answer}" ) #f strings formatting 
    meal = str(input("Do you want a keto friendly meal?")) #asks the keto question 
    meal2 = str(input("Do you want a vegan meal?")) #asks the vegan meal question 
    meal3 = str(input("Do you want a Gluten-free meal?")) #asks the user for gluten-free meal 
    print("---------------------------")
    
    

 #created variables in relation to the answers received if specific questions get yes/no inputs.
    Pizza = (meal == 'y'and meal2 == 'y' and meal3 != 'y') #This means if question1 = yes, question2 = yes and question3 does not equal = yes
    Pasta = (meal != 'y' and meal2 == 'y' and meal3 != 'y') #This variable will be used if question1 does not equal yes, question2 = yes and question3 does not equal yes
    Falafel = (meal == 'y' and meal2 == 'y' and meal3 == 'y') #This variable will be used if question1 = yes, question2 does not equal yes and question3 equals yes 
    Steak = (meal == 'y' and meal2 != 'y' and meal3 == 'y') #This variable will be used if question1 = yes, question2 does not equal yes, question3 = yes
    Beverage = (meal != 'y' and meal2 != 'y' and meal3 != 'y') #This variable will be used if question1 does not equal yes, question2 does not equal yes, and question3 does not equal yes
    

    orders = 0 #orders is set to 0 because this value will increase as more values increase. 

    if Pizza: #if user picks pizza, it will add it to the order
        orders += 1
        pizzaOrders+=1
        totalCostpizza += costPizza
    elif Pasta: #if user picks pasta, it will add it to the order
        orders += 1
        pastaOrders+=1
        totalCostpasta += costPasta
    elif Falafel: #if user picks falafel, it will add it to the order
        orders += 1
        falafelOrders+=1
        totalCostfalafel += costFalafel
    elif Steak: #if user picks steak, it will add it to the order
        orders += 1
        steakOrders+=1
        totalCoststeak += costSteak
    elif Beverage: #if user doesnt pick anything, then a beverage will be added 
        orders +=1
        beverageOrders +=1
        totalCostBeverage += costBeverage

        
#inputted tip by the user. This is the tip percentage the customer wants to give 
tip = int(input("How much do you want to tip your server (% percent)?"))

#the result of the orders that were previously inputted by the user 
print("\nYou have", answer, "invitees with the following orders: ") 
print(pizzaOrders,"invitees ordered Pizza. The cost is: ${:.2f}".format(totalCostpizza)) #displays how many pizzas are ordered and shows the total cost 
print(pastaOrders,"invitees ordered Pasta. The cost is: ${:.2f}".format(totalCostpasta)) #displays how many pastas are ordered and shows the total cost 
print(falafelOrders,"invitees ordered Falafel. The cost is: ${:.2f}".format(totalCostfalafel)) #displays how many falafel are ordered and shows the total cost 
print(steakOrders,"invitees ordered Steak. The cost is: ${:.2f}".format(totalCoststeak)) #displays how many steaks are ordered and shows the total cost 
print(beverageOrders,"invitees ordered beverage. The cost is: ${:.2f}".format(totalCostBeverage)) #displays how many beverages are ordered and shows the total cost 


beforeTax = totalCostpizza + totalCostpasta + totalCostfalafel + totalCoststeak + totalCostBeverage #adds all the prices of the food items ordered. 
afterTax = beforeTax * 1.13 #multiplies the beforetax price by 1.13 (ontario tax price)
OverallCost = afterTax * ((100+tip)/100) #this is after the tip percentage is contributed in the overall price

rbeforeTax = round(beforeTax,2) #rounds the value by two decimal places
rafterTax = round(afterTax,2) #rounds the value by two decimal places
rOverallCost = round(OverallCost) #rounds the value by two decimal places

print("\nThe total cost before tax is: ${:.2f}".format(rbeforeTax)) #displays the total cost before tax
print("The total cost after tax is ${:.2f}".format(rafterTax)) #displays the total cost after tax
print("The total cost after", f"{tip}%"" tip is ${:.2f}".format(rOverallCost)) #displays the total cost after tax and tip percentage (includes everything)