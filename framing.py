'''
@author: Hien Le
@group: 55
@id: 2594428
@email: hien.le@student.auc.nl
Assignment 1 - Computer Networks 2018 - Vrije Universiteit Amsterdam
'''


# dest = 2 bytes
# source = 2 bytes
# length = 4 bytes
# payload = 0-64 bytes
# checksum = 2 bytes

import binascii


class ALP(object):
    def __init__(self, dest, stream):
        self.dest = dest
        self.stream = stream

    def check_mismatch(self, frame_dest):

        # check if real address matches frame's address
        if self.dest != frame_dest:
            print('ADDRESS MISMATCH')
            return False

    @staticmethod
    def verify_checksum(frame):

        # computes checksum and checks if it matches frame's checksum
        frame_cs = frame[-2:]
        frame_without_cs = frame[:-2]
        lst_dec_vals = [frame_without_cs[i: i + 2] for i in range(0, len(frame_without_cs), 2)]
        dec_checksum = sum([int(hex_val, 16) for hex_val in lst_dec_vals]) % 128
        hex_checksum = '{0:x}'.format(int(dec_checksum))
        if len(hex_checksum) < 2:
            hex_checksum = "0" + hex_checksum
        if hex_checksum != frame_cs:
            print('ERROR')
            return False

    def distinguish(self, first_index, separated_frames):

        # separates frames in a single stream, using recursion
        lst_frames = separated_frames
        if first_index == len(self.stream):
            return lst_frames
        else:
            hex_length_frame = self.stream[first_index + 8:first_index + 16]
            dec_length_frame = int(hex_length_frame, 16)  # get length of frame as indicated in the 4 bytes
            msg_end = first_index + 16 + (dec_length_frame - 8) * 2
            separated_frames.append(self.stream[first_index:msg_end])
            return self.distinguish(msg_end, separated_frames)

    @staticmethod
    def decode(frame):

        # decodes message, returns whole decoded frame
        dest = frame[0:4]
        src = frame[4:8]
        length = frame[8:16]
        msg_end_index = 16 + (int(length, 16) - 9) * 2  # 9 redundant data bytes in frame
        msg = frame[16:msg_end_index]
        decoded_msg = binascii.unhexlify(msg).decode('utf-8')
        decoded_length = str(int(length, 16))
        return dest + " " + src + " " + decoded_length + " " + decoded_msg


def main():
    dest = input()
    stream = input()
    alp = ALP(dest, stream)
    frames = alp.distinguish(0, [])
    received_frames = ""
    for frame in frames:
        if alp.check_mismatch(frame[0:4]) == False:
            return
        elif ALP.verify_checksum(frame) == False:
            return
        received_frames += ALP.decode(frame) + "\n"  # print each frame on a single line
    print(received_frames[:-1])  # remove last escaped linebreak
    # return received_frames  # => for unittests

main()


'''
#Unit test
full_case_file_input = open('assignment-1-tea.input', 'r').read().splitlines()
full_case_file_output = open('assignment-1-tea.output', 'r').read()
example_input = "004b0049000000275468657265206973206e6f2077617220696e2042612053696e672053652e07"
import unittest
from unittest.mock import patch

class TestALP(unittest.TestCase):
    def test_solve_alp(self):
        user_input1 = [
    		full_case_file_input[0],
    		full_case_file_input[1],
    	]
        expected_output1 = full_case_file_output
        user_input2 = [
    		'004b',
    		example_input,
    	]
        expected_output2 = "004b 0049 39 There is no war in Ba Sing Se.\n"
        with patch('builtins.input', side_effect=user_input1):
            result1 = main()
        with patch('builtins.input', side_effect=user_input2):
            result2 = main()
        self.assertEqual(result1, expected_output1)
        self.assertEqual(result2, expected_output2)

if __name__ == "__main__":
    unittest.main(exit=False)


'''