# 🐍 Automação de Cadastro de Produtos com PyAutoGUI

Este projeto utiliza **Python**, **PyAutoGUI** e **Pandas** para automatizar o processo de login e cadastro de produtos em um sistema web. Os dados são lidos de um arquivo `.csv` e preenchidos automaticamente em um formulário online.

## 📋 Funcionalidades

- Abertura automática do navegador Microsoft Edge
- Acesso a um site de login e preenchimento automático das credenciais
- Leitura de dados a partir de um arquivo `produtos.csv`
- Preenchimento e envio de formulários com os dados de cada produto

## 📂 Estrutura do Projeto

```
📁 automacao-cadastro
├── produtos.csv
├── codigo.py
├── auxiliar.py
└── README.md
```

## 🛠 Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes pacotes Python instalados:

```bash
pip install pyautogui pandas
```

**Nota:** Para sistemas Windows, o `PyAutoGUI` pode exigir permissões adicionais dependendo das configurações de segurança.

## ▶️ Como Usar

1. Certifique-se de que o arquivo `produtos.csv` esteja no mesmo diretório do script.
2. Atualize as informações de login (`email` e `senha`) no código, se necessário.
3. Execute o script:

```bash
python cadastro_automacao.py
```

O navegador será aberto e o processo de automação começará. **Evite mover o mouse ou digitar durante a execução.**

## 📝 Exemplo de produtos.csv

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,MarcaA,TipoX,Categoria1,19.90,10.00,Produto em promoção
002,MarcaB,TipoY,Categoria2,29.90,15.00,
...
```

## ⚠️ Aviso de Segurança

⚠️ **Nunca compartilhe dados reais de login ou arquivos com informações sensíveis.** Este projeto é apenas para fins educacionais.

## 📌 Tecnologias Utilizadas

* Python
* PyAutoGUI
* Pandas

## 🤖 Autor

Desenvolvido por **Gustavo Moreno Souza**  
📧 [g.moreno.souza05@gmail.com](mailto:g.moreno.souza05@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/gustavo-moreno-8a925b26) 

> "Automatizar tarefas repetitivas é libertar tempo para o que realmente importa." 🚀
