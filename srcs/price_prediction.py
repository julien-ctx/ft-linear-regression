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
   option = input(color.BOLD + "Available options:\n- Type 'plot' to display the linear regression model\n- Type the mileage to display the estimated price\n>> " + color.END)
   if (option == "plot"):
      os.popen("python3 linear_regression.py plot")
   else:
      try:
         option = int(option)
      except Exception:
         print(color.RED + "Error: invalid mileage." + color.END)
         exit(1)
      if option < 0:
         print(color.RED + "Error: mileage must be a non null positive integer." + color.END)
         exit(1)
      coefs = os.popen("python3 linear_regression.py").read().split(",")
      price = float((option - float(coefs[0])) / float(coefs[1])) #Convert to standarized
      price = price * float(coefs[2]) + float(coefs[3]) #Add coefs, transform to price
      if price < 0:
         print(color.RED + "Mileage too high: impossible to predict a price." + color.END)
      else:
         print(color.BOLD + "Estimated price: " + color.GREEN + str(round(price, 2)) + "$" + color.END)
