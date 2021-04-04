import io
import chardet
import os
import html


def file_encode(filename):
    bytes = min(32, os.path.getsize(filename))
    raw = open(filename, 'rb').read(bytes)
    result = chardet.detect(raw)
    encoding = result['encoding']
    infile = io.open(filename, 'r', encoding=encoding)
    data = html.unescape(infile.read())
    return data

def correction(mess):
    mess = mess.replace('&#34;', '"')
    mess = mess.replace('&#40;', '(')
    mess = mess.replace('&#41;', ')')
    id = mess[mess.find('id=') + 3: mess.find('"', mess.find('id='))]
    theme = mess[mess.find('<title>') + 7: mess.find('</title>')]
    discription = mess[mess.find('<description>') + 13: mess.find('</description>')]
    creator = mess[mess.find('<dc:creator>') + 12: mess.find('<', mess.find('<dc:creator>') + 1)]
    if creator != '':
        email = mess[mess.find(creator) + len(creator) + 1: mess.find('</dc:creator>') - 1]
    else:
        email = mess[mess.find('<dc:creator>') +13 : mess.find('</dc:creator>') - 1]

    server = email[email.find('@') + 1: len(email)]
    mess = 'ID: %s\nemail: %s\nИмя создателя: %s\nТема: %s\nТекст: %s' %(id, email, creator, theme, discription)
    #print(mess)
    return mess, id, server

def create_file(mess, id, server):
    sub_folder = ''
    if server == 'sfedu.ru':
        sub_folder = 'sfedu'
    elif server == 'grade.sfedu.ru':
        sub_folder = 'grade'
    else:
        sub_folder = 'other'
    f = open('email/%s/%s.txt' % (sub_folder, id), 'w')
    control = f.write(mess)
    if control != len(mess):
        print('ERROR! Mess %s.txt wrong write' % id)
    else:
        print('Success! Mess %s.txt write complite' % id)
    f.close()
