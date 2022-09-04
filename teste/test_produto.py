# Importando Funções
import pytest
import numpy as np
import requests
# Importando Classes
from classes.Produto import Produto
from classes.Carrinho import Carrinho

# Testes unitários do Produto
@pytest.mark.produto
def test_criacao_objeto_produto():
    id_produto = "0010342967" 
    nome = "Sabonete"
    produto = Produto(id_produto, nome)
    assert produto.id == id_produto 
    assert produto.nome == nome

# Produto | Testa criação de um novo ID
@pytest.mark.produto
def test_self_id():
    produto = Produto("0010342967", "Sabonete")
    novo_id = "0010342968"
    assert produto.self_id(novo_id) == novo_id

# Produto | Testa se o id do produto está sendo pego (função "get_id")
@pytest.mark.produto
def test_get_id():
    id_produto = "0010342967"
    nome = "Sabonete"
    produto = Produto(id_produto, nome)
    assert Produto.get_id(produto) == id_produto

# Carrinho | Testa se um item está sendo adicionar corretamente
@pytest.mark.carrinho
def test_adicionar_item():
    produto = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 4)
    atributo = carrinho.get_itens()
    assert atributo == {"0010342967": 4}



