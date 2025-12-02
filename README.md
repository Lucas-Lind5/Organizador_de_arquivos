# Organizador de Arquivos 📁

Um script Python automático que organiza arquivos na pasta Downloads agrupando-os por tipo de extensão em subpastas.

## 📋 Características

- ✅ Organiza automaticamente arquivos por categoria (Imagens, Documentos, Vídeos, etc.)
- ✅ Detecta extensões de arquivo e move para pasta correspondente
- ✅ Cria subpastas automaticamente se não existirem
- ✅ Evita sobrescrita de arquivos duplicados com contador automático
- ✅ Registra todas as operações em arquivo de log (`logs/log.txt`)
- ✅ Tratamento de erros robusto
- ✅ Interface amigável com feedback visual

## 📁 Estrutura do Projeto

```
projeto 1/
├── main.py              # Script principal de organização
├── config.py            # Configuração de mapeamento de extensões
├── logs/                # Pasta para armazenar logs (criada automaticamente)
│   └── log.txt         # Arquivo de registro de operações
└── README.md           # Este arquivo
```

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6+
- As bibliotecas padrão do Python (pathlib, shutil, logging)

### Instalação

1. **Clone ou baixe o projeto:**
   ```powershell
   cd "c:\Users\Windows 10\Desktop\Projetos\projeto 1"
   ```

2. **Nenhuma dependência externa necessária** - todas as bibliotecas são padrão do Python

### Execução

Execute o script no terminal PowerShell:

```powershell
python main.py
```

Você verá uma saída similar a:
```
Iniciando organização de arquivos...
Pasta de origem: C:\Users\Windows 10\Downloads

✓ Movido: foto.jpg → Imagens/foto.jpg
✓ Movido: documento.pdf → Documentos/documento.pdf
✓ Movido: musica.mp3 → Audio/musica.mp3

Organização concluída!
```

## 📊 Categorias Suportadas

O script reconhece as seguintes categorias de arquivo:

| Categoria | Extensões |
|-----------|-----------|
| **Imagens** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| **Documentos** | .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .txt, .odt |
| **Vídeos** | .mp4, .avi, .mkv, .mov, .flv, .wmv, .webm |
| **Áudio** | .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a |
| **Arquivos** | .zip, .rar, .7z, .tar, .gz, .iso |
| **Códigos** | .py, .js, .html, .css, .java, .cpp, .c, .php, .rb, .go |
| **Executáveis** | .exe, .msi, .bat, .cmd, .sh |
| **Outros** | Qualquer extensão não reconhecida |

## ⚙️ Configuração

Para adicionar ou modificar categorias, edite o arquivo `config.py`:

```python
EXTENSOES_MAPA = {
    'MinhaCategoria': ['.ext1', '.ext2', '.ext3'],
    'OutraCategoria': ['.ext4', '.ext5'],
    # ... mais categorias
}
```

## 📝 Logs

Todas as operações são registradas em `logs/log.txt` com:
- Data e hora da operação
- Nome do arquivo original
- Pasta de destino
- Erros encontrados (se houver)

**Exemplo de log:**
```
02/12/2025 14:30:45 - Arquivo movido: 'foto.jpg' → 'Imagens/foto.jpg'
02/12/2025 14:30:46 - Arquivo movido: 'documento.pdf' → 'Documentos/documento.pdf'
02/12/2025 14:30:47 - Erro ao mover 'arquivo_bloqueado.zip': [Permission denied]
```

## 🛡️ Tratamento de Duplicatas

Se um arquivo com o mesmo nome já existir na pasta de destino, o script adiciona um contador:

- `foto.jpg` (primeiro arquivo)
- `foto_1.jpg` (duplicata)
- `foto_2.jpg` (outra duplicata)

Isso evita perda de dados por sobrescrita.

## ⚠️ Observações Importantes

1. **Pasta de Origem**: O script sempre organiza arquivos da pasta `Downloads` do usuário
2. **Diretórios**: Subpastas na pasta Downloads não são processadas, apenas arquivos
3. **Backup**: Considere fazer backup de seus arquivos antes da primeira execução
4. **Permissões**: O script necessita de permissões de leitura/escrita na pasta Downloads
5. **Arquivos em Uso**: Arquivos abertos não podem ser movidos

## 🔧 Solução de Problemas

### Erro: "A pasta ... não existe"
A pasta Downloads não foi encontrada. Verifique se existe em seu computador.

### Erro: "Permission denied"
Um arquivo está aberto em outro programa. Feche o arquivo e tente novamente.

### Nenhum arquivo foi movido
Verifique se há arquivos realmente na pasta Downloads (não apenas subpastas).

## 📚 Arquivos do Projeto

- **main.py**: Script principal com a função `organizar_arquivos()`
- **config.py**: Dicionário `EXTENSOES_MAPA` com mapeamento de extensões
- **logs/log.txt**: Arquivo de histórico (criado automaticamente)

## 💡 Exemplos de Uso Avançado

### Rodar manualmente com feedback detalhado
```python
from main import organizar_arquivos

organizar_arquivos()
```

### Adicionar novas categorias
Edite `config.py` e adicione:
```python
'Planilhas': ['.csv', '.tsv', '.ods']
```

## 📄 Licença

Projeto livre para uso pessoal e educacional.


