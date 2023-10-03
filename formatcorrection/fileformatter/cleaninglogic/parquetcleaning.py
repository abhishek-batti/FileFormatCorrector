import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import numpy as np
def create_log_file(parquets_path, log_file_path):
    log_file = open(log_file_path, 'w+')
    all_fields = []
    for parquet_path in parquets_path:
        df = pd.read_parquet('fileformatter/pool/' + parquet_path)
        for col in df.columns:
            if col.title() not in all_fields:
                all_fields.append(col.title())
                log_file.write("NewTagFound:"+parquet_path + ": " + col.title() + " \n")
    
    log_file.close()
    del(all_fields)
    return log_file_path

def read_log_file(log_file_path):
    final_format = []
    logfile = open(log_file_path, 'r')
    
    for line in logfile:
        col = line.split()[1]
        final_format.append(col)
    
    logfile.close()
    return final_format

def append_missing_value(file_paths, log_file_path):
    
    for file_path in file_paths:
        all_fields = read_log_file(log_file_path)
        df = pd.read_parquet('fileformatter/pool/' + file_path)

        columns = []
        for col in df.columns:
            columns.append(col.title)
        
        for col in all_fields:
            if col not in columns:
                df[col.title()] = " "
        
        table = pa.Table.from_pandas(df)
        pq.write_table(table, 'fileformatter/pool/formatted_' + file_path, version= '1.0')
    
def inp(file_list, log_file_path):
    log_path = create_log_file(file_list, log_file_path)
    append_missing_value(file_list, log_path)