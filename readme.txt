Projeto:

O projeto é um sistema de gerenciamento de receitas em Python que permite adicionar, visualizar, atualizar, deletar, filtrar receitas por país, buscar receitas por ingredientes 
e marcar receitas favoritas. As receitas são armazenadas em um arquivo CSV para manipulação fácil e persistência de dados.





Recursos:

1. Adicionar nova receita: Permite adicionar uma nova receita ao sistema.
2. Visualizar todas as receitas: Exibe todas as receitas que foram cadastradas no sistema.
3. Atualizar receita existente: Permite atualizar informações de uma receita do sistema.
4. Deletar Receita: Permite deletar uma receita.
5. Filtrar as receitas pelo país: Exibe receitas de um país escolhido.
6. Receita Aleatória: Sugere uma receita randômica entre as cadastradas.
7. Marcar receita como favoritas: Permite o usuário marcar uma receita como sua favorita.
8. Escolher receita por ingredientes: Busca receitas que contenham determinados ingredientes.





Requisitos:

Ter instalada uma versão do Python 3.x com as bibliotecas 'os', 'csv' e 'random', que são nativas do próprio Python.





Como Usar:

1. Clone o repositório ou copie o código para seu aparelho.
2. Execute o script python nome_do_arquivo.py (substitua nome_do_arquivo.py pelo nome do arquivo onde o código está salvo).
3. Siga as instruções no menu principal para interagir com o sistema.





Codificação do projeto:

- `arquivo_receitas`: Nome do arquivo CSV no qual as receitas são armazenadas.
- `limpar_tela()`: Função usada para limpar a tela do terminal.
- `menu_principal()`: Exibe o menu principal e gerencia as opções escolhidas pelo usuário.
- `adicionar_receita()`: Adiciona uma nova receita ao arquivo CSV.
- `visualizar_receitas()`: Exibe todas as receitas armazenadas no arquivo CSV.
- `atualizar_receita()`: Atualiza as informações de uma receita existente.
- `deletar_receita()`: Deleta uma receita do arquivo CSV.
- `filtrar_por_pais()`: Filtra e exibe receitas de um país específico.
- `receita_aleatoria()`: Sugere uma receita aleatória.
- `buscar_por_ingredientes()`: Busca receitas que contenham ingredientes específicos.
- `fav()`: Marca uma receita como favorita.





Exemplo de Uso:

1. Adicionar Nova Receita:
   * Escolha a opção 1 no menu.
   * Forneça o nome da receita, país de origem, ingredientes (separados por vírgula) e modo de preparo.

2. Visualizar Todas as Receitas:
   * Escolha a opção 2 no menu.
   * Todas as receitas serão exibidas com seus respectivos detalhes.

3. Atualizar Receita Existente:
   * Escolha a opção 3 no menu.
   * Forneça o número da receita a ser atualizada e os novos detalhes.

4. Deletar Receita:
   * Escolha a opção 4 no menu.
   * Forneça o número da receita a ser deletada.

5. Filtrar Receitas Por País:
   * Escolha a opção 5 no menu.
   * Forneça o país cujas receitas deseja visualizar.

6. Sugestão de Receita Aleatória:
   * Escolha a opção 6 no menu.
   * Uma receita aleatória será exibida.

7. Adicionar Receita aos Favoritos:
   * Escolha a opção 7 no menu.
   * Forneça o nome da receita que deseja marcar como favorita.
   * A receita será salva como favorita e poderá ser acessada mais facilmente.

8. Escolher Receita por Ingredientes:
   * Escolha a opção 8 no menu.
   * Forneça os ingredientes desejados (separados por vírgula).
