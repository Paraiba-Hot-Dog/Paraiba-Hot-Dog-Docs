# Backlog do Produto

> Este documento registra as **14 histórias de usuário** e seus **100 requisitos funcionais** do ecossistema **Paraíba Hot Dog** (frontend + backend).
>
> Os requisitos são numerados sequencialmente de **RQ01** a **RQ100**, na ordem em que aparecem neste documento.

## Resumo por épico

| Épico | US | Requisitos | Concluídos |
|-------|----|------------|------------|
| 1 — Experiência do Cliente | US01–US05 | RQ01–RQ24 | 24 / 24 |
| 2 — Operação de Vendas | US06–US07 | RQ25–RQ38 | 14 / 14 |
| 3 — Fidelidade | US08 | RQ39–RQ46 | 8 / 8 |
| 4 — Business Intelligence | US09 | RQ47–RQ66 | 20 / 20 |
| 5 — Administração | US10–US13 | RQ67–RQ94 | 28 / 28 |
| 6 — Cozinha | US14 | RQ95–RQ100 | 6 / 6 |
| **Total** | **14 US** | **RQ01–RQ100** | **100 / 100** |

---

## Épico 1: Experiência do Cliente

### US01 – Interface de Navegação Visual

Como cliente, quero navegar por uma interface visualmente atraente e rápida, para encontrar informações sem atritos.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ01** | Menu hambúrguer no cabeçalho e links estruturados no rodapé | ✅ |
| **RQ02** | Suporte a imagens otimizadas (WebP, JPEG e PNG) no cardápio e uploads | ✅ |
| **RQ03** | Identidade visual da marca (cores e favicon) | ✅ |
| **RQ04** | Ícones flutuantes de redes sociais (iFood e Instagram) na home e rodapé | ✅ |
| **RQ05** | Atalho para pedido no iFood na página inicial | ✅ |
| **RQ06** | Listagem de unidades na home com link para a página da loja | ✅ |
| **RQ07** | Carrosséis de produtos em destaque na home | ✅ |
| **RQ08** | Acesso à área administrativa a partir do menu público | ✅ |

### US02 – Nossa História e Blog de Novidades

Como cliente, quero ler sobre a origem da lanchonete e ver notícias recentes, para criar conexão com a marca.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ09** | Seção "Sobre Nós" com texto institucional e fotos | ✅ |
| **RQ10** | Feed de notícias e promoções integrado à API do blog | ✅ |
| **RQ11** | FAQ expansível/recolhível | ✅ |
| **RQ12** | Exibição de depoimentos de clientes em carrossel | ✅ |
| **RQ13** | Gestão administrativa de publicações do blog (CRUD com imagem) | ✅ |

### US03 – Localizador de Lojas e Horários

Como cliente, quero localizar a unidade mais próxima por região, para planejar minha visita ou pedido.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ14** | Horário de funcionamento detalhado por unidade | ✅ |
| **RQ15** | Indicação visual "Aberta" ou "Fechada" com base no horário da unidade | ✅ |
| **RQ16** | Horário de abertura e fechamento configurável por unidade no painel admin | ✅ |
| **RQ17** | Botão "Como Chegar" integrado ao Google Maps | ✅ |

### US04 – Visualização de Cardápio Interativo

Como cliente, quero ver o cardápio detalhado com filtros, para escolher o lanche ideal.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ18** | Produtos com nome, composição e preço em destaque | ✅ |
| **RQ19** | Navegação entre categorias por abas ou scroll lateral | ✅ |
| **RQ20** | Fotos dos produtos no cardápio | ✅ |
| **RQ21** | Filtro de cardápio por unidade selecionada | ✅ |

### US05 – Localização Inteligente via Mapa

Como cliente, quero visualizar as unidades em um mapa interativo, para identificar a loja mais próxima.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ22** | Horário e status de funcionamento na página da unidade | ✅ |
| **RQ23** | Mapa interativo com zoom e arrastar | ✅ |
| **RQ24** | Link "Abrir no Maps" para navegação externa | ✅ |

