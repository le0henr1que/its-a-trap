import time
import pyautogui
import cv2
import keyboard
import subprocess
import easygui
import pygame
import pygetwindow as gw
import win32gui
import win32con

tempo_espera = 1

while True:
    posicao_inicial = pyautogui.position()

    time.sleep(tempo_espera)

    posicao_final = pyautogui.position()

    if posicao_final != posicao_inicial:
        numero_de_fotos = 5

        camera = cv2.VideoCapture(0)

        for i in range(numero_de_fotos):
            _, imagem = camera.read()

            nome_arquivo = f"foto_{i+1}.jpg"
            cv2.imwrite(nome_arquivo, imagem)

        camera.release()

        print("Mouse movido! Fotos capturadas.")
        path_gif = './GlisteningBlankEidolonhelvum-size_restricted.gif'
        pygame.init()
        largura = 400
        altura = 300
        janela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Its a trap")
       # Obter o identificador da janela do Pygame
        hwnd = pygame.display.get_wm_info()["window"]

        # Definir a janela sempre no topo
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        gif = pygame.image.load(path_gif)


        fonte = pygame.font.SysFont("Arial", 20)
        mensagem = fonte.render("Mensagem para o usuário", True, (255, 255, 255))  
        janela.blit(mensagem, (50, 50))  
        janela.blit(gif, (0, 0))


        pygame.display.flip()
        pygame.display.update()

    
        pygame.time.wait(1500)  

  
        pygame.quit()
      
        subprocess.call("rundll32.exe user32.dll,LockWorkStation")

        break