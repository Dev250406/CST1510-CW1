"""
RECORD CHECK  -  my version
===========================

Name  :Dev Patel
Lane  :Cyber
Date  :21-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize a new Record instance with label, value, and limit attributes."""
        self.label = label
        self.value = value
        self.limit = limit
        
    def difference(self):
        """Calculate and return the remaining headroom logic gap."""
        return self.limit - self.value

    def percent(self):
        """Calculate and return the raw failure percentage score."""
        return (self.value / self.limit) * 100

    def status(self):
        """Determine and return 'OVER LIMIT', 'WARNING', or 'OK' based on threshold."""
        percent = self.percent()
        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

with open("C:/Users/jayes/Documents/CST1510_CW1/Week 05 - Classes and Objects/LAB/results.txt", "w") as out_file:
    for record in records:
        current_status = record.status()
        
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {record.label}")
        print("=" * 34)

        print(f"{'Failed Logins':<17} :{record.value:>10.2f}")
        print(f"{'Total Logins':<17} :{record.limit:>10.2f}")
        print(f"{'Succesful Logins':<17} :{record.difference():>10.2f}")
        print(f"{'Failure Percent':<17} :{record.percent():>10.2f}%")
        print(f"{'Status':<17} : {current_status:>9}")
        print("=" * 34)

        out_file.write(f"{record.label},{current_status}\n")

print()
print(f"Failed Logins over limit : {Record.over_limit_count}")