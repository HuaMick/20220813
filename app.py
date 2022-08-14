
#C:\Users\mickh\OneDrive\01_Developer\02_Python\louder-data-eng-task\.venv\Scripts\activate.ps1

"""
& c:/Users/mickh/OneDrive/01_Developer/02_Python/louder-data-eng-task/.venv/Scripts/python.exe -i `
c:/Users/mickh/OneDrive/01_Developer/02_Python/louder-data-eng-task/app.py
"""

import app_test #This is the testing module
import app_func #This is where the app's functions are
import yaml #yaml is used to load the config file
import pandas as pd #Used to convert error log into a dataframe

errorlog = {
    'file_id':[]
    , 'source_file_path': []
    , 'test_applied': []
    , 'error_message': []
}

from yaml.loader import SafeLoader
# Open the file and load the file
with open('app_config.yaml') as f:
    app_config = yaml.load(f, Loader=SafeLoader)

file_store = {}
for file_id, file_config in enumerate(app_config['files']):
    file_store[file_id] = {
        'filepath':file_config['filepath']
        , 'file_header':None
        , 'file_body':None
    }

    app_test.check_path_points_to_csv(
        errorlog
        , file_id=file_id
        , filepath = file_store[file_id]['filepath'])

    with open(file_store[file_id]['filepath'],'r') as file:
        payload = app_func.get_file_header(opened_file = file)
        file_store[file_id]['file_header'] = payload['header']
        file_store[file_id]['account_id'] = payload['account_id']

        app_test.check_end_of_file_header_found(
            errorlog
            , file_id=file_id
            , filepath = file_store[file_id]['filepath']
            , end_of_header_found=payload['end_of_header_found'])
        
        app_test.check_file_header_contains_account_id(
            errorlog
            , file_id=file_id
            , filepath = file_store[file_id]['filepath']
            , account_id = file_store[file_id]['account_id'])

        #cursor maintains position so read csv will start at the correct header row.
        ## If Header Row Found then get data body ##
        if payload['end_of_header_found']:
            payload = app_func.get_file_body(opened_file = file)
          
            app_test.check_file_footer_found(
                errorlog
                , file_id=file_id
                , filepath = file_store[file_id]['filepath']
                , file_footer_found=payload['file_footer_found'])

            ## If Account ID Exists then Add it to Body ##
            if file_store[file_id]['account_id'] != None and type(payload['body']) != str:
                file_store[file_id]['file_body'] = app_func.add_account_id_to_body(
                    file_body = payload['body']
                    , account_id = file_store[file_id]['account_id'])

            else:
                #Adding the Account ID is a specified requirement, so failure results in skipping file
                file_store[file_id]['file_body'] = None 
        else:
            #No End of Header found in file, store nothing and skip file
            file_store[file_id]['file_body'] = None 

errorlog = pd.DataFrame(errorlog)
if len(errorlog) > 0:
    print("\n Source file errors found, see below... \n")
    with pd.option_context(
        'display.max_rows', None
        , 'display.max_columns', None
        , 'display.max_colwidth', 100):
        print(errorlog)

for file_id, file in file_store.items():
    if file_id not in list(errorlog['file_id']):
        file['file_body'].to_csv(f'sample_{file_id}.csv',index=False)

#         """File Content"""
#         
#         #(Its reading down from where it left off)
#         #Assert that the header contains the following columns..
#         file_info[file_ID]['body'] = pd.read_csv(file)
#         file_info[file_ID]['body'] = file_info['body'][file_info['body']['Date']!='Grand Total:']
#         #Add the Account ID Field

#         file_info['body']['Account ID'] = int(file_info['file_header'][5][1].replace('\n','')) 

#         #Need to make sure the columns are in a standard order

# from pprint import pprint
# pprint(source_files)

# if key != 'Report Fields\n':
#     file_info['header'][row_counter] = next(file).split(',')
# else:
#     break


