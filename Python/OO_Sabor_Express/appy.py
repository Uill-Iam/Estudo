from modelos.restaurante import Restaurante


#instanciando objeto
Restaurante_pizza = Restaurante('pizaria','Italiana')
Restaurante_Sushi = Restaurante('sushi','Japonesa')
Restaurante_mexicano = Restaurante('Hola','Mexicana')

# eenviando avaliação
Restaurante_Sushi.receber_avaliacao('Uill',2)
Restaurante_Sushi.receber_avaliacao('Thais',5)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()