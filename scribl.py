import sys

def encode_msg(otp_map, msg):
    otp = generate_otp(otp_map, msg)
    encoded_msg = bytearray()

    for i in range(len(msg)):
        encoded_msg.append(msg[i] ^ otp[i])
    
    return encoded_msg


def decode_msg(otp_map, msg):
    otp = generate_otp(otp_map, msg)
    decoded_msg = bytearray()

    for i in range(len(msg)):
        decoded_msg.append(msg[i] ^ otp[i])
    
    return decoded_msg


def write_to_file(file, msg):
    with open(file, mode='rb') as f:
        otp_map = f.read()
    with open(file, mode='ab') as f:
        f.write(encode_msg(otp_map, msg.encode('utf-8')))

def read_from_file(file):
    pass

def remove_from_file(file):
    pass

def generate_otp(otp_map, msg):    
    otp = bytearray(otp_map[:len(msg)])
    i = 0
    while len(otp) < len(msg):
        otp.append(otp[i])
        i +=1

    return otp


if __name__ == '__main__':
    pass
