import os
import psutil
import socket

def criar_pasta_oculta():
    caminho_pasta = "C:\\monitoramento"
    if not os.path.exists(caminho_pasta):
        os.mkdir(caminho_pasta)
        os.system(f"attrib +h {caminho_pasta}")

def salvar_dados_em_arquivo(dados):
    caminho_arquivo = "C:\\monitoramento\\dados_monitoramento.txt"
    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(dados + "\n")

def obter_nome_usuario():
    return os.getlogin()

def obter_hostname():
    return socket.gethostname()

def monitorar_recursos():
    nome_usuario = obter_nome_usuario()
    hostname = obter_hostname()

    salvar_dados_em_arquivo(f"Usuário de rede: {nome_usuario}")
    salvar_dados_em_arquivo(f"Hostname do equipamento: {hostname}\n")

    # Monitoramento de CPU
    uso_cpu = psutil.cpu_percent()
    salvar_dados_em_arquivo(f"Uso da CPU: {uso_cpu:.2f}%")

    # Monitoramento de memória RAM
    uso_memoria = psutil.virtual_memory().percent
    salvar_dados_em_arquivo(f"Uso de memória RAM: {uso_memoria:.2f}%")

    # Monitoramento de espaço em disco (HD)
    uso_hd = psutil.disk_usage("C:\\").percent
    salvar_dados_em_arquivo(f"Uso de HD (C:\\): {uso_hd:.2f}%")

def listar_processos():
    processos = psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_percent"])
    processos_ordenados_por_memoria = sorted(processos, key=lambda x: x.info["memory_percent"], reverse=True)
    processos_ordenados_por_cpu = sorted(processos, key=lambda x: x.info["cpu_percent"], reverse=True)

    return processos_ordenados_por_memoria[:10], processos_ordenados_por_cpu[:10]

if __name__ == "__main__":
    criar_pasta_oculta()
    monitorar_recursos()
    print("Dados salvos em C:\\monitoramento\\dados_monitoramento.txt")

    processos_memoria, processos_cpu = listar_processos()

    salvar_dados_em_arquivo("\nPrincipais processos:")
    for processo in processos_memoria:
        salvar_dados_em_arquivo(f"PID: {processo.info['pid']} | Nome: {processo.info['name']} | Memória: {processo.info['memory_percent']:.2f}% | CPU: {processo.info['cpu_percent']:.2f}%")