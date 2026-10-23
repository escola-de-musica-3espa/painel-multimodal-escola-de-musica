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


