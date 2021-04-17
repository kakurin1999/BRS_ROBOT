def getMess(filename):
    f = open(filename, 'r')
    mess = f.read()
    mess = mess[mess.find('Текст:') + 7:len(mess)]
    f.close()
    return mess