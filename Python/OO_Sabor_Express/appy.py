from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


#instanciando objeto
restaurante_pizza = Restaurante('pizaria','Italiana')
restaurante_Sushi = Restaurante('sushi','Japonesa')
restaurante_mexicano = Restaurante('Hola','Mexicana')

# eenviando avaliação
restaurante_Sushi.receber_avaliacao('Uill',2)
restaurante_Sushi.receber_avaliacao('Thais',5)

#criando pratos e bebidas

prato = Prato('Sushi',11.50,'Prato com peixe')
prato.aplica_desconto()
bebida = Bebida('Coca-cola',5.60,'250ML')
bebida.aplica_desconto()
restaurante_Sushi.adcionar_item_cardapio(bebida)
restaurante_Sushi.adcionar_item_cardapio(prato)

def main():
  # Restaurante.listar_restaurante()
    restaurante_Sushi.exibir_cardapio

if __name__ == '__main__':
    main()
