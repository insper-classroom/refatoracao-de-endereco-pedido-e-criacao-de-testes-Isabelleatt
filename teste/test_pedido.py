# Importando funções
import pytest
import numpy as np
import requests

# Importando classes
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho

# Testes unitários dos Pedidos

# Pedido | Testa se os objetos de "Pedido" estão sendo criados corretamente
@pytest.mark.pedido
@pytest.mark.criacao_objeto
def test_criacao_objeto_pedido():
    pessoa = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    carrinho = Carrinho()
    pedido = Pedido(pessoa=pessoa, carrinho=carrinho)
    assert pedido.pessoa == pessoa
    assert pedido.carrinho == carrinho

# Pedido | Testa se os objetos de "endereço entrega" e "endereço de faturamento" de "Pedido" estão sendo criados corretamente
@pytest.mark.pedido
@pytest.mark.criacao_objeto
def test_criacao_objeto_pedido_todos_os_parametros():
    pessoa = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    carrinho = Carrinho()
    pedido = Pedido(pessoa=pessoa, carrinho=carrinho)
    assert pedido.pessoa == pessoa
    assert pedido.carrinho == carrinho
    assert pedido.endereco_faturamento == ''
    assert pedido.endereco_entrega == ''








