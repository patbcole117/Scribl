import sys

def generate_otp(otp_map, msg):    
    otp = bytearray(otp_map[:len(msg)])
    i = 0
    while len(otp) < len(msg):
        otp.append(otp[i])
        i +=1

    return otp


if __name__ == '__main__':
    pass