# criando uma classe abstrata para que todas as outras classe receba o metodo da classe Mãe
# Todas as outras classes serão obrigadas a ter esse metodos abistrato implementado
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplica_desconto(self):
        pass