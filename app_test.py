"""App Tests"""
import os

def check_path_points_to_csv(errorlog, file_id = None, filepath=None):
    """Check source file type is csv"""
    path, extension = os.path.splitext(filepath)
    try:
        assert extension == '.csv' 
    except AssertionError:
        errorlog['file_id'].append(file_id)
        errorlog['source_file_path'].append(filepath)
        errorlog['test_applied'].append(check_path_points_to_csv.__doc__)
        errorlog['error_message'].append(
            f"no .csv extension detected, please check the path points to a valid csv file")


def check_end_of_file_header_found(errorlog, file_id = None, filepath = None, end_of_header_found=None):
    """Check that the end of the file header was found"""
    #"Report Fields" flags the end of the file header
    try:
        assert end_of_header_found
    except AssertionError:
        errorlog['file_id'].append(file_id)
        errorlog['source_file_path'].append(filepath)
        errorlog['test_applied'].append(check_end_of_file_header_found.__doc__)
        errorlog['error_message'].append(
            f"Cound not find 'Report Fields' line in file. This is used to flag the end of the file header")

def check_file_header_contains_account_id(errorlog, file_id = None, filepath = None, account_id=None):
    """Check that account id exists in the header"""
    #"Report Fields" flags the end of the file header
    try:
        assert account_id != None
    except AssertionError:
        errorlog['file_id'].append(file_id)
        errorlog['source_file_path'].append(filepath)
        errorlog['test_applied'].append(check_file_header_contains_account_id.__doc__)
        errorlog['error_message'].append(
            f"Cound not find Account ID in header. This is needed for the account id field to be generated")


def check_file_footer_found(errorlog, file_id = None, filepath = None, file_footer_found=None):
    """Check that the the file footer was found"""
    #"Grand Total" flags the file footer
    try:
        assert file_footer_found
    except AssertionError:
        errorlog['file_id'].append(file_id)
        errorlog['source_file_path'].append(filepath)
        errorlog['test_applied'].append(check_file_footer_found.__doc__)
        errorlog['error_message'].append(
            f"Cound not find 'Grand Total' line in file. This is the expected file footer")




