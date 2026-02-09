

# Python para Dados – Alura

Projeto desenvolvido durante os estudos do curso **Python para Dados** da Alura.  
O objetivo é praticar os fundamentos da linguagem Python aplicados à análise e manipulação de dados, utilizando boas práticas de código.



## 📌 Objetivo do Projeto

- Trabalhar com **estruturas de dados** em Python
- Criar e organizar **funções reutilizáveis**
- Aplicar **tratamento de exceções** para tornar o código mais robusto
- Simular cenários comuns em análise de dados



## 🧩 Estruturas de Dados Utilizadas

### 📋 Listas

Usadas para armazenar coleções ordenadas de dados.

```python
valores = [10, 20, 30, 40]
```


### 🗝 Dicionários

Utilizados para relacionar chaves e valores, muito comuns em dados estruturados.

```python
produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 10
}
```



### 🧮 Tuplas

Empregadas quando os dados não devem ser alterados.

```python
colunas = ("nome", "preco", "estoque")
```


## 🔧 Funções

As funções foram criadas para deixar o código mais organizado, reutilizável e legível.

Exemplo:

```python
def calcular_media(valores):
    """
    Calcula a média de uma lista de valores numéricos
    """
    return sum(valores) / len(valores)
```

### Benefícios do uso de funções

* Evitam repetição de código
* Facilitam manutenção
* Melhoram a legibilidade


## ⚠ Tratamento de Exceções

O tratamento de exceções é utilizado para lidar com erros comuns.

```python
try:
    resultado = calcular_media(valores)
    print(resultado)
except ZeroDivisionError:
    print("Erro: a lista está vazia.")
except TypeError:
    print("Erro: tipo de dado inválido.")
else:
    print("Cálculo realizado com sucesso.")
finally:
    print("Fim da execução.")
```

### Vantagens

* Evita que o programa quebre inesperadamente
* Permite mensagens de erro mais claras
* Torna o código mais profissional


## ▶ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/python_para_dados_alura.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
python main.py
```

## 🚀 Tecnologias Utilizadas

* Python 3
* Bibliotecas padrão do Python
* Pandas (opcional)
* Numpy (opcional)

---

## 📚 Aprendizados

* Estruturas de dados em Python
* Criação de funções
* Tratamento de exceções
* Organização de projetos
* Boas práticas de código

---

## ✍ Autor Talilo

Projeto desenvolvido para fins educacionais durante os cursos da **Alura**.
