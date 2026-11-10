"""
RECORD CHECK  -  my version
===========================

Name  :Dev Patel
Lane  :Cyber
Date  :04-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(r"Week 06 - Pandas\LAB\login_attempts.csv")

df["percent"] = (df["failed_logins"]/df["total_attempts"])*100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p>= 100 else "WARNING" if p>= 90 else "OK")
