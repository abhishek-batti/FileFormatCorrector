import lxml.etree as ET
from xml.dom import minidom

def create_log_file(xmls_path, log_file_path):
    log_file = open(log_file_path, 'w+')
    all_fields = []
    for xml_path in xmls_path:
        xml_path = 'fileformatter/pool/' + xml_path
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for row in root:
            for field in row:
                if str(field.tag) not in all_fields:
                    all_fields.append(str(field.tag))
                    log_file.write("NewTagFound:" + xml_path + ": " + str(field.tag) + " \n")
    
    log_file.close()
    del(all_fields)
    return log_file_path

def read_log_file(log_file_path):
    final_format = []
    logfile = open(log_file_path, 'r')
    
    for line in logfile:
        tag = line.split()[1]
        final_format.append(tag)
    
    logfile.close()
    return final_format

def prettify(tree):
    text = ET.tostring(tree)
    reparsed_text = minidom.parseString(text)
    return reparsed_text.toprettyxml(indent="\t")

def append_missing_value(file_paths, log_file_path):
    for file_path in file_paths:

        all_tags = read_log_file(log_file_path)
        
        tree = ET.parse('fileformatter/pool/' + file_path)
        root = tree.getroot()
        new_root = ET.Element(str(root.tag))

        for row in root:
            fields = []
            for field in row:
                fields.append(str(field.tag))
        
            for field in all_tags:
                if field not in fields:
                    ele = ET.Element(field)
                    ele.text = "Not present"
                    row.append(ele)
                    
            new_root.append(row)
        
        new_tree = ET.ElementTree(new_root)
        new_text = prettify(new_tree)
        new_root = ET.fromstring(new_text)
        new_tree = ET.ElementTree(new_root)
        print(new_tree)
        new_tree.write('fileformatter/pool/formatted_' + file_path)
        
def inp(file_list, log_file_path):
    log_path = create_log_file(file_list, log_file_path)
    append_missing_value(file_list, log_path)



                









