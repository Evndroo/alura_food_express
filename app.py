

from modules.restaurant import Restaurant


restaurante_praca = Restaurant('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Evandro', 10)
restaurante_praca.receber_avaliacao('User 1', 8)
restaurante_praca.receber_avaliacao('User 2', 2)

def main():
    Restaurant.listar_restaurantes()

if __name__ == '__main__':
    main()