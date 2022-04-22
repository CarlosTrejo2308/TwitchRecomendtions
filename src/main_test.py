import main
import unittest
from unittest.mock import Mock, patch
from unittest import TestCase
import io
import sys
import mock

class TestMain(unittest.TestCase):

    def test_getOptions(self):
        salida_esperada = "\n    1. Load Options\n    2. Save Options\n    3. Add channel\n    4. Remove channel\n    5. Block channel\n    6. Calculate\n    7. Get Recomendations\n    8. View Channels\n    9. Agregar por usuario\n    0. Quit"
        salida_actual = main.getOptions()

        self.assertEqual(salida_actual, salida_esperada)

    @mock.patch('main.input')
    def test_getChannel(self, mock_open):
        entrada = ["Clase 1", "Ninja", "Ninga", "", " ", ".", "-12345667", "CarlosTrejo2308"]
        salida = [-1, "Ninja", "Ninga", -1, -1, -1, -1, "CarlosTrejo2308"]


        for r in range(len(entrada)):
            with self.subTest(r=r):
                capturedOutput = io.StringIO()                # Create StringIO object
                sys.stdout = capturedOutput                   #  and redirect stdout.
                obj = entrada[r]
                mock_open.return_value = obj

                salida_actual = main.getChannel()
                sys.stdout = sys.__stdout__                   # Reset redirect.
                printed = capturedOutput.getvalue()
                salida_esperada = salida[r]

                self.assertEqual(salida_actual, salida_esperada)
                if salida[r] is -1:
                    self.assertEqual(printed, "Enter name of channel: \nHay un problema con este canal, o no hay internet\n")
                else:
                    self.assertEqual(printed, "Enter name of channel: \n")
                mock_open.assert_called_with(">> ")

    @mock.patch('main.input')
    @mock.patch('main.getOptions')
    def test_takeAction(self, mock_options, mock_input):
        B = "Out of bounds!\n"
        N = "Please only numbers!\n"
        E = "\nTo many errors!\nHere are the options again:\n\n"

        entrada = [["4"], ["0"], ["9"], ["-1", "10", "12", "10000", "-10000", "5"], [" ", "one", "zero", "u8", "8o", "@", "", "2"]]
        salida_esperada = [4, 0, 9, 5, 2]
        print_esperado = [[], [], [], [B, B, B, E, B, B], [N, N, N, E, N, N, N, E, N]]

        for r in range(len(entrada)):
            with self.subTest(r=r):
                mock_input.call_count = 0
                mock_options.call_count = 0

                #Variables cuanticas
                # lo = mock_options.call_count
                # la = mock_input.call_count
                # le = la is 1 or la is 0
                # self.assertEqual(lo, 0)
                # self.assertTrue(le)
                # self.assertEqual(la, 0)

                mock_input.side_effect = entrada[r]
                mock_options.return_value = ""

                capturedOutput = io.StringIO()                # Create StringIO object
                sys.stdout = capturedOutput                   #  and redirect stdout.

                salida_actual = main.takeAction()

                sys.stdout = sys.__stdout__                   # Reset redirect.
                printed = capturedOutput.getvalue()

                print_esperado_completo = ""
                called_options = 0
                pr_esperado = print_esperado[r]
                for i in pr_esperado:
                    if i is E:
                        called_options += 1
                    print_esperado_completo += i

                self.assertEqual(salida_actual, salida_esperada[r])
                self.assertEqual(printed, print_esperado_completo)

                #Ignore this for now becouse they are cuantic
                #Fixed! :D
                self.assertEqual(mock_options.call_count, called_options)
                self.assertEqual(mock_input.call_count, len(entrada[r]))

    @mock.patch('main.coneccion_bd')
    @mock.patch('main.getChannel')
    @mock.patch('main.workingbolt')
    @mock.patch('main.sys')
    def test_doAction_calls(self, mock_sys, mock_bolt, mock_chanel, mock_bd):
        #Input = 0
        capturedOutput = io.StringIO()                # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.

        main.doAction(0)

        sys.stdout = sys.__stdout__                   # Reset redirect.
        printed = capturedOutput.getvalue()

        self.assertEqual(printed, "Goodbye!\n")
        #self.assertEqual(mock_sys.exit.call_count, 1)

        #Input = 1
        main.doAction(1)
        self.assertEqual(mock_bd.get_list.call_count, 1)

        #Input = 2
        main.doAction(2)
        self.assertEqual(mock_bd.save_list.call_count, 1)

        #Input = 3
        main.doAction(3)
        self.assertEqual(mock_chanel.call_count, 1)
        self.assertEqual(mock_bolt.addChanel.call_count, 1)

        mock_chanel.call_count = 0
        #Input = 4
        main.doAction(4)
        self.assertEqual(mock_chanel.call_count, 1)
        self.assertEqual(mock_bolt.removeChanel.call_count, 1)

        mock_chanel.call_count = 0
        #Input = 5
        main.doAction(5)
        self.assertEqual(mock_chanel.call_count, 1)
        self.assertEqual(mock_bolt.blockChanel.call_count, 1)

        #Input = 6
        main.doAction(6)
        self.assertEqual(mock_bolt.calculate.call_count, 1)

        #Input = 7
        main.doAction(7)
        self.assertEqual(mock_bolt.printRecomendations.call_count, 1)

        #Input = 8
        main.doAction(8)
        self.assertEqual(mock_bolt.viewChannels.call_count, 1)


    @mock.patch('main.getOptions')
    @mock.patch('main.takeAction')
    @mock.patch('main.doAction')
    def test_main(self, mock_action, mock_take, mock_options):
        for r in range(8):
            with self.subTest(r=r):
                mock_take.return_value = r
                mock_options.call_count = 0
                mock_options.return_value = ""

                #Clean output
                capturedOutput = io.StringIO()                # Create StringIO object
                sys.stdout = capturedOutput                   #  and redirect stdout.

                main.main(True)
                mock_action.assert_called_with(r)
                self.assertTrue(mock_options.call_count, 1)


if __name__ == '__main__':
    unittest.main()
