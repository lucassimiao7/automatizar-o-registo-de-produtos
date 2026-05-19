import pyautogui
import pandas as pd
import time

#tempo de espera dos comandos#
pyautogui.PAUSE - 60

# importar a base de dados #
tabela = pd.read_csv("produtos.csv")
print(tabela)

#abrir o sistema

pyautogui.press ("win")
pyautogui.write("chorme")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar a tela carregar#
time.sleep(7)

# POSIÇÃO LOGIN x=942, y=375)
#posição senha (x=1007, y=472)

#fazer login no site
pyautogui.click(x=942, y=375)
pyautogui.write("Projeotodeautomação@gmail.com")
pyautogui.press("tab")
pyautogui.write("automação2026")
pyautogui.click(x=963, y=536)
pyautogui.press("enter")

#registrar os produtos de cada linha#
for linha in tabela.index:
    pyautogui.click(x=1067, y=257)
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
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.click(x=867, y=775)
        pyautogui.scroll(5000)


    



