from encode import *

def cutter(file_name):
    filename = file_name
    data = file_encode(filename)
    start_index = data.find('<item rdf', 0)
    end_index = data.find('</item>', start_index)
    while(start_index != -1):
        mess = data[start_index:end_index + 7]
        mess, id, email_server = correction(mess)
        create_file(mess, id, email_server)
        start_index = end_index
        start_index = data.find('<item rdf', end_index)
        end_index = data.find('</item>', start_index)

cutter('support.sfedu.ru.txt')