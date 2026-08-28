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

    timestamp = f"{partes[0]}, {partes[1]}"

    print(timestamp)

linha_teste = "2025-02-20 08:15:01 FAIL usuario=admin ip=185.220.101.1"
parsear_linha_auth(linha_teste)

def parsear_linha_firewall(linha):
    """Parseia uma linha do firewall.log e retorna dict normalizado."""

def parsear_linha_web(linha):
    """Parseia uma linha do web_access.log e retorna dict normalizado."""

def carregar_todos_os_logs(pasta_logs):
    """
    Lê todos os arquivos de log da pasta e retorna lista unificada.
    Usa os.listdir() para encontrar os arquivos.
    """