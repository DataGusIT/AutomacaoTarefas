# Automação de Cadastro de Produtos

> Robô de automação (RPA) que realiza o cadastro de produtos em um sistema web a partir de uma planilha, utilizando Python, Pandas e PyAutoGUI para simular a interação humana.

[![Status](https://img.shields.io/badge/Status-Funcional-success)](https://github.com/seu-usuario/automacao-cadastro-pyautogui)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB)](https://www.python.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automação_GUI-000000)](https://pyautogui.readthedocs.io/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

## Sobre o Projeto

Este projeto demonstra uma solução de Automação de Processos Robóticos (RPA) para uma tarefa comum e repetitiva: o cadastro de produtos em um sistema web. A automação lê os dados de uma planilha (`produtos.csv`), abre o navegador, realiza o login no sistema e preenche o formulário de cadastro para cada produto listado, simulando cliques de mouse e digitação de teclado.

O objetivo é eliminar o trabalho manual, reduzir a chance de erros humanos e liberar tempo para tarefas mais estratégicas. Como diz o ditado: *"Automatizar tarefas repetitivas é libertar tempo para o que realmente importa."* 🚀

## ✨ Funcionalidades

-   **Leitura de Dados em Lote:** Utiliza a biblioteca **Pandas** para ler de forma eficiente todos os produtos de um arquivo `.csv`.
-   **Navegação e Login Automatizados:** Abre o navegador (Microsoft Edge, neste caso), navega até a página de login e insere as credenciais de forma automática.
-   **Preenchimento Dinâmico de Formulários:** Itera sobre cada linha da planilha e preenche os campos do formulário de cadastro de produtos com os dados correspondentes.
-   **Controle de Interface Gráfica (GUI):** Usa o **PyAutoGUI** para controlar o mouse e o teclado, clicando em botões, preenchendo campos de texto e navegando pela interface do sistema web.

## Tecnologias

### Core
-   **Python 3.9+** - Linguagem principal da automação.

### Ferramentas de Automação e Dados
-   **PyAutoGUI** - Para automação da interface gráfica do usuário (GUI).
-   **Pandas** - Para leitura e manipulação dos dados da planilha.

## Pré-requisitos

-   Python 3.9 ou superior instalado.
-   O navegador Microsoft Edge (ou o navegador de sua preferência, com o código ajustado).

## Instalação e Uso

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/seu-usuario/automacao-cadastro-pyautogui.git
    cd automacao-cadastro-pyautogui
    ```

2.  **Instale as dependências**
    ```bash
    pip install pyautogui pandas
    ```

3.  **Prepare o arquivo de dados**
    -   Certifique-se de que o arquivo `produtos.csv` está na mesma pasta.
    -   Preencha-o com os produtos que deseja cadastrar, seguindo o formato do exemplo abaixo.

4.  **Execute o script**
    ```bash
    python codigo.py
    ```

⚠️ **Importante:** Após executar o script, **não utilize o mouse ou o teclado**. A automação precisa de controle total sobre eles para funcionar corretamente.

### Estrutura do Arquivo `produtos.csv`

O arquivo de dados deve seguir esta estrutura de colunas:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Molin,Caneta,Papelaria,5.50,2.10,Caneta esferográfica azul.
LOGI000341,Logitech,Mouse,Informática,89.90,45.00,Mouse sem fio.
COCA000252,Coca-Cola,Refrigerante,Bebidas,9.00,3.50,
```

## ⚠️ Avisos Importantes

-   **Segurança:** Este projeto é para fins educacionais. **Nunca** insira senhas ou dados sensíveis diretamente no código em um ambiente de produção nem compartilhe arquivos com credenciais reais.
-   **Resolução de Tela:** As coordenadas do PyAutoGUI são baseadas na resolução da tela. O script pode precisar de ajustes nas coordenadas (`pyautogui.click(x=..., y=...)`) se for executado em um monitor com resolução diferente daquela em que foi desenvolvido.

## Suporte e Contato

-   **Email**: [g.moreno.souza05@gmail.com](mailto:g.moreno.souza0s@gmail.com)
-   **LinkedIn**: [Gustavo Moreno Souza](https://www.linkedin.com/in/gustavo-moreno-8a925b26a/)

## Licença

Este projeto está licenciado sob uma Licença Proprietária.

**Uso Restrito**: Este software é de propriedade exclusiva do autor. Uso comercial ou redistribuição requer autorização expressa.

---

<div align="center">
  Desenvolvido por Gustavo Moreno Souza
  <br><br>
  <a href="https://www.linkedin.com/in/gustavo-moreno-8a925b26a/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" alt="LinkedIn"/>
  </a>
</div>
