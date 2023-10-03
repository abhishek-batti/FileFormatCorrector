from .cleaninglogic import jsoncleaning
from .cleaninglogic import xmlcleaning
from .cleaninglogic import parquetcleaning



def pass_to_formatter(file_list):

    ext = file_list[0].split('.')[1]
    if ext == "json" or ext == 'xml' or ext == "parquet":
        for x in file_list:
            if x.split('.')[1] != ext:
                return "File mismatch"
    
    if ext == "json":
        jsoncleaning.inp(file_list, "fileformatter/pool/logfile.txt")
    elif ext == "xml":
        xmlcleaning.inp(file_list, "fileformatter/pool/logfile.txt")
    elif ext == "parquet":
        parquetcleaning.inp(file_list, "fileformatter/pool/logfile.txt")

    return "Formatting Done"