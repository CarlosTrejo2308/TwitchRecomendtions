import unittest
from unittest.mock import Mock, patch
from unittest import mock
import twitch
from twitch import TwitchClient, TwitchHelix
import requests
from APIfuncional import apiTwitch
class TestApi(unittest.TestCase):
    
    def test_get_userid(self):
        prueba = apiTwitch()
        resultados = ["118237854", "31478096", "46719113"]
        nombres = ["albertto1198", "mym_alkapone", "gorilanerd"]
        for i in range(len(resultados)):
            salida_esperada = resultados[i]
            salida_actual = prueba.get_userid(nombres[i])
            self.assertAlmostEqual(salida_actual, salida_esperada)

    def test_get_followers(self):
        prueba = apiTwitch()
        salidas = [['97322738', '118974117', '233992790', '49656095', '158434891', '64582762', '28344564', '31894912', '42999001', '19106200', '31478096', '46719113', '80987594'],
        ['76149772', '136922366', '121203480', '36029255', '69588825', '39023698', '84594988', '103828377', '84982869', '96235256', '41725774', 
        '46490205', '189755167', '21130533', '453376326', '1518077', '127718836', '109724636', '29661191', '101400190', '65171890', '124425501', 
        '43691', '421838340', '149289742', '35618666', '267573232', '45453222', '133702699', '29249710', '167189231', '118918431', '61629003', 
        '27934574', '40035700', '8014563', '108005221', '85956078', '13240194', '143524887', '20420989', '22552479', '76385901', '55762605', 
        '36473331', '43199383', '168843586', '79506805', '51693898', '36769016', '125381567', '19249745', '49397431', '38301436', '62509579', 
        '30721712', '110176631', '64479989', '144555242', '234294620', '42894631', '60056333', '38948800', '67509214', '56625428', '48286022', 
        '40972890', '39298218', '38553197', '31595348', '106125347', '145270723', '15564828', '29829912', '28344564', '110690086', '49940618', 
        '66691674', '37851229', '38865133', '32140000', '53831525', '30782393', '41939266', '8330235', '64342766', '38881685', '40061427', 
        '31089858', '117379932', '14408894', '25236843', '108547363', '122320848', '100213504', '39955384', '159950991', '138539768', '26946000', 
        '63135520', '51496027', '37402112', '9679595', '78513335', '19571641', '90020006', '91265602', '62551187', '52091823', '66217508', 
        '74497222', '28036688', '23822990', '51753224', '23735582', '37120773', '101936909', '17337557', '46719113', '45921770', '120475981', 
        '47939440', '63164470', '30933196', '27586515', '106852329', '112815281', '46877634', '38718052', '84569419', '59131475', '84072112', 
        '74785305', '26301881', '48589777', '49236135', '45016072', '100484450', '24538518', '35790122', '23161357', '1121217', '32632309', 
        '23057278', '39627315', '44445592', '69955030', '19106200', '51792908', '61574749', '42999001', '24991333', '48535640', '21673391', 
        '35838240', '26490481', '26085270', '25281570', '31478096']]
        id_usuarios = ["118237854", "31894912"]
        for r in range(len(salidas)):
            prueba = apiTwitch()
            salida = salidas[r]
            salida_actual = prueba.get_followers(id_usuarios[r])
            salida_esperada = salida
            self.assertAlmostEqual(salida_actual, salida_esperada)

    def test_get_name(self):
        prueba = apiTwitch()
        resultados = ["albertto1198", "keriosriven", "ag_bean3r"]
        id_nombres = ["118237854", "118974117", "28344564"]
        for k in range(len(id_nombres)):            
            salida_actual = prueba.get_name(id_nombres[k])
            salida_esperada = resultados[k]
            self.assertAlmostEqual(salida_actual, salida_esperada)


    def test_get_followe(self):
        prueba = apiTwitch()
        lista_id = ["42999001", "97322738", "80987594"]
        resultados = [prueba.get_followe(42999001), prueba.get_followe(97322738), prueba.get_followe(80987594)]

        for l in range(len(lista_id)):
            salida = resultados[l]
            salida_actual = prueba.get_followe(lista_id[l])
            salida_esperada = salida
            self.assertAlmostEqual(salida_actual, salida_esperada)
if __name__ == "__main__":
    unittest.main() 