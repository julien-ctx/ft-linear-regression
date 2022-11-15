import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

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

class LinearRegression:

	def __init__(self, mean = None, std = None, alpha = 0.001, max_i = 10000):
		self.thetas = np.array([[0.], [0.]])
		self.alpha = alpha
		self.max_i = max_i
		if not mean or not std:
			sys.exit(color.RED + "Error: no mean/std provided on model's instance" + color.END)
		self.mean = np.mean(x)
		self.std = np.std(x)
		self.loss_x = []
		self.loss_y = []
	
	def add_intercept(self, x):
		if not isinstance(x, (np.ndarray, np.generic)):
			return None
		if not x.size:
			return None
		if x.ndim == 1:
			x = x[:,np.newaxis]
		ones = np.ones((len(x), 1))
		return np.hstack((ones, x))

	def gradient(self, x, y, theta):
		xp = self.add_intercept(x)
		xpt = xp.T
		return np.array((xpt @ (xp @ theta - y)) / y.size)
	
	def gradient_descent(self, x, y, old_x):
		i = 0
		for _ in range(self.max_i):
			i += 1
			self.loss_x.append(i)
			self.loss_y.append(self.mse(y, (((old_x - self.mean) / self.std) * self.thetas[1] + self.thetas[0])))
			self.thetas = self.thetas - self.alpha * self.gradient(x, y, self.thetas)
		return self.thetas

	def plot(self, old_x, x, y):
		figure, axis = plt.subplots(1, 2)
		axis[0].scatter(old_x, y)
		axis[0].plot(old_x, x * self.thetas[1] + self.thetas[0], 'r')
		axis[0].set_title("Linear Regression")
		axis[0].set_xlabel("Mileage (km)")
		axis[0].set_ylabel("Price ($)")
		axis[1].plot(self.loss_x, self.loss_y, 'b')
		axis[1].set_title("Loss")
		axis[1].set_xlabel("Iterations")
		axis[1].set_ylabel("Mean Squared Error (MSE)")
		plt.tight_layout()
		plt.show()

	def mse(self, y, y_hat):
		return np.average((y_hat - y) ** 2)

	@staticmethod
	def standardize(x):
		return (x - np.mean(x)) / np.std(x)
	
if __name__ == "__main__":
	dataset = pd.read_csv("../assets/data.csv")
	x = np.array(dataset['km']).reshape(-1, 1).astype(float)
	y = np.array(dataset['price']).reshape(-1, 1).astype(float)
	model = LinearRegression(np.mean(x), np.std(x))
	old_x = x
	x = LinearRegression.standardize(x)
	thetas = model.gradient_descent(x, y, old_x)
	if len(sys.argv) == 1:
		print(f"{model.mean},{model.std},{int(thetas[1])},{int(thetas[0])}")
	elif (sys.argv[1] == 'plot'):
		model.plot(old_x, x, y)
