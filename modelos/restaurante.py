from modelos.avaliacao import Avaliacao

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avalicao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @property
    def ativo(self):
        return 'Sim' if self._ativo else 'Não'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avalicao.append(avaliacao)
    
    @property    
    def media_avaliacoes(self):
        if not self._avalicao:
            return '-'
        total = sum(avaliacao._nota for avaliacao in self._avalicao)
        return round (total / len(self._avalicao), 1)