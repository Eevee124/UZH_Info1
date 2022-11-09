#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def max_profit(prices):
	if not type(prices) == list:
		return "Invalid Input Type"
	
	if prices == []:
		return "Empty Price List"
	
	if not all(isinstance(item, int) for item in prices):
		return "Invalid Data Type within List"

	if not all(item >= 0 for item in prices):
		return "Invalid Prices"
	
	if len(prices) == 1:
		return 0
	
	max = 0
	for i in range(len(prices) - 1):
		for j in range(i, len(prices)):
			if prices[i] < prices[j]:
				if max < (prices[j] - prices[i]):
					max = prices[j] - prices[i]

	return max