---

## Épico 2: Operação de Vendas

### US06 – Registro de Pedidos

Como caixa, quero registrar pedidos rapidamente através de uma interface tátil, para agilizar o atendimento.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ25** | Grade de produtos com fotos para seleção por toque | ✅ |
| **RQ26** | Observações personalizadas por item | ✅ |
| **RQ27** | Cálculo automático de subtotal, desconto fidelidade e total do pedido | ✅ |
| **RQ28** | Múltiplos métodos de pagamento (Pix, Cartão, Dinheiro) | ✅ |
| **RQ29** | Identificação do pedido por nome de comanda | ✅ |
| **RQ30** | Manter pedido aberto e complementar itens antes do pagamento | ✅ |
| **RQ31** | Painel de pedidos abertos com atualização automática | ✅ |
| **RQ32** | Montagem de combos com escolha de bebida | ✅ |
| **RQ33** | Seleção da unidade de origem do pedido | ✅ |
| **RQ34** | Cadastro de novo cliente durante a venda | ✅ |

### US07 – Gestão de Cancelamentos e Erros

Como administrador, quero registrar justificativas para cancelamentos para entender falhas na operação.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ35** | Cancelamentos restritos a usuários autenticados na área administrativa | ✅ |
| **RQ36** | Registro de motivo em cancelamentos na cozinha e no PDV | ✅ |
| **RQ37** | Feedback de erros e confirmações nas operações de venda | ✅ |
| **RQ38** | Consulta de pedidos cancelados com motivo na tela de cozinha | ✅ |

---

## Épico 3: Retenção e Fidelidade

### US08 – Sistema de Fidelidade por Telefone

Como cliente, quero acumular pontos pelo meu número de telefone para trocar por benefícios.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ39** | Cadastro e identificação por telefone no PDV | ✅ |
| **RQ40** | Acúmulo automático de pontos pela compra | ✅ |
| **RQ41** | Exibição do saldo de pontos | ✅ |
| **RQ42** | Exibição do progresso para o próximo prêmio no cartão fidelidade | ✅ |
| **RQ43** | Publicação de promoções via módulo de blog | ✅ |
| **RQ44** | Comunicação automatizada com cliente via WhatsApp no cadastro | ✅ |
| **RQ45** | Resgate de benefício por pontos no fechamento do pedido | ✅ |
| **RQ46** | Mensagem de boas-vindas via WhatsApp ao cadastrar cliente | ✅ |

---

## Épico 4: Business Intelligence

### US09 – Dashboard de BI e Relatórios

Como administrador, quero visualizar métricas de vendas e lucratividade para tomar decisões baseadas em dados.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ47** | Indicadores de faturamento bruto com filtro por ano e mês | ✅ |
| **RQ48** | Lucro líquido (vendas − custos) | ✅ |
| **RQ49** | Ticket médio atualizado conforme vendas do período | ✅ |
| **RQ50** | Margem de lucro do produto em destaque | ✅ |
| **RQ51** | Ranking Top 10 de produtos mais vendidos | ✅ |
| **RQ52** | Ranking de produtos mais vendidos no período selecionado | ✅ |
| **RQ53** | Identificação do produto mais lucrativo | ✅ |
| **RQ54** | Gráfico de distribuição de vendas por categoria (mix de produtos) | ✅ |
| **RQ55** | Dashboard consolidado de indicadores por período | ✅ |
| **RQ56** | Gráfico de barras de vendas por hora | ✅ |
| **RQ57** | Identificação de picos de venda por horário no gráfico | ✅ |
| **RQ58** | Comparação percentual de desempenho em relação ao mês anterior | ✅ |
| **RQ59** | Listagem dos produtos com maior volume no período | ✅ |
| **RQ60** | Quantidade vendida e receita por produto no ranking | ✅ |
| **RQ61** | Variação dos KPIs em relação ao período anterior | ✅ |
| **RQ62** | Ranking de produtos para análise de volume de vendas | ✅ |
| **RQ63** | Painel resumo com KPIs de vendas do período filtrado | ✅ |
| **RQ64** | Lista dos mais vendidos conforme período visualizado | ✅ |
| **RQ65** | Ticket médio exibido conforme período selecionado | ✅ |
| **RQ66** | Filtros de período por ano, mês e fechamento mensal | ✅ |

