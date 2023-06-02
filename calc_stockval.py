# calculate stock value increase/decrease

daShareval = float(input("Enter the per share stock price: "))
daShares = float(input("Enter the number of shares purchased: "))

daTotShareval = (daShareval * daShares)
print("The original total share value is", daTotShareval)

danewShareval = float(input("Enter the new per share stock price: "))
danewStockvaltot = (danewShareval * daShares)

print("The current total share value is", danewStockvaltot)

daStockvalinc = (danewStockvaltot - daTotShareval)
print("The increase in stock value is:", daStockvalinc)

daPercgain = ((daStockvalinc / daTotShareval) * 100)
print("The percent increase in stock value is:", daPercgain)

# Total stock share increase

#print("Original total share value", daTotShareval)
#print("Total stock share increase", daStockvalinc)