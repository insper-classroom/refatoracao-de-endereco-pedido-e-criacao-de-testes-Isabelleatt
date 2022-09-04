# Testes unitários do Carrinho

import pytest
import numpy as np
import requests
from classes.Carrinho import Carrinho
from classes.Produto import Produto

# Testes unitários do Carrinho

# Carrinho | Testa função de adicionar item
@pytest.mark.carrinho
def test_adicionar_item():
    produto = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 4)
    atributo = carrinho.get_itens()
    assert atributo == {"0010342967": 4}
        
# Carrinho | Testa função de remover item
@pytest.mark.carrinho
def test_remover_item(): 
    produto = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 4)
    carrinho.remover_item(produto)
    atributo = carrinho.get_itens()
    assert atributo == {}

# Carrinho | Testa função de pegar itens
@pytest.mark.carrinho
def test_get_itens():
    produto = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 4)
    atributo = carrinho.get_itens()
    assert atributo == {"0010342967": 4}

