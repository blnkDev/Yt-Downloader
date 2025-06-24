import yt_dlp #lib pra fazer interações com o yt
import tkinter as tk #lib pra interface
from tkinter import filedialog, messagebox, scrolledtext
import os
import sys

pasta_destino = ""

def log_mensagem(msg, tipo="info"):
    cor = {
        "info": "black",
        "ok": "green",
        "erro": "red",
        "status": "blue"
    }.get(tipo, "black")

    caixa_log.insert(tk.END, f"{msg}\n")
    caixa_log.tag_add(tipo, f'end-{len(msg)+1}c', 'end')
    caixa_log.tag_config(tipo, foreground=cor)
    caixa_log.see(tk.END)
    janela.update()

def progresso_hook(d):
    if d['status'] == 'downloading':
        total = d.get('_percent_str', '').strip()
        velocidade = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        log_mensagem(f"[STATUS] Baixando... {total} a {velocidade} | ETA: {eta}", "status")
    elif d['status'] == 'finished':
        log_mensagem("[STATUS] Finalizando...", "status")

def caminho_ffmpeg():
    #./ffmpeg/ffmpeg.exe
    diretorio_base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    caminho = os.path.join(diretorio_base, 'ffmpeg', 'ffmpeg.exe')
    return caminho if os.path.isfile(caminho) else "ffmpeg"

def baixar_video():
    url = entrada_url.get()
    formato = formato_var.get()
    destino = pasta_destino or filedialog.askdirectory(title="Escolha a pasta de destino")

    if not url or not destino:
        log_mensagem("[ERRO] Forneça um link e selecione uma pasta!", "erro")
        return

    entrada_url.config(state='disabled')
    botao.config(state='disabled')
    log_mensagem(f"[INFO] Iniciando download de:\n{url}", "info")
    log_mensagem(f"[INFO] Formato: {formato.upper()}", "info")
    log_mensagem(f"[INFO] Pasta: {destino}", "info")

    try:
        ffmpeg_path = caminho_ffmpeg()

        if formato == "mp3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{destino}/%(title)s.%(ext)s',
                'merge_output_format': 'mp3',
                'ffmpeg_location': ffmpeg_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'progress_hooks': [progresso_hook]
            }
        else:
            ydl_opts = {
                'format': 'mp4',
                'outtmpl': f'{destino}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
                'ffmpeg_location': ffmpeg_path,
                'progress_hooks': [progresso_hook]
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            log_mensagem(f"[INFO] Título: {info.get('title', 'Desconhecido')}", "info")
            ydl.download([url])

        log_mensagem("[SUCESSO] Download concluído!", "ok")
        entrada_url.delete(0, tk.END)

    except Exception as e:
        log_mensagem(f"[ERRO] {str(e)}", "erro")
        messagebox.showerror("Erro", f"Falha no download:\n{str(e)}")

    entrada_url.config(state='normal')
    botao.config(state='normal')

def escolher_pasta():
    global pasta_destino
    pasta = filedialog.askdirectory(title="Escolha a pasta de destino")
    if pasta:
        pasta_destino = pasta
        log_mensagem(f"[INFO] Pasta selecionada: {pasta}", "info")

# Interface
janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("600x500")
janela.resizable(False, False)

# centralizar
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
largura_janela = 600
altura_janela = 500
x = (largura_tela // 2) - (largura_janela // 2)
y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

# visual
tk.Label(janela, text="Cole o link do YouTube:", font=("Arial", 12)).pack(pady=10)
entrada_url = tk.Entry(janela, width=60)
entrada_url.pack(pady=5)

formato_var = tk.StringVar(value="mp4")
formato_frame = tk.Frame(janela)
tk.Label(formato_frame, text="Formato:", font=("Arial", 10)).pack(side="left", padx=5)
tk.Radiobutton(formato_frame, text="MP4", variable=formato_var, value="mp4").pack(side="left")
tk.Radiobutton(formato_frame, text="MP3", variable=formato_var, value="mp3").pack(side="left")
formato_frame.pack(pady=5)

botao_pasta = tk.Button(janela, text="Selecionar pasta de destino", command=escolher_pasta)
botao_pasta.pack(pady=5)

botao = tk.Button(janela, text="Baixar", command=baixar_video, bg="#1e90ff", fg="white", font=("Arial", 11, "bold"))
botao.pack(pady=10)

caixa_log = scrolledtext.ScrolledText(janela, width=70, height=15, font=("Consolas", 10))
caixa_log.pack(padx=10, pady=10)

janela.mainloop()
