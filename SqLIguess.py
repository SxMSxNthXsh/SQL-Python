
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thunder",
    database="sam"
)


def Inp():
    while True:
      A = int(input("SCode:"))
      B = input("SName:")
      C = int(input("Value:"))
      D = int(input("Stock:"))
      E = input("Date:")

      mycursor = mydb.cursor()
      sql = ("insert into items (SCode,SName,Value,Stock,UpdatedDate) values(%s,%s,%s,%s,%s)")
      val = (A, B, C, D, E)
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted")
      Ca = input("Enter more record? (Y/N):")
      if Ca in "nN":
        break


def Update():
    mycursor = mydb.cursor()

    while True:
      print("1.Update SCode")
      print("2.Update SName")
      print("3.Update Values")
      print("4.Update Stock")
      print("5.Update Date")
      print("6.Exit")
      NO = (1, 2, 3, 4, 5, 6)

      UChoice = int(input("Enter your choice:"))
      if UChoice not in NO:
          print("Enter the correct value!!")
      if UChoice == 1:
          OldSCode = int(input("Enter the old SCode:"))
          NewSCode = int(input("Enter the new SCode:"))
          sql1 = ("update items set SCode=%s where SCode=%s")
          val1=(NewSCode,OldSCode)
          mycursor.execute(sql1,val1)

          mydb.commit()

          print(mycursor.rowcount, "Records Updated")

      elif UChoice == 2:
          OldSName = input("Enter the old SName:")
          NewSName = input("Enter the new SName:")
          sql2 = ("update items set SName=%s where SName=%s")
          val2 = (NewSName,OldSName)
          mycursor.execute(sql2, val2)

          mydb.commit()

          print(mycursor.rowcount, "Records Updated")

      elif UChoice == 3:
          OldValue = int(input("Enter the old Value:"))
          NewValue = int(input("Enter the new Value:"))
          sql3 = ("update items set Value = %s where Value = %s")
          val3=(NewValue,OldValue)
          mycursor.execute(sql3,val3)

          mydb.commit()

          print(mycursor.rowcount, "Records Updated")

      elif UChoice == 4:
          OldStock = int(input("Enter the old Stock:"))
          NewStock = int(input("Enter the new Stock:"))
          sql4 = ("update items set Stock=%s where Stock=%s")
          val4=(NewStock,OldStock)
          mycursor.execute(sql4,val4)

          mydb.commit()

          print(mycursor.rowcount, "Records Updated")

      elif UChoice == 5:
          OldDate= input("Enter the old Date:")
          NewDate = input("Enter the new Date:")
          sql5= ("update items set UpdatedDate=%s where UpdatedDate=%s")
          val5=(NewDate,OldDate)
          mycursor.execute(sql5,val5)

          mydb.commit()

          print(mycursor.rowcount, "Records Updated")

      elif UChoice == 6:
          CCC=input("Do you want to exit? (Y/N):")
          if CCC in "yY":
            print("Exiting Update Menu")
            break

      else:
          print("Enter correct value!!")

      



def Remove():
        
        mycursor = mydb.cursor()
        while True:
          print("1.Remove SName")
          print("2.Remove Values")
          print("3.Remove Stock")
          print("4.Remove Date")
          print("5.Exit")
          Nu = (1, 2, 3, 4, 5)
          v = 0
          N = "null"
          RChoice = int(input("Enter your choice:"))
          if RChoice not in Nu:
              print("Enter the correct choice!!")


          if RChoice == 1:
              RemSName = input("Enter the SName to remove:")
              sql7 = ("update items set SName=%s where SName=%s")
              val7=(N,RemSName)
              mycursor.execute(sql7,val7)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 2:
              RemValue = int(input("Enter the Value to remove:"))
              sql8 = ("update items set Value=%s where Value=%s")
              val8=(v,RemValue)
              mycursor.execute(sql8,val8)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 3:
              RemStock = int(input("Enter the Stock to remove:"))
              sql9 = ("update items set Stock=%s where Stock=%s")
              val9=(v,RemStock)
              mycursor.execute(sql9,val9)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 4:
              RemDate = input("Enter the Date to remove:")
              sql10 = ("update items set UpdatedDate=%s where UpdatedDate=%s")
              val10=(N,RemDate)
              mycursor.execute(sql10,val10)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 5:
              RRR=input("Do you want to exit? (Y/N):")
              if RRR in "yY":
                print("Exiting Remove Menu")
                break
          
          else: 
              print("Enter the correct value!!")


