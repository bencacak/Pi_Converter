def convert(msg, value):  
    msg = msg.lower()
    input = msg.split(' ')

    for i in input:    
        if i == 'km':
            unit = i
            new_unit = 'mi'
            new_value = value / 1.62
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        elif i == 'mi':
            unit = i
            new_unit = 'km'
            new_value = value * 1.62
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        elif i == 'kg':
            unit = i
            new_unit = 'lb'
            new_value = value * 2.21
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        elif i == 'lb':
            unit = i
            new_unit = 'kg'
            new_value = value / 2.21
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        elif i == 'c':
            unit = i
            new_unit = 'f'
            new_value = (value * 1.8) + 32
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        elif i == 'f':
            unit = i
            new_unit = 'c'
            new_value = (value - 32) / 1.8
            new_value = round(new_value, 2)
            return str(value) + ' ' + unit + ' is equal to ' + str(new_value) + ' ' + new_unit
        else:
            print("Not yet...")
        

        
            

    


        