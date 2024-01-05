"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

from datetime import datetime as dati
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dati.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dati.timestamp(today)
print(unix_epoch_time)