def Check():
        mycursor = mydb.cursor()
        while True:
          print("1.Check SCode")
          print("2.Check SName")
          print("3.Check Values")
          print("4.Check Stock")
          print("5.Check Date")
          print("6.Exit")
          Nom = (1, 2, 3, 4, 5, 6)
          CChoice = int(input("Enter your choice:"))
          if CChoice not in Nom:
              print("Enter the correct choice!!")
          if CChoice == 1:
              ChScode = int(input("Enter the SCOde to check:"))
              TSCode=("SCode")
              sql11 = ("select %s from items where SCode=%s")
              val11=(TSCode,ChScode)
              mycursor.execute(sql11,val11)
              data=mycursor.fetchone()
              for row in data:
                print(row)
                mydb.commit()

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 2:
              ChSName = input("Enter the SName to check:")
              TSName="SName"
              sql12 = ("select %s from items where SName=%s")
              val12=(TSName,ChSName)
              mycursor.execute(sql12,val12)
              data=mycursor.fetchmany(34)
              for row in data:
                print(row)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 3:
              ChValue = int(input("Enter the Value to remove:"))
              sql13 = ("select Value from items where Value=%s")
              val13=(ChValue)
              mycursor.execute(sql13,val13)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 4:
              ChStock = int(input("Enter the Stock to remove:"))
              sql14 = ("select stock from items where stock=%s")
              val14=(ChStock)
              mycursor.execute(sql14,val14)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 5:
              ChDate = input("Enter the Date to be remove:")
              sql15 = ("select updateddate from items where updateddate=%s")
              val15=(ChDate)
              mycursor.execute(sql15,val15)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 6:
              ddd=input("Do you want to exit? (Y/N):")
              if ddd in "yY":
                print("Exiting the Check Menu")
                break
          else: 
              print("Enter the correct value!!")

def Employee():
  while True:
    print("1.Input A New Item")
    print("2.Update the Item")
    print("3.Remove the Item")
    print("4.Check the item")
    print("5.Exit the program")
    NN = (1, 2, 3, 4, 5)
    Coice = int(input("Enter your choice:"))
    if Coice not in NN:
        print("Enter the correct value!!")
    if Coice == 1:
        Inp()
    elif Coice == 2:
        Update()
    elif Coice == 3:
        Remove()
    elif Coice == 4:
        Check()
    elif Coice == 5:
        abcd=input("Do you want to exit? (Y/N):")
        if abcd in "yY":
          print("Exiting the program!!")
          break




def User():
     while True:
        print("1.Input A New Item")
        print("2.Update the Item")
        print("3.Remove the Item")
        print("4.Check the item")
        print("5.Exit the program")
        NN = (1, 2, 3, 4, 5)
        Cooice = int(input("Enter your choice:"))
        if Cooice not in NN:
            print("Enter the correct value!!")
        if Cooice == 1:
            Inp()
        elif Cooice == 2:
            Update()
        elif Cooice == 3:
            Remove()
        elif Cooice == 4:
            Check()
        elif Cooice == 5:
            abcd=input("Do you want to exit? (Y/N):")
            if abcd in "yY":
                print("Exiting the program!!")
            break

def View():
    print("1.View Market")
    print("2.View Purchased")
    print("3.Exit View")
    Nooo=(1,2,3)
    AAbb=int(input("Enter your choice:"))
    if Nooo not in AAbb:
        print("Enter the correct value!!")

    if AAbb==1:
        mycursor = mydb.cursor()
        mycursor.execute("select * from items")
        print("Table values are:")
        print("__________________")
        data=mycursor.fetchall()
        count=mycursor.rowcount
        for row in data:
            print(row)


    if AAbb==2:
        mycursor.execute("select * from user")
        print("Table values are:")
        print("__________________")
        data=mycursor.fetchall()
        count1=mycursor.rowcount
        for row1 in data:
            print(row1)

    
    if AAbb == 3:
        while True:
            abcde = input("Do you want to exit? (Y/N):")
            if abcde in "yY":
                print("Exiting the program!!")
            break

            
def Buy():
    while True:
        print("Buy Option")
        mycursor = mydb.cursor()
        mycursor.execute("select SName from items")
        print("Here are the stock!!")
        print("__________________")
        print("  ")
        data=mycursor.fetchall()
        count=mycursor.rowcount
        for row in data:
            print(row)
        print("__________________")
        print("Which Stock You are going to buy?")
        BName = input("Enter the Stock Name:")
        BStock=int(input("Enter how much stock to buy:"))

        # Define the value before executing the SQL statement
        val16 = (BName,)  # Define val16 with the tuple

        sql16 = "INSERT INTO user (StockCode, StockName, Value, YourStock) SELECT SCode, SName, Value, Stock FROM items WHERE SName = %s"
        mycursor.execute(sql16, val16)

        mydb.commit()  # Commit the changes
        BName = "YourName"  # Example value for BName

        val18 = (BName,)  # Define val18 with the tuple

        sql18 = "SELECT Stock FROM items WHERE SName = %s"
        mycursor.execute(sql18, val18)
        result = mycursor.fetchone()
        if result:
            VV = result[0]
            print(VV)
        else:
            VV = None
            print("No result found.")

        BStock = "YourNewStock"  # Example value for BStock
        val17 = (BStock, VV)

        sql17 = "UPDATE user SET YourStock = %s WHERE YourStock = %s"
        mycursor.execute(sql17, val17)

        mydb.commit()
        

        YrN = input("Want to buy again?(Y/N):")
        if YrN in "nNNOno":
                    break
     

Buy()

