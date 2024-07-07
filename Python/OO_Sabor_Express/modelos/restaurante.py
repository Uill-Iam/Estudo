from modelos.avaliacao import Avaliacao

# Projeto Orientado a Objeto

# Criação de classe
# __init__ é o construtor.
# __str__ com return retorna em string a informação que eu desejo ver
# self referencia o objeto sendo criado
# Colocar o "_" no atributo faz com que ele vire um atributo protegido
# @classmethod define que é um método da classe. Quando for dos objetos não precisa definir 
# @property altera a propriedade de um atributo
# Uma classe também pode importar outras classes usando o import

class Restaurante:
    """Classe com restaurante e suas caracteristicas"""
    restaurantes = []
    
    def __init__(self, nome, categoria):
        """
        Recebe dois parametros:
        - Nome (Str)
        - Categoria(Str)
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Lista como String:
        Outputs:
        - Nome 
        _Categoria
        """
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        """
        Lista os restaurantes:
        Outputs:

        - Nome
        - Categoria 
        - Avaliacao
        - Estado
        """
        for restaurante in cls.restaurantes:
            print(f'Nome Restaurante: {restaurante._nome.ljust(25)} | Categoria: {str(restaurante._categoria.ljust(25)).ljust(25)} | Avaliação: {restaurante.media_avaliacao} | Estado: {restaurante.ativo}')
    
    @property
    def ativo(self):
        """Exibe o estado como Simbulo"""
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self):
        """Altera o estado do restaurante"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Recebe as avaliações e inlcui em uma lista" quando a nota estiver entre 0 e 5 """
        if  0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        """ Retorna a media das avaliações"""
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media
