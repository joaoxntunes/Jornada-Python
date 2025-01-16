import pyautogui # automatização teclado e mouse
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Processo de Entrar no site/conta

pyautogui.press("win") # press > Pressionar uma tecla
pyautogui.write("chrome") # write > Texto
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=580, y=370) # click > Click do Mouse
pyautogui.write("admin")
pyautogui.press("tab") # hotkey > Atalho do teclado
pyautogui.write("root")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

for linha in tabela.index:
   pyautogui.click(x=586, y=264)
   pyautogui.write(str(tabela.loc[linha, "codigo"]))
   pyautogui.press("tab")
   # Repita os processos
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
   pyautogui.press("tab")
   pyautogui.press("enter")
   pyautogui.scroll(500000)
   time.sleep(0.5)