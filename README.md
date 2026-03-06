# 🎵 YouTube Downloader

Aplicativo simples e poderoso para baixar vídeos e músicas do YouTube diretamente para o seu PC, com interface gráfica intuitiva usando Python + Tkinter + yt-dlp.

---

## ✨ Funcionalidades

✅ Baixar vídeos em **MP4**  
✅ Baixar músicas em **MP3**  
✅ Interface amigável com **log em tempo real**  
✅ Escolha da **pasta de destino**  
✅ Totalmente offline — pode rodar sem instalação externa  
✅ Compatível com **Windows**   
✅ **FFmpeg embutido**

---

## 🖼️ Interface

<img src="https://raw.githubusercontent.com/oliveiraNeto-blnk/Yt-Downloader/main/docs/interface.png" alt="Interface do aplicativo" width="400">

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/):** Linguagem principal.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Interface gráfica (GUI).
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** Motor de download robusto e atualizado.
- **[FFmpeg](https://ffmpeg.org/):** Processamento e conversão de mídia.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado.
- FFmpeg (já incluído na pasta `ffmpeg/` para Windows).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/blnkDev/Yt-Downloader.git
   cd Yt-Downloader
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o aplicativo:**
   ```bash
   python baixador.py
   ```

---

## 📦 Como Gerar o Executável (.exe)

Se você quiser gerar um executável para Windows usando o `PyInstaller`:

```bash
pip install pyinstaller
pyinstaller baixador.spec
```

O executável será gerado na pasta `dist/`.

---

## 🤝 Contribuições

Sinta-se à vontade para abrir **Issues** ou enviar um **Pull Request**. Toda ajuda é bem-vinda!

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
