#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    pessoa = []
    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.pessoa.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco): # O argumento "end" deve ser um objeto da classe endereço
        self.__enderecos[apelido_endereco] = end 
        return self.__enderecos[apelido_endereco]
        
    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]
        
    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        return list(self.__enderecos.values())

    def busca_nome(nome):
        ocorrencia_nomes = []
        for objeto in PessoaFisica.pessoa:
            if objeto.nome == nome: 
                ocorrencia_nomes.append(objeto)
        return ocorrencia_nomes
        

