"""
RECORD CHECK  -  my version
===========================

Name  : DEV PATEL
Lane  : Cyber     
Date  :21/09/2026

Run it:   python template.py

"""
label = input("Enter a SOURCE IP: ")
first = float(input("Enter the FAILED LOGIN: "))
second = float(input("Enter the TOTAL ATTEMPTS: "))

difference = first - second 
percent = (first / second) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Failed Login:    {first:>10.2f}")
print(f" Total Attempts:   {second:>10.2f}")
print(f" Difference:     {difference:>+10.2f}")
print(f" Percentage:     {percent:>10.2f}%")
print(f" Summary:        Record processed.") 

print("=" * 34)