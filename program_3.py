# Author: Lucia Floan
# Date: Feb 28, 2025
# Title: Tax Rate

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# pseudocode:
# 1. Define calculate_taxes(total_sales)
#       a. calculate the state sales tax
#       b. calculate the county sales tax
#       c. calculate the total sales tax
#       d. return all the tax values
# 2. Ask the user for total_sales input
# 3. Call calculate_taxes(total_sales)
# 4. Print the final county sales tax, state sales tax, and total sales tax.

def calculate_taxes(total_sales):
  county_tax_rate = 0.025 # The amount of county sales tax.
  state_tax_rate = 0.05 # The amount of state sales tax.

  state_sales_tax = total_sales * state_tax_rate
  county_sales_tax = total_sales * county_tax_rate
  
  total_sales_tax = state_sales_tax + county_sales_tax # The total sales tax (county plus state)

  return state_sales_tax, county_sales_tax, total_sales_tax
# Use at least one function with input and output in this program
total_sales = float(input('Enter the total monthly sales: '))
state_sales_tax, county_sales_tax, total_sales_tax = calculate_taxes(total_sales)

print(f'The total county sales tax: ${county_sales_tax:.2f}')
print(f'The total state sales tax: ${state_sales_tax:.2f}')
print(f'The total sales tax (county + state): ${total_sales_tax:.2f}')
