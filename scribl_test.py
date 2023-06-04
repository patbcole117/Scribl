import scribl
import unittest

msg_list = [b'pat', b'patrick']
key_list = [b'\x00\x00\x00', b'\x01\x01\x01', b'\x01', b'\x00\x01\x02\x03\x04']


class encode_msg_test(unittest.TestCase):
    pass

class generate_otp_test(unittest.TestCase):
    
    def test_generate_otp_same_len(self):
    
        for m in msg_list:
            for k in key_list:
                pass

if __name__ == '__main__':
    unittest.main()