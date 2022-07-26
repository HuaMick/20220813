Louder Data Engineering Skills Assessment
=========================================

Overview
--------

Write a tool to convert a Campaign Manager report file into a valid CSV file.

Input - see `example.csv` in this repo

Transforamtions required
------------------------

1. remove header rows (up to and including the row starting `Report Fields`)
2. remove the total row at the end
3. return the remaining data rows in valid csv format will all supplied fields 
4. add an extra column containing the account id (containing the number taken from the relevant header)
5. save in a file `output.csv` 

Additional information that may be relevant
-------------------------------------------

Several types of Campaign Manager reports in use
- the number of header rows in a report varies dependant on the report criteria
- the number and order of columns in the report are depend on the report definition
- fields with containing currency values will include the word `Cost` in the column heading 

How to complete this task
-------------------------

1. Clone this repo
2. Write your code 
3. Share your cloned repo