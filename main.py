from pathlib import Path
import shutil
import logging
from datetime import datetime
from config import EXTENSOES_MAPA

# Definir a pasta de origem (Downloads)
PASTA_DOWNLOADS = Path.home() / 'Downloads'
PASTA_LOGS = Path.cwd() / 'logs'

# Criar pasta de logs se não existir
PASTA_LOGS.mkdir(exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename=PASTA_LOGS / 'log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    encoding='utf-8'
)

def organizar_arquivos():
    """
    Organiza os arquivos da pasta Downloads em subpastas baseado na extensão do arquivo.
    """
    if not PASTA_DOWNLOADS.exists():
        print(f"Erro: A pasta {PASTA_DOWNLOADS} não existe.")
        return
    
    # Iteração sobre todos os arquivos na pasta Downloads
    for arquivo in PASTA_DOWNLOADS.iterdir():
        # Pular diretórios
        if arquivo.is_dir():
            continue
        
        # Obter a extensão do arquivo (em minúsculas)
        extensao = arquivo.suffix.lower()
        
        # Encontrar a pasta de destino para esta extensão
        pasta_destino = None
        for categoria, extensoes in EXTENSOES_MAPA.items():
            if extensao in extensoes:
                pasta_destino = categoria
                break
        
        # Se a extensão não for reconhecida, mover para pasta "Outros"
        if pasta_destino is None:
            pasta_destino = 'Outros'
        
        # Criar a subpasta se não existir
        caminho_pasta_destino = PASTA_DOWNLOADS / pasta_destino
        caminho_pasta_destino.mkdir(exist_ok=True)
        
        # Mover o arquivo para a subpasta de destino
        try:
            caminho_arquivo_destino = caminho_pasta_destino / arquivo.name
            
            # Verificar se o arquivo já existe e adicionar contador se necessário
            if caminho_arquivo_destino.exists():
                nome_base = arquivo.stem  # Nome sem extensão
                extensao = arquivo.suffix  # Extensão do arquivo
                contador = 1
                
                # Procurar um nome disponível
                while caminho_arquivo_destino.exists():
                    novo_nome = f"{nome_base}_{contador}{extensao}"
                    caminho_arquivo_destino = caminho_pasta_destino / novo_nome
                    contador += 1
            
            shutil.move(str(arquivo), str(caminho_arquivo_destino))
            mensagem_log = f"Arquivo movido: '{arquivo.name}' → '{pasta_destino}/{caminho_arquivo_destino.name}'"
            logging.info(mensagem_log)
            print(f"✓ Movido: {arquivo.name} → {pasta_destino}/{caminho_arquivo_destino.name}")
        except Exception as e:
            mensagem_erro = f"Erro ao mover '{arquivo.name}': {e}"
            logging.error(mensagem_erro)
            print(f"✗ {mensagem_erro}")

if __name__ == '__main__':
    print("Iniciando organização de arquivos...")
    print(f"Pasta de origem: {PASTA_DOWNLOADS}\n")
    organizar_arquivos()
    print("\nOrganização concluída!")
