import unittest

def retorna_numeros_primos(numero):
    n = 2
    lista_primos=[]
    while n <= numero:
        if (numero_primo(n)) and (numero % n == 0):
            lista_primos.append(n)
            numero = numero/n
        else:
            n+=1
    return lista_primos

def numero_primo(n):
    if n is not 2:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True




class TestFatoresPrimos(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_5(self):
        numero = 5
        esperado = [5]
        self.assertEqual(esperado, retorna_numeros_primos(numero))

    def test_5_e_primo(self):
        numero = 5
        esperado = True
        self.assertEqual(esperado, numero_primo(numero))

    def test_100(self):
        numero = 100
        esperado = [2,2,5,5]
        self.assertEqual(esperado, retorna_numeros_primos(numero))

    def test_276(self):
        numero = 276
        esperado = [2,2,3,23]
        self.assertEqual(esperado, retorna_numeros_primos(numero))

    def test_9230(self):
        numero = 9230
        esperado = [2,2,3,23]
        self.assertEqual(esperado, retorna_numeros_primos(numero))

if __name__ == '__main__':
    unittest.main()
