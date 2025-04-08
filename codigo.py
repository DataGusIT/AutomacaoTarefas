import pyautogui
import time
import pandas as pd

# Configura um intervalo padrão entre cada ação do PyAutoGUI
pyautogui.PAUSE = 0.5

# Abre o navegador Microsoft Edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Acessa o site de login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)  # Aguarda o carregamento da página

# Preenche e envia o formulário de login
pyautogui.click(x=659, y=452)  # Campo de e-mail
pyautogui.write("gustavo@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")  # Senha
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3.5)  # Aguarda o redirecionamento

# Carrega os dados da planilha CSV
tabela = pd.read_csv("produtos.csv")

# Loop para preencher o formulário de cadastro de produtos
for linha in tabela.index:
    # Clica no primeiro campo do formulário
    pyautogui.click(x=716, y=308)

    # Preenche os campos com os dados da planilha
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Verifica se há observações (obs)
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write("" if obs == "nan" else obs)
    pyautogui.press("tab")

    # Envia o formulário
    pyautogui.press("enter")

    # Faz scroll para mostrar o próximo formulário, se necessário
    pyautogui.scroll(10000)
