Louder Data Engineering Skills Assessment
=========================================

Overview
--------

This is a tool to convert a Campaign Manager report file into a valid CSV file.

app_config.yaml contains the application's current configuration
app.py contains the application code
app_test.py contains test functions
app_func.py contains application functions  

Note this application requires python 3.10.5

How to run the application
--------

0. Pip install any dependancies found in requirements.txt

1. Update app_config.yaml by default this will contains 5 sample files for testing.

2. run app.py using python (python app.py)

3. Review the error log if any errors occur

4. The application will output any files that had no errors to output.csv
Note: if more than one file was specified in app_config.yaml, than more that one output file will be generated. Output files will have a number postfix that corresponds to the order specified in the app_config.yaml.

Transformations Performed
------------------------
1. remove header rows (up to and including the row starting `Report Fields`)
2. remove the total row at the end
3. return the remaining data rows in valid csv format will all supplied fields 
4. add an extra column containing the account id (containing the number taken from the relevant header)
5. save in a file `output.csv` 

Notes:
- the number of header rows in a report varies dependant on the report criteria
- the number and order of columns in the report are depend on the report definition
- fields with containing currency values will include the word `Cost` in the column heading 
------------------------

testing 123