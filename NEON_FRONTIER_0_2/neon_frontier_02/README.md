# NEON FRONTIER 0.2

Versão principal atualizada do GAME-1: protótipo original de exploração urbana, construção e NPCs com memória.

## Executar
Abra `index.html` num navegador moderno. Sem servidor ou dependências.

## Funcionalidades
- Exploração de mapa 2D com obstáculos e descobertas.
- Construir/remover blocos.
- Save persistente via `localStorage`.
- NPCs com memória de encontros, histórico limitado e confiança adaptativa.
- Créditos, inventário de blocos e registro de eventos.

## ARC-AGI-3
A pasta `arc_agi3/` contém um smoke test do toolkit oficial em um jogo já suportado pelo SDK. Isso verifica instalação/imports e execução de ações discretas; não significa que NEON FRONTIER esteja registrado como ambiente customizado oficial. Referência: https://docs.arcprize.org/toolkit/overview

Instale com `python -m pip install -r requirements.txt` e execute `python arc_agi3/smoke_test.py`.