---

## Épico 5: Administração e Segurança

### US10 – Gestão de Acessos e Segurança

Como administrador, quero controlar o nível de acesso dos colaboradores para garantir a integridade dos dados.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ67** | Autenticação com senha para área administrativa (Keycloak) | ✅ |
| **RQ68** | Cadastro de perfis de acesso (administrador, caixa, cozinha) | ✅ |
| **RQ69** | Gestão de permissões por função na administração de usuários | ✅ |
| **RQ70** | Validação de sessão por token na área administrativa | ✅ |
| **RQ71** | Recuperação de senha por e-mail com link temporário | ✅ |
| **RQ72** | Redefinição de senha com token de uso único | ✅ |
| **RQ73** | Painel administrativo central com atalhos às áreas | ✅ |
| **RQ74** | Gestão de colaboradores (criar, editar, excluir) | ✅ |
| **RQ75** | API de permissões por área do sistema | ✅ |

### US11 – Gestão de Cardápio

Como administrador, quero gerenciar o catálogo de produtos para manter o cardápio atualizado.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ76** | Criar produtos, preços e fotos | ✅ |
| **RQ77** | Editar produtos, preços e fotos | ✅ |
| **RQ78** | Remover itens com confirmação obrigatória | ✅ |
| **RQ79** | Conteúdo visual da home com carrosséis de produtos em destaque | ✅ |
| **RQ80** | Edição de preços por variação de produto | ✅ |
| **RQ81** | Feedback visual de alterações ao administrador (confirmações e toasts) | ✅ |
| **RQ82** | Organização do cardápio em categorias e subcategorias | ✅ |
| **RQ83** | Variações de produto (tamanhos, combos) com preços distintos | ✅ |
| **RQ84** | Cadastro de adicionais opcionais vinculados aos produtos | ✅ |
| **RQ85** | Ativar/desativar produto sem excluir do catálogo | ✅ |

### US12 – Relatórios e Exportação

Como administrador, quero extrair dados consolidados em formato PDF, para facilitar a conferência contábil.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ86** | Exportação do dashboard em PDF pelo painel BI | ✅ |
| **RQ87** | Geração de relatório conforme ano e mês selecionados | ✅ |
| **RQ88** | Envio de e-mails transacionais (recuperação de senha) | ✅ |
| **RQ89** | Exportação de KPIs e ranking de produtos no PDF do dashboard | ✅ |

### US13 – Gestão Administrativa de Unidades

Como administrador, quero gerenciar as localizações no mapa para manter os pontos de venda atualizados.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ90** | Cadastro de unidades com endereço completo e link do Google Maps | ✅ |
| **RQ91** | Editar horários de funcionamento por unidade | ✅ |
| **RQ92** | Dados de localização disponíveis via API para o front | ✅ |
| **RQ93** | Exclusão de unidades pelo painel administrativo | ✅ |
| **RQ94** | Imagem representativa da unidade no cadastro | ✅ |

---

## Épico 6: Operação de Cozinha

### US14 – Gestão de Fila de Produção

Como cozinheiro, quero visualizar os pedidos em uma tela organizada por status e ordem de chegada.

| ID | Requisito | Status |
| :--- | :--- | :---: |
| **RQ95** | Cards com itens, observações e horário do pedido | ✅ |
| **RQ96** | Semaforização visual por status (fila, preparando, entregue, cancelado) | ✅ |
| **RQ97** | Baixa de pedido por toque (preparar / entregar) | ✅ |
| **RQ98** | Consulta de pedidos entregues e cancelados | ✅ |
| **RQ99** | Busca na cozinha por comanda ou item | ✅ |
| **RQ100** | Abas separadas para fila, entregues e cancelados | ✅ |
