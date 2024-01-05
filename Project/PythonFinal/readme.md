# Configuration Change tracking on Cisco Switch 
- This program is a Python program designed to create a log file whenever there is any configuration change on a Cisco Switch.
- The program compares the latest "switch show run" configuration output with its previous output line by line. 
- If the latest configuration is different compared to previous configuration, a new log will be created with the date of change on the file name. If no changes were observed, No files are created. Instead it reports saying "The files are equal."

## Prerequisites
- Python 3.11.0

## Libraries Used
>difflib

>datetime

## About the Program:
1. This program will compare log files named "SwitchShow1" & "SwitchShow2" located in Source folder. 
2. The Log file is configuration of a Cisco Switch. The program compares both the log files line by line and creates a log file, if the configuration output differs between the files.
3. The new file is created in Tests folder in file format of "Switch_Show_Latest_DD-MMM-YYYY". The same file gets updated on dates whenever the configuration differs. 
4. The "Switch_Show_Latest_DD-MMM-YYYY" will report the lines using (+ & - symbols)  where changes were observed. These will help to idenfity the configuration changes made on the said date.
5. Lines with symbol "+" indicates the new configuration and Lines with symbol "-" indicates old configuration. This allows Network administrators to successfully identify and track the changes in the switches managed.

## Program and Location:
- "MainProgram" under Source folder.
- SwitchShow Logs for comparision is under Source folder. 

## Author
    Name: Sudharsan Vishvanath S Guptha
    ID: L00179143
    Contact: l00179143@atu.ie

## License
    This project is open source.