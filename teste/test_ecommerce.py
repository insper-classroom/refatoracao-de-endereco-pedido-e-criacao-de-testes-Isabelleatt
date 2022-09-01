import pytest
import numpy as np
import requests
from classes.Endereco import Endereco

# Verifica se a criação do objeto "cep" e número está sendo feita de forma correta
@pytest.mark.endereco
@pytest.mark.criacao_objeto
def test_verica_criacao_objeto_cep_numero():
    cep = "04546042"
    numero = 300
    endereco = Endereco(cep=cep, numero=numero) 
    assert endereco.rua == 'R. Quatá'
    assert endereco.estado == 'SP' 
    assert endereco.cidade == 'São Paulo'

# Verifica se a criação dos demais objetos está sendo feita de forma correta
@pytest.mark.endereco
@pytest.mark.criacao_objeto
def test_verica_criacao_objeto_todos_os_parametros(): 
    cep = '04546042'
    numero = 300
    rua = 'R. Quatá'
    estado = 'São Paulo'
    cidade = 'São Paulo'
    complemento = 'Próximo ao Contém Café'
    endereco = Endereco(cep=cep, numero=numero, rua=rua, estado=estado, cidade=cidade, complemento=complemento) # Compara a sua variável pelo que a classe recebe 
    assert endereco.cep == '04546042'
    assert endereco.numero == 300
    assert endereco.rua == 'R. Quatá'
    assert endereco.estado == 'SP' 
    assert endereco.cidade == 'São Paulo'
    assert endereco.complemento == 'Próximo ao Contém Café'

# Testando o método consultar_cep:

# Consultar Cep | Passa o cep como string (str)
@pytest.mark.endereco
@pytest.mark.consulta_cep
def test_consulta_cep_string():
    cep = '04546042'
    endereco = Endereco.consultar_cep(cep=cep) 
    assert endereco['logradouro'] == 'R. Quatá' and endereco['localidade'] == 'São Paulo' and endereco['uf'] == 'SP'

# Consultar Cep | Passa o cep como inteiro (int)
@pytest.mark.endereco
@pytest.mark.consulta_cep
def test_consulta_cep_int():
    cep = '04546042'
    endereco = Endereco.consultar_cep(cep=cep) 
    assert endereco['logradouro'] == 'R. Quatá' and endereco['localidade'] == 'São Paulo' and endereco['uf'] == 'SP'

# Consultar Cep | Passa cep não existente
@pytest.mark.endereco
@pytest.mark.consulta_cep
def test_formato_numerico_cep():
    cep = '11111111'
    endereco = Endereco.consultar_cep(cep=cep) 
    assert endereco == False

# Consultar Cep | Erro no formato númerico - Cep menor do que o esperado
@pytest.mark.endereco
@pytest.mark.consulta_cep
def test_formato_numerico_menor_cep():
    cep = '4546042'
    endereco = Endereco.consultar_cep(cep=cep) 
    assert endereco == False

# Consultar Cep | Erro no formato númerico de um cep - Cep maior do que o esperado
@pytest.mark.endereco
@pytest.mark.consulta_cep
def test_formato_numerico_maior_cep():
    cep = '045460422'
    endereco = Endereco.consultar_cep(cep=cep) 
    assert endereco == False

# Verifica se há erro de conexão
@pytest.mark.erro_de_conexao
def test_conexao_de_internet():
    cep = '04546042'
    with pytest.raises(requests.exceptions.ConnectionError) as excinfo:
        endereco = Endereco.consultar_cep(cep) 
    assert "maximum recursion Max retries exceeded with url" in str(excinfo.value)
