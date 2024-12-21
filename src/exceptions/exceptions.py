import sys
#sys module helps to trace execution and this makes to understand exceptions easier
#Exception is parent class
class custom_exception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exe_tb=error_details.exc_info()
        print(exe_tb)
        
        self.lineno=exe_tb.tb_lineno
        self.file_name=exe_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))

if __name__ == '__main__':
    try:
        a=1/0
        
    except Exception as e:
        raise custom_exception(e,sys)
        