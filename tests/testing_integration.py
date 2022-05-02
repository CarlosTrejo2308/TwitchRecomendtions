# import main
# import unittest

# import io
# ##################################

# from src.imp.functional_bolt import FunctionalBolt
# from mBD import mockBD
# from APIfuncional import apiTwitch

# from unittest.mock import Mock
# import mock

# class TestIntegration(unittest.TestCase):

#     @mock.patch('main.input')
#     def testMain(self, mock_input):
#         entradas = ["3", "CarlosTrejo2308", "3", "Ninja", "3", "albertto1198", "4", "Ninja", "3", "mym_alkapone", "5", "mym_alkapone", "6", "7", "0"]

#         printed_esperado = """('name: ', 'mymtumtum69', ' id: ', '42999001', ' ponderation: ', 0.9305210918114144, ' blocked: ', False)
# ('name: ', 'ag_bean3r', ' id: ', '28344564', ' ponderation: ', 0.9305210918114144, ' blocked: ', False)
# ('name: ', 'duxativa', ' id: ', '19106200', ' ponderation: ', 0.9305210918114144, ' blocked: ', False)
# ('name: ', 'spartangeek', ' id: ', '97322738', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'keriosriven', ' id: ', '118974117', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'rainbow6latam', ' id: ', '233992790', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'zruuben', ' id: ', '49656095', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'francoescamilla', ' id: ', '158434891', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'officialyugiohchannel', ' id: ', '64582762', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# ('name: ', 'delt4forc3', ' id: ', '31894912', ' ponderation: ', 0.7692307692307693, ' blocked: ', False)
# Goodbye!"""
#         mock_input.side_effect = entradas

#         capturedOutput = io.StringIO()                # Create StringIO object
#         sys.stdout = capturedOutput                   #  and redirect stdout.


#         main.main(False)

#         sys.stdout = sys.__stdout__                   # Reset redirect.
#         printed = capturedOutput.getvalue()


#         x = printed_esperado in printed

#         self.assertTrue(x)

# if __name__ == '__main__':
#     unittest.main()
