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

    
