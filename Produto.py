class Produto:
    def __init__(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):
       if type(codigo) == int and codigo <= 0:
           raise ValueError("Codigo invalido!")
       if type(nome) != str or len(nome) < 2:
           raise ValueError("Nome invalido!")
       if type(preco) != float or preco <= 0:
           raise ValueError("Preco invalido!")
       if type(descricao) != str:
           raise ValueError("Descricao invalida!")
       if type(categoria) != str or categoria not in ["frutas", "eletronicos", "roupas"]:
          raise ValueError("Categoria invalida!") 
           
       self.categoria = categoria
       self.preco = preco
       self.estoque = estoque
       self.perecivel = perecivel

    def reajustar_precpo(self, percentual):
        if (percentual <=0):
            raise ValueError("Percenutal de reajuste inválido!")
        self.preco = self.preco * (1 + percentual/100)