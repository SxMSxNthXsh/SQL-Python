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
          sql5= ("update items set UpdatedDate='%s' where UpdatedDate='%s'")
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
          print("1.Remove the whole item")
          print("2.Remove SName")
          print("3.Remove Values")
          print("4.Remove Stock")
          print("5.Remove Date")
          print("6.Exit")
          Nu = (1, 2, 3, 4, 5, 6)
          v = 0
          N = "Null"
          RChoice = int(input("Enter your choice:"))
          if RChoice not in Nu:
              print("Enter the correct choice!!")

          if RChoice == 1:
              RemSC = int(input("Enter the SName to remove the whole item:"))
              sql6 = ("delete from items where SCode=%s")
              val6=(RemSC)
              mycursor.execute(sql6,val6)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 2:
              RemSName = input("Enter the SName to remove:")
              sql7 = ("update items set SName=%s where SName=%s")
              val7=(N,RemSName)
              mycursor.execute(sql7,val7)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 3:
              RemValue = int(input("Enter the Value to remove:"))
              sql8 = ("update items set Value=%s where Value=%s")
              val8=(v,RemValue)
              mycursor.execute(sql8,val8)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 4:
              RemStock = int(input("Enter the Stock to remove:"))
              sql9 = ("update items set Stock=%s where Stock=%s")
              val9=(v,RemStock)
              mycursor.execute(sql9,val9)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 5:
              RemDate = input("Enter the Date to remove:")
              sql10 = ("update items set UpdatedDate=%s where Date=%s")
              val10=(N,RemDate)
              mycursor.execute(sql10,val10)
              mydb.commit()

              print(mycursor.rowcount, "Records Updated")

          elif RChoice == 6:
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
              TSCode=input("Which Column:")
              sql11 = ("select %s from items where SCode=%s")
              val11=(TSCode,ChScode)
              mycursor.execute(sql11,val11)
              data=mycursor.fetchall()
              for x in data:
                  print(x)

              print(mycursor.rowcount, "Records Updated")
          elif CChoice == 2:
              ChSName = input("Enter the SName to check:")
              sql12 = ("select SName from items where SName=%s")
              val12=(ChSName)
              mycursor.execute(sql12,val12)
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

Employee()