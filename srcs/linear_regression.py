import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

class LinearRegression:

	def __init__(self, alpha = 0.01, max_i = 100000):
		self.thetas = np.array([[0.], [0.]]).astype(float)
		self.alpha = alpha
		self.max_i = max_i
	
	def add_intercept(self, x):
		if not isinstance(x, (np.ndarray, np.generic)):
			return None
		if not x.size:
			return None
		if x.ndim == 1:
			x = x[:,np.newaxis]
		ones = np.ones((len(x), 1))
		return np.hstack((ones, x))

	def predict_(self, x):
		if not isinstance(x, (np.ndarray, np.generic)):
			return None
		return np.array(self.add_intercept(x) @ self.thetas)

	def gradient(self, x, y, theta):
		xp = self.add_intercept(x)
		xpt = xp.T
		# print(xpt)
		# print()
		# print(xp @ theta - y)
		return np.array((xpt @ (xp @ theta - y)) / y.size)
	
	def gradient_descent(self, x, y):
		for _ in range(self.max_i):
			self.thetas = self.thetas - self.alpha * self.gradient(x, y, self.thetas)
		return self.thetas

	@staticmethod
	def mse_(y, y_hat):
		return np.average((y_hat - y) ** 2)

if __name__ == "__main__":
	dataset = pd.read_csv("../assets/data.csv")
	x = np.array(dataset['km']).reshape(-1, 1).astype(float)
	y = np.array(dataset['price']).reshape(-1, 1).astype(float)
	model = LinearRegression()
	thetas = model.gradient_descent(x, y)
	print(thetas)