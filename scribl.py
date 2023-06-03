import sys                                                                    
                                       
DELIMITER = b'BOM'               
                                       
def help():                  
    print('''                                                                 
    Scribl is a tool for hiding messages in files.
                          
    USAGE: scribl.py FILE MESSAGE
    ''')            
                                       
def scribl(file, msg):
    with open(file, mode='ab') as file: 
        pass                                                                  
                                       
def encode_msg(file, msg)
    with open(file, mode='rb') as file: 
        key = file.read()[:len(msg.encode())]
        byte_pairs = list(zip(key,msg.encode()))
                                                                              
        encoded_msg = bytearray()
        encoded_msg.append(DELIMITER)
        for bp in byte_pairs:
            encoded_msg.append(bp[0] ^ bp[1])
                                                                                  
        return encoded_msg
                                       
def decode_msg(file)
      pass                                 
                                       
def check(file):                                                              
    with open(file, mode='rb') as file:                                       
        print(file.read())             
                                       
if __name__ == '__main__':                                                    
    if len(sys.argv) == 3:                                                    
        check(sys.argv[1])                                                    
        scribl(sys.argv[1], sys.argv[2])                                      
        check(sys.argv[1])