from linear_regression import LinearRegression, color
import numpy as np
import sys

if __name__ == "__main__":
   option = input(color.BOLD + "Type the mileage to display the estimated price\n>> " + color.END)
   try:
      option = int(option)
   except Exception:
      sys.exit(color.RED + "Error: invalid mileage." + color.END)
   if option < 0:
      sys.exit(color.RED + "Error: mileage must be a non null positive integer." + color.END)
   try:
      with open('training_results.txt', 'r') as f:
         coefs = f.read().split(',')
   except Exception as e:
      sys.exit(color.RED + "Error: predicted price is 0$ because model has not been trained!" + color.END)
   try:
      coefs = [float(x) for x in coefs]
      if len(coefs) != 5:
         raise()
   except Exception as e:
      sys.exit(color.RED + "Error: bad syntax for linear regression training data." + color.END)
   price = float((option - float(coefs[0])) / float(coefs[1]))
   price = price * float(coefs[2]) + float(coefs[3])
   if price < 0:
      print(color.RED + "Mileage too high: impossible to predict a price." + color.END)
   else:
      print(color.BOLD + "Estimated price: " + color.CYAN + str(round(price, 2)) + "$" + color.END)
      print(color.BOLD + "Accuracy: " + color.CYAN + str(round(float(coefs[4]), 2)) + "%")
