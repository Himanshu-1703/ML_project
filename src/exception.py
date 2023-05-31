import sys


# function to print our custom error message
def error_message_detail(error):
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    message = str(error)
    error_message = f'Error occured in script name {file_name} ,line number {line_no} and error message is {error}'

    return error_message

# global exception handling
class CustomException(Exception):
    def __init__(self,error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error=error_message)
        

    def __str__(self) -> str:
        return self.error_message