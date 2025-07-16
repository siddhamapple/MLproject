import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() 
    #Traceback object shows exactly where your code failed in exc_info , 3rd element of tuple is traceback object]
    # this calls exc info from sys module which has 3 things -> exception type, exception value, traceback object
    #traceback object contains information about where (in what file, at what line) the error happened, and how Python got there (the call stack).
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message="Error occured at [{0}] & at line number [{1}] and error message is [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_message_detail:sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
