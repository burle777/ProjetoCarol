# Livro de Receitas em Python

Este projeto é um livro de receitas interativo criado em Python, que permite aos usuários adicionar, visualizar, atualizar e gerenciar suas receitas favoritas de maneira simples e intuitiva. Este projeto foi realizado para a cadeira de fundamentos de programação da Cesar School.
Feito pelos alunos Guilherme Mourão, Henrique Tefile, André Burle e Guilherme Vinícius

![License](https://img.shields.io/badge/license-MIT-brightgreen)

## Tabela de Conteúdos
- [Instalação](#instalação)
- [Uso](#uso)
  - [Adicionar Receitas](#adicionar-receitas)
  - [Visualizar Receitas](#visualizar-receitas)
  - [Visualizar Receitas Favoritas](#visualizar-receitas-favoritas)
  - [Atualizar Receita](#atualizar-receita)
  - [Deletar Receitas](#deletar-receitas)
  - [Adicionar uma Receita à Lista de Favoritos](#adicionar-uma-receita-à-lista-de-favoritos)
  - [Filtrar Receitas pelo País](#filtrar-receitas-pelo-país)
  - [Sugerir uma Receita Aleatória](#sugerir-uma-receita-aleatória)
  - [Escolher a Receita pelos Ingredientes](#escolher-a-receita-pelos-ingredientes)
  - [Sair do programa](#sair-do-programa)
- [Licença](#licença)
- [Fluxograma](#fluxograma-do-projeto)
- [Autores](#autores)

# Instalação
Para instalar e configurar o ambiente do projeto, siga as etapas abaixo:

1. Clone o repositório:
   git clone https://github.com/burle777/ProjetoCarol.git
2. Navegue até o diretório do projeto:
    cd ProjetoCarol

# Uso
## Adicionar Receitas
A primeira função do programa permite adicionar novas receitas ao livro de receitas.
### Exemplo de uso:
- O usuário insere o prompt 1.
- Insere o nome da receita.
- Insere o país de origem.
- Insere os ingredientes.
- Insere o modo de preparo.
- A receita é então adicionada.
#### Resultado:
    Nome da Receita: Bolo de Chocolate
    País de Origem: Brasil
    Ingredientes: Farinha, Açúcar, Ovos, Chocolate
    Modo de Preparo: Misture todos os ingredientes e asse por 30 minutos.


## Visualizar Receitas
A segunda função permite visualizar todas as receitas existentes no livro. As receitas são exibidas juntamente com seus países de origem, ingredientes e o modo de preparo.
#### Resultado:
    Bolo de Chocolate - Brasil
    Ingredientes: Farinha, Açúcar, Ovos, Chocolate
    Modo de Preparo: Misture todos os ingredientes e asse por 30 minutos.


## Visualizar Receitas Favoritas
A terceira função exibe as receitas que foram adicionadas à lista de favoritos. O programa retorna a lista de receitas favoritas. Caso nenhuma esteja adicionada, o programa retorna uma mensagem de que não há nenhuma receita favorita.
### Exemplo de uso:
- "1"
#### Resultado:
    (Receitas que foram adicionadas na lista.)


## Atualizar Receita
A quarta função permite atualizar uma receita existente. O usuário pode alterar o nome, o país, os ingredientes e o modo de preparo. Caso o usuário não queira alterar alguma das opções, ele deverá deixar em branco.
Após alterar a receita, ela é salva no livro de receitas.
### Exemplo de uso:
- "1"
#### Resultado:
    Novo Nome: Bolo de Cenoura
    Novo País de Origem: Brasil
    Novos Ingredientes: Farinha, Açúcar, Ovos, Cenoura
    Novo Modo de Preparo: Misture todos os ingredientes e asse por 25 minutos.


## Deletar Receitas
A quinta função permite excluir uma receita do livro de receitas. São mostradas na tela as receitas adicionadas anteriormente. O usuário insere o número da receita que deseja excluir. A receita é excluída. Caso o número da receita seja inválido, o programa não apaga nenhuma receita e retorna uma mensagem de erro.
### Exemplo de uso:
- "1(Bolo de cenoura)"
#### Resultado:
    Receita deletada com sucesso.


## Adicionar uma Receita à Lista de Favoritos
A sexta função permite adicionar uma receita à lista de favoritos. É pedido que ele insira o nome da receita que deseja adicionar à lista de favoritos. Caso o nome da receita não seja encontrado na lista, o programa retornará uma mensagem informando que a receita não foi encontrada.
### Exemplo de uso:
- "Bolo de cenoura"
#### Resultado:
    (Receita adicionada na lista de favoritos!)


## Filtrar Receitas pelo País
A sétima função permite filtrar receitas pelo país de origem. É pedido que ele insira o país das receitas que deseja ver.
O programa retorna as receitas do país escolhido pelo usuário. Caso nenhuma receita seja encontrada para o país selecionado, o programa retorna uma mensagem informando que nenhuma receita daquele país foi encontrada.
### Exemplo de uso:
- "Brasil"
#### Resultado:
    Bolo de cenoura


## Sugerir uma Receita Aleatória
A oitava função sugere uma receita aleatória ao usuário. O programa retorna uma receita aleatória da lista de receitas.
#### Resultado:
    Receita: Bolo de Cenoura
    Ingredientes: Farinha, Açúcar, Ovos, Cenoura
    Modo de Preparo: Misture todos os ingredientes e asse por 25 minutos.


## Escolher a Receita pelos Ingredientes
A nona função permite escolher uma receita com base nos ingredientes fornecidos. O programa pede que ele insira os ingredientes da receita.
Após digitar todos os ingredientes, o programa retorna as receitas que contêm os ingredientes inseridos pelo usuário. Caso nenhuma receita seja encontrada, o programa retorna uma mensagem informando que não foram encontradas receitas com os ingredientes desejados.
### Exemplo de uso:
- "Farinha, Açúcar, Ovos"
#### Resultado:
    Bolo de cenoura

## Sair do programa
Essa parte do programa faz com que o programa encerre quando o usuário inserir 0 no menu de opções.
#### Resultado:
    Saindo do sistema...


# Licença
Este projeto está protegido por direitos autorais e é licenciado sob os termos da MIT License. Consulte o arquivo [LICENSE](https://github.com/burle777/ProjetoCarol/blob/main/LICENSE.md) para obter mais informações.


# Fluxograma do projeto:
![Fluxograma Receitas](https://github.com/burle777/ProjetoCarol/blob/main/Fluxograma%20Carol%20-%20fluxograma%20carol.jpg)


# Autores
- Guilherme Mourão
- Henrique Tefile
- André Burle
- Guilherme Vinícius
