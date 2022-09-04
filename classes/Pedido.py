#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re

class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    def __init__(self, pessoa, carrinho):
        self.pessoa = pessoa
        self.carrinho = carrinho
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
    
    # Formata a string que contém o pedido
    def __str__(self):
        return (f'''
Nome: {self.pessoa.nome}
Produtos: {self.carrinho.get_itens()}
Endereço de entrega: {self.endereco_entrega}
Endereço de recebimento da fatura: {self.endereco_faturamento}
''')



    