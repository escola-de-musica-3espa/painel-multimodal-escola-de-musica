"""Ponto de entrada do painel executado pelo PyScript.

As funcionalidades de telemetria, guardrails e embeddings devem ser
implementadas na feature branch designada para a tarefa.
"""

from pyscript import display


def iniciar_painel() -> None:
    """Confirma que a estrutura inicial foi carregada corretamente."""
    display(
        "Estrutura inicial pronta. Implemente telemetria, guardrails e embeddings.",
        target="status",
    )


iniciar_painel()
