def littleendian(value):
    value = value.replace('0x','').lower()

    value_dict = dict([('0',0),('1',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('a',10),('b',11),('c',12),('d',13),('e',14),('f',15)])

    dec_value_list = []

    # Создание списка из 10-значных чисел
    for i in value:
        dec_value_list.append(value_dict.get(i))

    s = ''
    bin_value_list = []

    # Создание списка из 2-значных чисел
    for i in range(len(dec_value_list)):
        if dec_value_list[i] == 0:
            bin_value_list.append('0000') 
        else:
            while dec_value_list[i] > 0:
                s = str(dec_value_list[i] % 2) + s
                dec_value_list[i] = dec_value_list[i] // 2
            bin_value_list.append(s)
            s = ''

    for i in range(len(bin_value_list)):
        if len(bin_value_list[i]) < 4:
            bin_value_list[i] = '0'*(4 - len(bin_value_list[i])) + bin_value_list[i]

    
    n = 0
    bin_value_list_new = []
    while n in range(len(bin_value_list)-1):
        bin_value_list_new.append(bin_value_list[n] + bin_value_list[n+1])
        n += 2
    if len(bin_value_list) % 2 != 0:
        bin_value_list_new.append(bin_value_list[-1])
    bin_value_list_new.reverse()  
 

    little_endian_string = ''.join(bin_value_list_new)


    # Cоздание списка для позиционной проверки
    value_position = []
    for i in range(len(little_endian_string)):
        valuelength = pow(2,i)
        value_position.append (valuelength)
    value_position.reverse()


    little_endian_value = 0

    # Вычисление значений
    for i in range(len(little_endian_string)):
        little_endian_value += value_position[i] * int(little_endian_string[i])
    return little_endian_value 

def bigendian(value):
    value = value.replace('0x','').lower()

    value_dict = dict([('0',0),('1',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('a',10),('b',11),('c',12),('d',13),('e',14),('f',15)])

    dec_value_list = []

    # Создание списка из 10-значных чисел
    for i in value:
        dec_value_list.append(value_dict.get(i))
 
    s = ''
    bin_value_list = []

    # Создание списка из 2-значных чисел
    for i in range(len(dec_value_list)):
        if dec_value_list[i] == 0:
            bin_value_list.append('0000') 
        else:
            while dec_value_list[i] > 0:
                s = str(dec_value_list[i] % 2) + s
                dec_value_list[i] = dec_value_list[i] // 2
            bin_value_list.append(s)
            s = ''

    for i in range(len(bin_value_list)):
        if len(bin_value_list[i]) < 4:
            bin_value_list[i] = '0'*(4 - len(bin_value_list[i])) + bin_value_list[i]


    big_endian_string = ''.join(bin_value_list)

    n = 0
    bin_value_list_new = []
    while n in range(len(bin_value_list)-1):
        bin_value_list_new.append(bin_value_list[n] + bin_value_list[n+1])
        n += 2
    if len(bin_value_list) % 2 != 0:
        bin_value_list_new.append(bin_value_list[-1])
    

    # Cоздание списка для позиционной проверки
    value_position = []
    for i in range(len(big_endian_string)):
        valuelength = pow(2,i)
        value_position.append (valuelength)
    value_position.reverse()


    big_endian_value = 0

    # Вычисление значений
    for i in range(len(big_endian_string)):
        big_endian_value += value_position[i] * int(big_endian_string[i])
    return big_endian_value

def numberofbytes(value):
    value = value.replace('0x','').lower()
    return len(value)//2


value = input('Enter hex-number: ')

numberofbytes = numberofbytes(value)
littleendian = littleendian(value)
bigendian = bigendian(value)

print(f'Value: {value}\nNumber of bytes: {numberofbytes}\nLittle-endian: {littleendian}\nBig-endian: {bigendian}')