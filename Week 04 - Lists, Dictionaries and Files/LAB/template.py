"""
RECORD CHECK  -  my version
===========================

Name  : Dev Patel
Lane  : Cyber
Date  : 

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

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

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "A-100", "value": 45.5, "limit": 50.0},
    {"label": "A-101", "value": 55.0, "limit": 50.0},
    {"label": "A-102", "value": 10.0, "limit": 20.0},
]


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )
    print_report(record, difference, percent, status)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
