"""App Functions"""
import pandas as pd #pandas for csv and dataframe management

def get_file_header(opened_file=None, errorlog=None):
    file_header = {}
    account_id = None
    #Don't want to read the whole file in case it is very large
    for row_counter, line in enumerate(opened_file):
        #Start the counter at 1, since most csv files start at 1
        row_counter = row_counter + 1 
        #Store the line content by row count
        file_header[row_counter] = line.split(',')

        #Get the first item in the row
        if len(file_header[row_counter]) > 0:
            if file_header[row_counter][0].strip() == 'Account ID':
                account_id = file_header[row_counter][1].replace('\n','')

            if file_header[row_counter][0] == 'Report Fields\n':
                end_of_header_found = True
                break
            else:
                end_of_header_found = False
    
    return {
        'header':file_header
        , 'end_of_header_found':end_of_header_found
        , 'account_id':account_id}

def get_file_body(opened_file = None):
    try:
        file_body = pd.read_csv(opened_file)
        file_body.columns = [col.strip() for col in file_body.columns]
    except Exception as e:
        print(e)
        file_body = 'nothing'

    #Column Order can vary so best way to remove grand total is to drop the last row
    #Assert that last row is grand total
    if 'Grand Total' in str(file_body.tail(1)):
        file_footer_found = True
        file_body = file_body.iloc[:len(file_body)-1, :]
        #file_body = file_body.drop(file_body.tail(1).index,inplace=True)
    else:
        file_footer_found = False
        #if the footer is not found we can still proceed to store the file
        #requirements dont specify how relaxed we should be on this, so will attempt to proceed

    return {'body':file_body, 'file_footer_found':file_footer_found}

def add_account_id_to_body(file_body = None, account_id = None):
    file_body['Account ID'] = account_id

    return file_body


            


