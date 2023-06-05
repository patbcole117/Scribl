import scribl
import unittest

msgs = [b'pat', b'patrick'] 
otp_maps = [b'\x00\x00\x00', b'\x01\x01\x01', b'\x01', b'\x00\x01\x02\x03\x04']
ans = [b'\x70\x61\x74', b'\x71\x60\x75', b'\x71\x60\x75', b'\x70\x60\x76', \
        b'\x70\x61\x74\x72\x69\x63\x6B', b'\x71\x60\x75\x73\x68\x62\x6A', \
        b'\x71\x60\x75\x73\x68\x62\x6A', b'\x70\x60\x76\x71\x6D\x63\x6A']


class encode_msg_test(unittest.TestCase):
    
    def test_encode_msg(self):
        print('\nBEGIN TEST ENCODE_MSG')

        results = []
        
        for m in msgs:
            for o in otp_maps:
                encoded_msg = scribl.encode_msg(o, m)
                results.append(encoded_msg)
        
        for i in range(len(results)):
            self.assertEqual(results[i], ans[i])
            print(f'ITER: {i} RESULT: {results[i]} ANS: {ans[i]}')

        print('END TEST ENCODE_MSG')


class generate_otp_test(unittest.TestCase):
   
    def test_generate_otp(self):
        print('\nBEGIN TEST GENERATE_OTP')

        for m in msgs:
            for o in otp_maps:
                otp = scribl.generate_otp(o,m)
                self.assertEqual(len(m), len(otp))
                print(f'MESSAGE: {m} OTPMAP: {o} OTP: {otp}')

        print('END TEST GENERATE_OTP')


if __name__ == '__main__':
    unittest.main()
