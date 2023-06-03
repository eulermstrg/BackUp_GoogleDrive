import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Configuração de autenticação
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Pasta local contendo os arquivos .xls
pasta_local = "C:/Users/Euler Magno/Documents/ARQUIVOS PARA BACKUP"

# ID da pasta de backup no Google Drive
pasta_backup_id = "1Bu_FY4Dl_i8wmzAPxkoGKJBb3-v1E8My"

# Obtém a lista de arquivos já existentes no Google Drive
arquivos_drive = drive.ListFile({'q': f"'{pasta_backup_id}' in parents and trashed=false"}).GetList()
nomes_arquivos_drive = [arquivo['title'] for arquivo in arquivos_drive]

# Percorre todos os arquivos na pasta local
for arquivo in os.listdir(pasta_local):
    if arquivo.endswith(".xlsx") and arquivo not in nomes_arquivos_drive:
        # Caminho completo do arquivo local
        caminho_local = os.path.join(pasta_local, arquivo)

        # Cria um objeto de arquivo no Google Drive
        arquivo_drive = drive.CreateFile({'title': arquivo, 'parents': [{'id': pasta_backup_id}]})

        # Define o arquivo local como conteúdo do arquivo no Google Drive
        arquivo_drive.SetContentFile(caminho_local)

        # Envia o arquivo para o Google Drive
        arquivo_drive.Upload()

        # Exibe a mensagem de sucesso
        print(f"Arquivo {arquivo} enviado com sucesso para o Google Drive.")
