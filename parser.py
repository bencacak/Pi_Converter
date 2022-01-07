def parse_num(msg):
    message = msg.split(' ')
    for x in message:
        try:
            return float(x)
        except ValueError:
            #print(x)
            pass