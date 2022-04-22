from channel import Channel
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unittest import TestCase
import io
import sys

class TestChannel(unittest.TestCase):

    #Create channel to test
    def setUp(self):
        id = 647298
        ponderation = 10
        self.cToTestEmpty = Channel(id)
        self.cToTestPon = Channel(id, ponderation)

    def testCreate(self):
        params = ({"id": 288302},
        {"id": 3872994, "name": "Carlos"},
        {"id": 9381398, "name": "Ninja"},
        {"id": 98382392, "name": "Pancho", "ponderation": 10},
        {"id": 123749, "name": "Gamer123", "ponderation": 70},
        {"id": 242810, "name": "Juan", "ponderation": -10},
        )

        for r in range(len(params)):
            with self.subTest(r=r):
                param = params[r]
                testChannel = Channel(**param)

                #id
                self.assertEqual(param["id"], testChannel.id)

                #name
                if "name" not in param:
                    self.assertEqual("", testChannel.name)
                else:
                    self.assertEqual(param["name"], testChannel.name)

                #ponderation
                if "ponderation" not in param:
                    self.assertEqual(0, testChannel._ponderation)
                else:
                    self.assertEqual(param["ponderation"], testChannel._ponderation)

                #blocked
                self.assertFalse(testChannel.blocked)

    def testAdd(self):
        total = 0
        totalIn = 10

        adders = [12, 23, -50, 18, 0, 77, 3819]

        for r in range(len(adders)):
            with self.subTest(r=r):
                number = adders[r]
                total += number
                totalIn += number

                self.cToTestEmpty.addPonderation(number)
                self.cToTestPon.addPonderation(number)

                self.assertEqual(self.cToTestEmpty._ponderation, total)
                self.assertEqual(self.cToTestPon._ponderation, totalIn)

    def testmultiplyPonderation(self):
        total = 0
        totalIn = 10

        adders = [12, 23, -50, 18, 0, 77, 3819]

        for r in range(len(adders)):
            with self.subTest(r=r):
                number = adders[r]
                total *= number
                totalIn *= number

                self.cToTestEmpty.multiplyPonderation(number)
                self.cToTestPon.multiplyPonderation(number)

                self.assertEqual(self.cToTestEmpty._ponderation, total)
                self.assertEqual(self.cToTestPon._ponderation, totalIn)

    def testresetPonderation(self):
        numbers = [0, 9348, 19028.2342, 1923, -1212, 2039, 2030, 10393, 1022, 1029]

        for r in range(len(numbers)):
            with self.subTest(r=r):
                self.cToTestEmpty._ponderation = numbers[r]
                self.cToTestEmpty.resetPonderation()

                self.assertEqual(self.cToTestEmpty._ponderation, 0)

    def testBlocked(self):
        numbers = [0, 9348, 19028.2342, 1923, -1212, 2039, 2030, 10393, 1022, 1029]
        blocked = -9999999

        for r in range(len(numbers)):
            with self.subTest(r=r):
                number = numbers[r]

                #Block
                self.cToTestEmpty.block(True)
                self.assertTrue(self.cToTestEmpty.blocked)

                #Test functions
                added = self.cToTestEmpty
                added.addPonderation(number)
                multiplied = self.cToTestEmpty
                multiplied.multiplyPonderation(number)

                reseted = self.cToTestEmpty
                reseted.resetPonderation()

                self.assertEqual(self.cToTestEmpty._ponderation, blocked)
                self.assertEqual(added._ponderation, blocked)
                self.assertEqual(multiplied._ponderation, blocked)
                self.assertEqual(reseted._ponderation, blocked)


                #Unblock
                self.cToTestEmpty.block(False)

                self.assertFalse(self.cToTestEmpty.blocked)
                self.assertEqual(self.cToTestEmpty._ponderation, 0)

                #Add
                self.cToTestEmpty.addPonderation(number)
                self.assertEqual(self.cToTestEmpty._ponderation, 0 + number)
                self.cToTestEmpty._ponderation = 0

                #Mult
                self.cToTestEmpty.multiplyPonderation(number)
                self.assertEqual(self.cToTestEmpty._ponderation, 0 * number)


if __name__ == '__main__':
    unittest.main()
