# NEON FRONTIER — Build 1.0

Jogo independente de exploração urbana 2D, construído com HTML, CSS e JavaScript Canvas, sem bibliotecas externas.

## Executar no PC

**Modo mais simples:** abra `index.html` num navegador moderno (Chrome, Edge, Firefox ou Safari). O jogo roda sem instalação e sem conexão à internet; salvamento depende de o navegador permitir `localStorage` em arquivos locais.

**Modo recomendado (PWA/offline):** para instalar como aplicativo e permitir o cache offline, sirva a pasta com um servidor HTTP local. Com Python instalado, abra o terminal nesta pasta e execute:

```bash
python -m http.server 8000
```

Depois abra `http://localhost:8000`. No Chrome/Edge, use a opção de instalar o site como aplicativo quando estiver disponível. A primeira visita precisa carregar os arquivos; depois, o service worker mantém uma cópia em cache.

## Controles

- `W A S D` ou setas: mover
- `E`: conversar/interagir com habitantes próximos
- `B`: alternar modo construção; clique num terreno a até 4 blocos
- `F`: entrar/sair do veículo quando estiver perto
- `Q`: procurar/coletar recursos próximos
- `Esc`: pausar/retomar
- Celular/tablet: controles táteis na tela
- Gamepad: suporte experimental a direcional/eixos e botões comuns

## Sistemas incluídos

- Mapa procedural determinístico com ruas, edifícios, água, árvores e distritos
- Câmera que acompanha o jogador e redimensionamento adaptável
- Exploração e descobertas, créditos, materiais e energia
- Construção e remoção de blocos
- Veículo com movimento acelerado
- Habitantes com memória curta e confiança que evolui com interações
- Objetivo guiado, registro de eventos, salvamento automático e manual
- Interface adaptável, controles touch, suporte experimental a gamepad
- Manifest PWA e service worker para cache offline em HTTP/HTTPS

## Inspirações e propriedade intelectual

O jogo implementa sistemas originais inspirados em categorias gerais de jogabilidade — exploração urbana, construção/coleta e estética futurista. Não inclui código-fonte, mapas, personagens, marcas, modelos ou áudio extraídos de GTA V, Minecraft ou Cyberpunk 2077. Esses jogos não são projetos open source. Qualquer contribuição futura de terceiros deve ser revisada quanto à licença e receber os créditos exigidos.

## ARC-AGI-3

Esta build não afirma ser um ambiente ARC-AGI-3 oficial nem estar validada pelo toolkit. A jogabilidade de navegador e o toolkit ARC são componentes distintos; uma integração oficial exigiria um adaptador de ambiente e testes com o SDK suportado.
