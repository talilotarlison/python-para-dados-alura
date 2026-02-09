"""
As tuplas são estruturas de dados imutáveis da linguagem Python que são utilizadas para armazenar conjuntos de múltiplos itens e frequentemente são aplicadas para agrupar dados que não devem ser modificados. Ou seja, não é possível adicionar, alterar ou remover seus elementos depois de criadas. Vamos explorar um pouco mais desse tipo de estrutura voltada à aplicação em ciência de dados.

Tuplas são especialmente úteis em situações nas quais precisamos garantir que os dados não sejam alterados acidental ou intencionalmente. Por exemplo, em um conjunto de dados que representa o cadastro de estudantes, podemos utilizar uma tupla para representar aquele(a) estudante em específico e manter no banco de dados de uma instituição de ensino. Dessa forma, garantimos que as informações de cada estudante não sejam alteradas inadvertidamente.

Para criar uma tupla, basta separar seus elementos por vírgulas. Por exemplo, podemos criar uma tupla com um registro de uma estudante da seguinte maneira:
"""
cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")

print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1

nome, idade, cidade, estado, turma = cadastro # desestruturação

print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')