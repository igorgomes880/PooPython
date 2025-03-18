class Produto:
    def init(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):
        if type(codigo) != int or codigo <= 0:
            raise ValueError("Código inválido!")
        if type(nome) != str or len(nome) < 2:
            raise ValueError("Nome inválido!")
        if type(preco) != float or preco <= 0:
            raise ValueError("Preço inválido!")
        if type(descricao) != str:
            raise ValueError("Descrição inválida!")
        if type(categoria) != str or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria inválida!")
        if type(estoque) != int or estoque < 0:
            raise ValueError("Estoque inválido!")
        if type(perecivel) != bool:
            raise ValueError("Perecível inválido!")
        self.set_codigo = (codigo)
        self.set_nome = (nome)
        self.set_descricao = (descricao)
        self.set_categoria = (categoria)
        self.set_preco = (preco)
        self.set_estoque = (estoque)
        self.set_perecivel = (perecivel)

    def reajustar_preco(self, percentual):
        if percentual <= 0:
            raise ValueError("Percentual de reajuste inválido!")
        self.__preco = self.__preco * (1 + percentual/100)

    def set_codigo(self, codigo):
        if type(codigo) != int or codigo <= 0:
            raise ValueError("Código inválido!")
        self.__codigo = codigo

    def set_nome(self, nome):
        if type(nome) != str or len(nome) < 2:
            raise ValueError("Nome inválido!")
        self.__nome = nome

    def set_descricao(self, descricao):
        if type(descricao) != str:
            raise ValueError("Descrição inválida!")
        
    def set_categoria(self, categoria):
        if type(categoria) != str or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria inválida!")
        self.__categoria = categoria

    def set_preco(self, preco):
        if type(preco) != float or preco <= 0:
            raise ValueError("Preço inválido!")
        
    def set_estoque(self, estoque):
        if type(estoque) != int or estoque < 0:
            raise ValueError("Estoque inválido!")
        self.__estoque = estoque

    def set_perecivel(self, perecivel):
        if type(perecivel) != bool:
            raise ValueError("Perecível inválido!")
        self.__perecivel = perecivel

    def get_codigo(self):
        return self.__codigo
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_categoria(self):
        return self.__categoria
    
    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque
    
    def get_perecivel(self):
        return self.__perecivel
        
    

    