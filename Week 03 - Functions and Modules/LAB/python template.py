"""
RECORD CHECK  -  my version
===========================

Name  :DEV PATEL 
Lane  :Cyber
Date  :07/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted

difference = 0.0   # replace with your code
percent = 0.0       # replace with your code
status = ""          # replace with your code

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print("=" * 34)

label = input("Enter a SOURCE IP: ")
first = float(input("Enter the FAILED LOGIN: "))
second = float(input("Enter the TOTAL ATTEMPTS: "))

difference = first - second 
percent = (first / second) * 100
status = "OK" if percent < 90 else "WARNING" if percent < 100 else "OVER LIMIT"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Failed Login:    {first:>10.2f}")
print(f" Total Attempts:   {second:>10.2f}")
print(f" Difference:     {difference:>+10.2f}")
print(f" Percentage:     {percent:>10.2f}%")
print(f" Status:        {status:>10}") 

print("=" * 34)