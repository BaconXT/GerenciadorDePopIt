import time

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

pastaOrigem = "C:\\Users\\AN1\\Downloads"
pastaDestino = "C:\\Users\\AN1\\Python\\Projeto103\\ArquivosBaixados"

tiposArquivos = {
    "Imagens": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Videos": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Documentos": ['.ppt', '.xls', 'xlsx', '.csv', '.pdf',  '.txt'],
    "Executaveis":  ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        
        nome, extensao = os.path.splitext(event.src_path)
        time.sleep(1)
        
        for key, value in tiposArquivos.items():
            time.sleep(1)
            
            if extensao in value:
                nomeArquivo = os.path.basename(event.src_path)
                print("Baixando " + nomeArquivo)
                
                caminho1 = pastaOrigem + '/' + nomeArquivo
                caminho2 = pastaDestino + '/' + key
                caminho3 = pastaDestino + '/' + key + '/' + nomeArquivo
                
                if os.path.exists(caminho2):
                    
                    print("Diretório existente...")
                    print("Movendo " + nomeArquivo + "....")
                    shutil.move(caminho1, caminho3)
                    time.sleep(1)
                    
                else:
                    
                    print("Criando diretório...")
                    os.makedirs(caminho2)
                    print("Movendo " + nomeArquivo + "....")
                    shutil.move(caminho1, caminho3)
                    time.sleep(1)
                    
event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, pastaOrigem, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando....")
        
except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()