#E-commerce

class Product:

    def __init__(self,product_id,name,price):

        self.product_id = product_id
        self.name = name
        self.__price = price

#get method

    def get_price(self):
      return self.__price

#set method

    def set_price(self):

      user_id = int(input("Enter Your Product Id:"))

      if user_id == self.product_id:

          print("Your id matched successfully!")

          new_price = float(input("Enter new price:"))

          if new_price > 0:
              self.__price = new_price
              print("Price Updated Successfully!")
          else:
              print("Invalid Price")
      else:
         print("Product ID not matched!")

    def display(self):
      print("\n========= Product Details ===========")
      print("Product Id:" , self.product_id)
      print("Product Name:" , self.name)
      print("Product Price:₹" , self.__price)


#child class

class Mobile(Product):

    def __init__(self , product_id , name , price , brand , ram , storage):

        super().__init__(product_id , name , price)

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def diaplay(self):

        super().dispaly()

        print("Product Brand:" , self.brand)
        print("Product RAM:" , self.ram , "GB")
        print("Product Storage:" , self.storage , "GB")


    def buy(self):
        print("\nOrder Placed Successfully!")
        print("Thank you for shopping with us.")


#Main porgram

mobile1 = Mobile(10,"ihone 18 pro max",150000,"Apple",12,2)
mobile2 = Mobile(11,"iphone 18 pro",130000,"Apple",12,1)
mobile3 = Mobile(12,"macbook air",180000,"Apple",16,8)

while True:

    print("\n========= E-commerce menu ============")
    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    if choice == 1:

        mobile1.display()
        mobile2.display()
        mobile3.display()

    elif choice == 2:

        print("Mobile 18 pro max Price : ₹", mobile1.get_price())
        print("Mobile 18 pro price : ₹", mobile2.get_price())
        print("macbook Current Price : ₹", mobile3.get_price())

    elif choice == 3:

        product_id = int(input("Enter Product ID: "))

        if product_id == mobile1.product_id:
            mobile1.set_price()
            
        elif product_id == mobile2.product_id:
              mobile2.set_price()
              
        elif product_id == mobile3.product_id:
              mobile3.set_price()

        else:
            print("Product Not Found!")

    elif choice == 4:

        product_id = int(input("Enter Product ID: "))

        if product_id == mobile1.product_id:
            mobile1.buy()
            
        elif product_id == mobile2.product_id:
            mobile2.buy()
            
        elif product_id == mobile3.product_id:
            mobile3.buy()

        else:
            print("Product Not Found!")

    elif choice == 5:

        print("Thank You!")
        break

    else:
        print("Invaild Choice")


              

























        
        
            
