
import json
import pandas as pd
#comparing each row
def create_log_file(file_paths, log_file_path):
    format = []
    logfile = open(log_file_path, 'w+')
    for file_path in file_paths:
        with open('fileformatter/pool/' + file_path, 'r') as fi:
            db = json.load(fi)
            for table in db:
                for row in db[table]:
                    for key in row:
                        if (str(key) + " " + str(type(row[key]))) not in format:
                            format.append(str(key) + " " + str(type(row[key])))
                            logfile.write("NewKeyFound:"+file_path + ": " + str(key) + " " + str(type(row[key]))+ ' \n')

    logfile.close()
    del(format)
    return log_file_path
    

#Reading the log file
def read_log_file(log_file_location):
    final_format = []
    logfile = open(log_file_location, 'r')

    for line in logfile:
        if line != "\n":
            key_datatype = ((line.split(': ', 2))[1]).split(' \n')[0]
            
            final_format.append(key_datatype)
    logfile.close()
    return final_format

#appending the fields that are not present in the row

def get_value(dt):
    if dt == "str":
        return ""
    elif dt == "int":
        return 0
    elif dt == "float":
        return 0.0



def append_missing_values(logfile_loc, file_paths):
    for file_path in file_paths:
        in_file = open('fileformatter/pool/' + file_path, 'r')
        out_file = open('fileformatter/pool/'+ "formatted_" + file_path, 'w+')
        table_data = []
        final_format = read_log_file(logfile_loc)
        in_db = json.load(in_file)
        for table in in_db:
            for row in in_db[table]:
                keys = []
                for key in row:
                    keys.append(str(key) + " " + str(type(row[key])))
                missing = [k for k in final_format if k not in keys]
                    # print(missing)

                for m in missing:
                    key = m.split()[0]
                    data_type = m.split()[2]
                    data_type = data_type.strip("'>")
                    val = get_value(data_type)
                    row.update({key: val})
                table_data.append(row)
            json.dump({table: table_data}, out_file, indent=4)
            in_file.close()
            out_file.close()

# def clean_files():
#     open("log_file.txt", 'w+').close()
#     open("file2.json", 'w+').close()

#change to all file convert
def inp(file_list, log_file_path):
    log_loc = create_log_file(file_list, log_file_path)
    append_missing_values(log_loc, file_list)




        
            

