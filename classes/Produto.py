#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

class Produto:    

    objeto_produto = []
    def __init__(self, id_produto, nome=''): # construtor "__init__" "self" é necessário para acessar os atributos
        # Características:
        self.id = id_produto
        self.nome = nome
        Produto.objeto_produto.append(self)
        # Ações:

    def self_id(self, id_novo):
        # O objeto que está chamando os métodos e os valores que estão sendo refereciados são prórpios deles
        self.id = id_novo # O próprio sabonete
        return self.id
    
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {'id': self.id_produto, 'nome': self.nome}

    def busca_nome(nome_produto):
        ocorrencia_produto = []
        for objeto in Produto.objeto_produto:
            if objeto.nome == nome_produto: 
                ocorrencia_produto.append(objeto)
        return ocorrencia_produto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_novo):
        if nome_novo[0] != 'T':
            self.__nome = nome_novo
    
    @nome.getter
    def nome(self):
        return self.__nome

    @nome.deleter
    def nome(self):
        del self.__nome
        return "Nome deletado com sucesso"
    


