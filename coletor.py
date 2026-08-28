def carregar_log(caminho_arquivo, fonte):
    """
    Lê um arquivo de log e retorna lista de eventos normalizados.
    - caminho_arquivo: str com o path do arquivo
    - fonte: str indicando o tipo ("auth", "firewall", "web")
    - Retorna: list[dict] com os eventos parseados
    """


def parsear_linha_auth(linha):
    """Parseia uma linha do auth.log e retorna dict normalizado."""

    linha_limpa = linha.strip()
    partes = linha_limpa.split()

    if len(partes) != 5:
        print(f"[AVISO] Formato de log não aceito")
        return None

    if not partes[3].startswith("usuario="):
        print(f"[AVISO] Campo de IP inválido: {linha_limpa}")
        return None

    if not partes[4].startswith("ip="):
        print(f"[AVISO] Campo de IP inválido: {linha_limpa}")
        return None

    timestamp = f"{partes[0]}, {partes[1]}"
    partes_ip = partes[4].split("=")
    tipo = partes[2]
    detalhes = partes[3]

    print(detalhes)
    print(tipo)
    ip = partes_ip[1]
    print(timestamp)

    evento = {
        "timestamp": timestamp,
        "fonte": "auth",
        "tipo": tipo,
        "ip": ip,
        "detalhes": detalhes,
        "linha_original": linha_limpa
    }

    return evento

linha_valida = (
    "2025-02-20 08:15:01 FAIL "
    "usuario=admin ip=185.220.101.1"
)

linha_invalida = "linha sem formato"

print(parsear_linha_auth(linha_valida))
print(parsear_linha_auth(linha_invalida))

def parsear_linha_firewall(linha):
    """Parseia uma linha do firewall.log e retorna dict normalizado."""

def parsear_linha_web(linha):
    """Parseia uma linha do web_access.log e retorna dict normalizado."""

def carregar_todos_os_logs(pasta_logs):
    """
    Lê todos os arquivos de log da pasta e retorna lista unificada.
    Usa os.listdir() para encontrar os arquivos.
    """