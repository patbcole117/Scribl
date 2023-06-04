import scribl
import unittest

msgs = [b'pat', b'patrick', b'patrickpatrickpatrick']
otp_maps = [b'\x00\x00\x00', b'\x01\x01\x01', b'\x01', b'\x00\x01\x02\x03\x04']


class encode_msg_test(unittest.TestCase):
    pass

class generate_otp_test(unittest.TestCase):
   
    def test_generate_otp_same_len(self):
        for m in msgs:
            for o in otp_maps:
                otp = scribl.generate_otp(o,m)
                self.assertEqual(len(m), len(otp))
                print(f'MESSAGE: {m} OTPMAP: {o} OTP: {otp}')


if __name__ == '__main__':
    unittest.main()