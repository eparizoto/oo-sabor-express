from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('Carlos', 10)
restaurante_praca.receber_avaliacao('Ana', 6)
restaurante_praca.receber_avaliacao('Pedro', 9)

def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()