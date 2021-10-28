def parse_num(msg):
    message = msg.split(' ')
    for x in message:
        if x.isnumeric():
            value = x
            return float(value)
            