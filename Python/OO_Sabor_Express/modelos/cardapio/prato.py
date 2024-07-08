from modelos.cardapio.item_cardapio import ItemCardapio

### desenvolvendo Herança
# Para importar informações da classe "pai " precisamos:
# 1 . Importar a classe
# 2. Informar dentro da classe filho  qual a classe pai()
# 3. usar o comando Super para trazer o construtor 

class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao

    def __str__(self) -> str:
        return self._nome
       
    def aplica_desconto(self):
        self._preco -= (self._preco * 0.05)