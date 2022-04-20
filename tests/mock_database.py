import unittest
import basedatos


class MyTests(unittest.TestCase):

    # @patch('basedatos.Ver_Bandas_Totales')
    def test_mostrar_artista(self):
        artista_list = basedatos.database.mostrar_usuario('seguidos')
        #mock_artista.return_value.read.return_value = basedatos.database.Ver_Bandas_Totales('artistas')

        self.assertEqual(
            artista_list, basedatos.database.mostrar_usuario('seguidos'))


if __name__ == '__main__':
    unittest.main()
