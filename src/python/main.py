"""painel Multimodal - Escola de Música
telemetria, guardrails e cálculo vetorial de embeddings (Norma Euclidiana com numpy)
"""

import json
from datetime import datetime

import numpy as np
from pyscript import document

# ======== dados ========
with open("dados.json", encoding="utf-8") as arquivo:
    DADOS = json.load(arquivo)

INSTRUMENTOS = DADOS["instrumentos"]

# ======== telemetria ========

def registrar(evento):
    """registra um evento com horário no painel de telemetria."""

    hora = datetime.now().strftime("%H:%M:%S")
    item = document.createElement("li")
    item.textContent = f"[{hora}] {evento}"
    document.getElementById("log-telemetria").prepend(item)

# ======== guardrails ========

TAMANHO_MAXIMO = 30
PALAVRAS_BLOQUEADAS = ["<script", "drop", "delete", "select", "--"]

def validar_entrada(texto):
    """Retorna (ok, mensagem). Bloqueia entradas vazias, longas ou suspeitas."""
    texto = texto.strip()
    if not texto:
        return False, "⚠️ Digite o nome de um instrumento."
    if len(texto) > TAMANHO_MAXIMO:
        return False, f"⚠️ Máximo de {TAMANHO_MAXIMO} caracteres."
    if any(p in texto.lower() for p in PALAVRAS_BLOQUEADAS):
        return False, "🚫 Entrada bloqueada pelo guardrail."
    if not all(c.isalpha() or c.isspace() for c in texto):
        return False, "⚠️ Use apenas letras."
    return True, texto


def buscar(event):
    entrada = document.getElementById("entrada-busca").value
    ok, resultado = validar_entrada(entrada)
    saida = document.getElementById("resultado-busca")

    if not ok:
        saida.textContent = resultado
        registrar(f"Guardrail acionado: {resultado}")
        return

    encontrados = [i for i in INSTRUMENTOS if resultado.lower() in i["nome"].lower()]
    if encontrados:
        i = encontrados[0]
        saida.textContent = f"✅ {i['nome']} · {i['familia']} · Nível {i['nivel']}"
    else:
        saida.textContent = "Instrumento não encontrado."
    registrar(f"Busca: '{resultado}' ({len(encontrados)} resultado(s))")

# ======== embeddings ========

def distancia_euclidiana(a, b):
    """Norma Euclidiana da diferença entre dois vetores: ||a - b||."""
    return float(np.linalg.norm(np.array(a) - np.array(b)))


def calcular_distancia(event):
    id_a = int(document.getElementById("instrumento-a").value)
    id_b = int(document.getElementById("instrumento-b").value)
    a = next(i for i in INSTRUMENTOS if i["id"] == id_a)
    b = next(i for i in INSTRUMENTOS if i["id"] == id_b)

    dist = distancia_euclidiana(a["embedding"], b["embedding"])
    document.getElementById("resultado-embedding").textContent = (
        f"Distância entre {a['nome']} e {b['nome']}: {dist:.4f}"
    )
    registrar(f"Embedding: {a['nome']} x {b['nome']} = {dist:.4f}")


# ======== Renderização ========
def renderizar_instrumentos():
    lista = document.getElementById("lista-instrumentos")
    lista.innerHTML = ""
    for i in INSTRUMENTOS:
        card = document.createElement("div")
        card.className = "instrumento"
        card.innerHTML = (
            f'<img src="{i["imagem"]}" alt="{i["nome"]}">'
            f"<strong>{i['nome']}</strong><small>{i['familia']}</small>"
        )
        lista.append(card)


def preencher_selects():
    for id_select in ("instrumento-a", "instrumento-b"):
        select = document.getElementById(id_select)
        for i in INSTRUMENTOS:
            opcao = document.createElement("option")
            opcao.value = str(i["id"])
            opcao.textContent = i["nome"]
            select.append(opcao)
    document.getElementById("instrumento-b").selectedIndex = 1


renderizar_instrumentos()
preencher_selects()
registrar(f"Painel carregado com {len(INSTRUMENTOS)} instrumentos.")