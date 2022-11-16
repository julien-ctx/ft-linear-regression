from linear_regression import LinearRegression, color
import numpy as np
import os

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
      price = float((option - float(coefs[0])) / float(coefs[1]))
      price = price * float(coefs[2]) + float(coefs[3])
      if price < 0:
         print(color.RED + "Mileage too high: impossible to predict a price." + color.END)
      else:
         print(color.BOLD + "Estimated price: " + color.CYAN + str(round(price, 2)) + "$" + color.END)
         print(color.BOLD + "Accuracy: " + color.CYAN + str(round(float(coefs[4]), 2)) + "%")
