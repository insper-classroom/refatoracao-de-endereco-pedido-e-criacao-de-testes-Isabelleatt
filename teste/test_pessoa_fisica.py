# Impotando funções
import pytest
import numpy as np
import requests
# Importando classes
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

# Testes unitários de Pessoa Física

# Pessoa Física | Verifica se a criação dos objetos essenciais de "Pessoa Física" está sendo feita de forma correta
@pytest.mark.pessoa_fisica
@pytest.mark.criacao_objeto
def test_criacao_objeto_pessoa_fisica():
    cpf = '524.222.452-6'
    email = 'tiago@email.com'
    pessoa_fisica = PessoaFisica(cpf=cpf, email=email)
    assert pessoa_fisica.cpf == cpf
    assert pessoa_fisica.email == email
    assert pessoa_fisica.nome == "Visitante"

# Pessoa Física | Verifica se a criação do objeto "Pessoa Física" com todos os parâmetros está sendo feita de forma correta
@pytest.mark.pessoa_fisica
@pytest.mark.criacao_objeto
def test_verica_criacao_objeto_pessoa_fisica_todos_os_parametros():
    cpf = '524.222.452-6'
    email = 'tiago@email.com'
    nome = 'Carlos'
    pessoa_fisica = PessoaFisica(cpf=cpf, email=email, nome=nome)
    assert pessoa_fisica.cpf == cpf
    assert pessoa_fisica.email == email
    assert pessoa_fisica.nome == nome

# Pessoa Física | Testa se um endereço de entrega está sendo adicionado 
@pytest.mark.pessoa_fisica
def test_adicionar_endereco():
    apelido_endereco = 'casa'
    end = Endereco('08320330', 430)
    pessoa_fisica = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    pessoa_fisica.adicionar_endereco(apelido_endereco, end)
    assert pessoa_fisica.listar_enderecos() == [end]

# Pessoa Física | Testa se um endereco de entrega está sendo removido 
@pytest.mark.pessoa_fisica
def test_remover_endereco():
    apelido_endereco = 'casa'
    end = Endereco('08320330', 430)
    pessoa_fisica = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    pessoa_fisica.adicionar_endereco(apelido_endereco, end)
    pessoa_fisica.remover_endereco(apelido_endereco=apelido_endereco)
    assert pessoa_fisica.listar_enderecos() == []

# Pessoa Física | Testa se o endereço está sendo pego (função get_endereco)
@pytest.mark.pessoa_fisica
def test_get_endereco():
    apelido_endereco = 'casa'
    end = Endereco('08320330', 430)
    pessoa_fisica = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    pessoa_fisica.adicionar_endereco(apelido_endereco, end)
    assert pessoa_fisica.get_endereco(apelido_endereco) == end

# Pessoa Física | Testa se os endereços estão sendo listados
@pytest.mark.pessoa_fisica
def test_listar_enderecos():
    apelido_endereco = 'casa'
    end = Endereco('08320330', 430)
    pessoa_fisica = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    pessoa_fisica.adicionar_endereco(apelido_endereco, end)
    assert pessoa_fisica.listar_enderecos() == [end]

# Pessoa Física | Testa se os nomes estão sendo buscados corretamente
@pytest.mark.pessoa_fisica
def test_busca_nome():
    nome = 'Maria'
    pessoa_fisica = PessoaFisica('524.222.452-4', 'maria@email.com', 'Maria')
    assert PessoaFisica.busca_nome(nome) == [pessoa_fisica]


