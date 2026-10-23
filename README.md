# Painel Multimodal para Escola de Musica

Checkpoint 2 da disciplina de IA & ML - Engenharia de Software - turma 3ESPA.

## Integrantes

| Integrante | RM | Papel sugerido |
|---|---:|---|
| Maria Eduarda Ferrés | 560418 | Interface HTML e estilos |
| Davi Corrêa Paião | 560438 | Tech Lead, GitHub e integracao |
| Gabriela Queiroga Cocuzza da Silva | 560035 | Python, JSON e ativos |

## Objetivo

Construir um sistema web interativo para uma Escola de Musica utilizando HTML, CSS, JSON e Python via PyScript.

## Estrutura

```text
.
|-- index.html
|-- integrantes.txt
|-- src/
|   |-- assets/
|   |-- css/
|   |   `-- estilo.css
|   `-- python/
|       |-- dados.json
|       `-- main.py
`-- README.md
```

## Fluxo Git

1. Clonar o repositorio.
2. Atualizar a branch `dev`.
3. Criar uma feature branch a partir de `dev`.
4. Fazer no minimo 3 commits semanticos por tarefa.
5. Enviar a feature branch.
6. Abrir Pull Request com destino para `dev`.
7. Aguardar o Code Review do Tech Lead.
8. Ao final, o Tech Lead integra `dev` em `main`.

### Comandos iniciais

```bash
git clone https://github.com/escola-de-musica-3espa/painel-multimodal-escola-de-musica.git
cd painel-multimodal-escola-de-musica
git checkout dev
git pull origin dev
git checkout -b feature/nome-da-tarefa
```

## Sugestao de tarefas e branches

### Maria - `feature/interface-painel`

- Estruturar o painel em `index.html`.
- Criar o layout responsivo em `src/css/estilo.css`.
- Integrar a interface com os elementos do PyScript.

Sugestoes de commits:

```text
feat(ui): cria estrutura semantica do painel
style(ui): implementa grid responsivo e identidade visual
feat(ui): integra controles da interface com o PyScript
```

### Gabriela - `feature/dados-telemetria`

- Preencher `src/python/dados.json` com os instrumentos.
- Implementar telemetria e guardrails em `src/python/main.py`.
- Implementar a Norma Euclidiana dos embeddings com NumPy.

Sugestoes de commits:

```text
data(instruments): adiciona base de instrumentos musicais
feat(telemetry): implementa telemetria e guardrails
feat(embeddings): calcula norma euclidiana com numpy
```

### Davi - Tech Lead

- Manter as branches `main` e `dev`.
- Revisar os Pull Requests.
- Solicitar correcoes quando necessario.
- Fazer os merges finais e conferir a entrega.

Sugestoes de commits:

```text
docs(readme): documenta projeto e fluxo de trabalho
docs(team): adiciona identificacao dos integrantes
chore(structure): cria estrutura inicial do projeto
```

## Regra dos Pull Requests

Todo Pull Request de funcionalidade deve usar:

- base: `dev`
- compare: a feature branch do integrante
- titulo objetivo e descricao do que foi implementado
- pelo menos 3 commits semanticos por tarefa

O merge para `main` sera feito pelo Tech Lead somente depois da validacao final.
