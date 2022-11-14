from linear_regression import LinearRegression
import numpy as np
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96;1m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94;1m'
   GREEN = '\033[92;1m'
   YELLOW = '\033[93;1m'
   RED = '\033[91;1m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

if __name__ == "__main__":
   mileage = int(input(color.BOLD + "Enter the mileage of the vehicle\n>> " + color.END))
   coefs = os.popen("python3 linear_regression.py").read().split(",")
   nb = float((mileage - float(coefs[0])) / float(coefs[1])) #Convert to standarized
   nb = nb * float(coefs[2]) + float(coefs[3]) #Add coefs, transform to price
   if nb < 0:
      print(color.RED + "Mileage too high: impossible to predict a price." + color.END)
   else:
      print(color.BOLD + "Estimated price: " + color.GREEN + str(round(nb, 2)) + "$" + color.END)
