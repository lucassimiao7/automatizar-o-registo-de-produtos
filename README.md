# Automação de Registo de Produtos

Este projeto consiste num script em Python desenvolvido para automatizar o registo de produtos num sistema web. 
O bot lê uma base de dados em formato CSV e utiliza a automação de interface gráfica para preencher os formulários repetitivamente de forma automática.

Projeto desenvolvido com base nos exercícios do Intensivão de Python da Hashtag Treinamentos.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Para leitura e manipulação da base de dados CSV.
* **PyAutoGUI**: Para automação dos comandos de teclado e do rato (mouse).
* **Time**: Para gerir os tempos de espera de carregamento do sistema.

## 📋 Pré-requisitos

Para que o código funcione corretamente, é necessário ter o Python instalado no computador e instalar as bibliotecas externas necessárias. 

Abra o seu terminal ou prompt de comandos e execute:

```bash
pip install pandas pyautogui

```
Nota: Certifique-se de que o ficheiro produtos.csv se encontra na mesma pasta que o seu script Python.

🚀 Como Funciona
Ao executar o script, ele irá realizar os seguintes passos autonomamente:

1 - Importar a base de dados de produtos através da biblioteca Pandas.

2 - Abrir o navegador (Google Chrome) simulando as teclas do Windows.

3 - Aceder ao link da plataforma de login.

4 - Preencher as credenciais de acesso (email e palavra-passe) e entrar no sistema.

5 - Iniciar um ciclo (loop) que percorre cada linha do ficheiro CSV, registando os produtos passo a passo:

Código

Marca

Tipo

Categoria

Preço Unitário

Custo

Observações (caso o campo não esteja vazio)
``````
⚠️ Avisos e Configurações Importantes

Coordenadas do Ecrã: A biblioteca PyAutoGUI funciona baseada nas coordenadas (x, y) do seu monitor. Os pontos definidos nos comandos pyautogui.click() foram mapeados para o 
computador onde o código foi criado. Se executar noutro computador com uma resolução de ecrã diferente, terá de recalcular estas posições.

Tempos de Espera (Sleep): O comando time.sleep(7) aguarda 7 segundos para que a página web carregue.
Caso a sua internet seja mais lenta ou mais rápida, poderá precisar de ajustar este valor.

Velocidade de Execução: Verifique o seu comando pyautogui.PAUSE = 60. Isto diz ao programa para esperar 60 segundos entre cada comando do teclado/mouse.
Se quiser que a automação corra depressa, sugere-se alterar para um valor mais baixo, como pyautogui.PAUSE = 0.5.

Digitação do Navegador: No código original está escrito pyautogui.write("chorme"). Dependendo do sistema operativo, pode ser necessário corrigir a ortografia para "chrome"
para que a pesquisa do Windows encontre o navegador corretamente.
