# Histórias de Usuário (US)

## Visão Geral

Este documento contém todas as **15 Histórias de Usuário** com seus respectivos requisitos funcionais, organizadas por 6 épicos principais. Cada US possui até 5 requisitos detalhados para implementação.

---

## Épico 1: Experiência do Cliente (Landing Page)

### US01 – Interface de Navegação Visual

Como cliente, quero navegar por uma interface visualmente atraente e rápida no celular, para encontrar informações sem atritos.

Requisitos Funcionais:

- RQ01: O sistema deve possuir um menu de navegação fixo no rodapé
- RQ02: O sistema deve utilizar imagens em formatos otimizados (WebP) para garantir carregamento rápido
- RQ04: O sistema deve aplicar a identidade visual da marca em todos os elementos (Cores e Favicon)

---

### US02 – Nossa História e Blog de Novidades

Como cliente, quero ler sobre a origem da lanchonete e ver notícias recentes, para criar uma conexão emocional com a marca.

Requisitos Funcionais:

- RQ05: O sistema deve apresentar a seção "Sobre Nós" com texto institucional e fotos
- RQ06: O sistema deve listar notícias e promoções recentes em formato de feed (Blog)
- RQ07: O sistema deve permitir a expansão/recolhimento de Perguntas Frequentes (FAQ)
- RQ08: O sistema deve exibir depoimentos e feedbacks reais de outros clientes

---

### US03 – Localizador de Lojas e Horários

Como cliente, quero localizar a unidade mais próxima por região, para planejar minha visita ou pedido.

Requisitos Funcionais:

- RQ09: O sistema deve permitir filtrar lojas por bairro, cidade ou região
- RQ10: O sistema deve exibir o horário de funcionamento detalhado por unidade
- RQ11: O sistema deve indicar visualmente se a loja está "Aberta" ou "Fechada" em tempo real
- RQ12: O sistema deve fornecer um botão "Como Chegar" integrado ao Google Maps

---

### US04 – Visualização de Cardápio Interativo

Como cliente, quero ver o cardápio detalhado com filtros, para escolher o lanche ideal.

Requisitos Funcionais:

- RQ13: O sistema deve organizar o cardápio por categorias (Prensados, Bebidas, Combos)
- RQ14: O sistema deve oferecer um campo de busca por nome ou ingrediente do lanche
- RQ15: O sistema deve exibir selos informativos (Ex: "Mais Vendido", "Veggie", "Picante")
- RQ16: O sistema deve permitir abrir fotos ampliadas e descrições de alérgenos de cada item

---

## Épico 2: Operação de Vendas (Sistema de Pedido / PDV)

### US05 – Registro de Pedidos (Interface PDV)

Como caixa, quero registrar pedidos rapidamente através de uma interface tátil, para agilizar o atendimento.

Requisitos Funcionais:

- RQ17: O sistema deve fornecer uma grade de produtos com fotos para seleção rápida por toque
- RQ18: O sistema deve permitir a inserção de observações personalizadas por item (Ex: "Sem cebola")
- RQ19: O sistema deve calcular automaticamente o subtotal, taxas e o valor total do pedido
- RQ20: O sistema deve permitir selecionar múltiplos métodos de pagamento (Pix, Cartão, Dinheiro)

---


### US07 – Gestão de Cancelamentos e Erros

Como administrador, quero registrar justificativas para cancelamentos para entender falhas na operação.

Requisitos Funcionais:

- RQ25: O sistema deve exigir login de administrador para autorizar cancelamentos
- RQ26: O sistema deve obrigar a seleção de um motivo para cada pedido cancelado
- RQ27: O sistema deve registrar logs técnicos de mensagens de erro ocorridas durante a venda
- RQ28: O sistema deve gerar um relatório mensal de "Perdas por Cancelamento"

---

## Épico 3: Gestão de Insumos e Retenção

### US08 – Sistema de Fidelidade por Telefone

Como cliente, quero acumular pontos pelo meu número de telefone para trocar por benefícios.

Requisitos Funcionais:

- RQ29: O sistema deve permitir o cadastro/identificação de clientes via número de telefone no checkout
- RQ30: O sistema deve calcular e acumular pontos automaticamente com base no valor da compra
- RQ31: O sistema deve exibir o saldo de pontos disponível para resgate na tela do caixa
- RQ32: O sistema deve permitir a aplicação de prêmios (Ex: Lanche grátis) via pontuação
- RQ33: O sistema deve registrar uma data de validade para os pontos acumulados (Ex: 90 dias)

---

## Épico 4: Business Intelligence (Dashboard BI)

### US09 – BI: Dashboard Financeiro e Lucratividade

Como administrador, quero ver o lucro real para avaliar a saúde financeira do negócio.

Requisitos Funcionais:

- RQ34: O sistema deve exibir gráficos de faturamento bruto diário, semanal e mensal
- RQ35: O sistema deve calcular o lucro líquido (Vendas - Custo de Insumos)
- RQ36: O sistema deve exibir o Ticket Médio por cliente em tempo real
- RQ37: O sistema deve mostrar a margem de lucro percentual de cada item vendido

---

### US10 – BI: Performance de Produtos e Insight de Vendas

Como administrador, quero saber quais lanches vendem mais para otimizar o menu e acompanhar o desempenho ao final de cada dia.

Requisitos Funcionais:

- RQ38: O sistema deve gerar um ranking (Top 10) de produtos mais vendidos
- RQ39: O sistema deve exibir um dashboard com os produtos mais vendidos no final do dia
- RQ40: O sistema deve identificar o "Produto Mais Lucrativo" (maior margem, não só venda)
- RQ41: O sistema deve exibir um gráfico de pizza com a distribuição de vendas por categoria
- RQ42: O sistema deve permitir filtrar o desempenho de produtos por unidade/loja específica

---

### US11 – BI: Análise de Fluxo e Sazonalidade

Como administrador, quero saber os horários de pico para organizar a escala da equipe.

Requisitos Funcionais:

- RQ43: O sistema deve exibir um gráfico de barras com o volume de vendas por hora
- RQ44: O sistema deve identificar os "Dias da Semana Mais Movimentados"
- RQ45: O sistema deve permitir a comparação de desempenho entre diferentes períodos (Filtro de Tempo)

---

## Épico 5: Administração e Segurança (CMS)

### US12 – Gestão de Acessos e Segurança

Como administrador, quero controlar o nível de acesso dos colaboradores para garantir a integridade dos dados e evitar fraudes.

Requisitos Funcionais:

- RQ46: O sistema deve exigir autenticação com senha criptografada para acesso administrativo
- RQ47: O sistema deve separar permissões entre perfis de "Caixa" e "Administrador"
- RQ48: O sistema deve registrar logs de auditoria (quem alterou preços ou deletou pedidos)

---

### US13 – Gestão de Cardápio (Cadastro e Remoção de Itens)

Como administrador, quero gerenciar o catálogo de produtos na área logada para manter o cardápio atualizado e controlar ofertas sazonais.

Requisitos Funcionais:

- RQ49: O sistema deve permitir criar/editar produtos, preços e fotos via painel administrativo
- RQ50: O sistema deve permitir remover itens do cardápio com confirmação obrigatória
- RQ51: O sistema deve permitir a alteração de banners da página inicial para campanhas
- RQ52: O sistema deve permitir o reajuste de preços em massa (por porcentagem)
- RQ53: O sistema deve exibir a data da última atualização de cada item do cardápio

---

### US14 – Controle de Vendas com Dashboard

Como caixa/administrador, quero acompanhar o desempenho do dia em tempo real através de um dashboard para gerenciar operações.

Requisitos Funcionais:

- RQ54: O sistema deve exibir um dashboard com resumo de vendas do dia (quantidade de pedidos, total faturado)
- RQ55: O sistema deve listar os produtos mais vendidos no período atual
- RQ56: O sistema deve mostrar o ticket médio de vendas do dia
- RQ57: O sistema deve permitir filtrar por período (hora, turno ou período personalizado)

---

### US15 – Relatórios e Exportação

Como administrador, quero extrair dados consolidados para facilitar a contabilidade e o acompanhamento financeiro do negócio.

Requisitos Funcionais:

- RQ58: O sistema deve permitir exportar relatórios financeiros (vendas, custos e lucro) nos formatos PDF e Excel
- RQ59: O sistema deve enviar um resumo do faturamento diário automaticamente por e-mail ao proprietário após o fechamento do caixa
- RQ60: O sistema deve permitir a seleção de períodos personalizados (data inicial e final) para a geração dos relatórios

---

## Épico 6: Análise de Vendas

### US16 – Insight de Produtos Mais Vendidos por Dia

Como gerente, quero visualizar um relatório consolidado dos produtos mais vendidos ao final de cada dia para identificar tendências e oportunidades de venda.

Requisitos Funcionais:

- RQ61: O sistema deve consolidar ao final do dia os Top 5 produtos mais vendidos
- RQ62: O sistema deve exibir a quantidade vendida e a receita gerada por cada produto
- RQ63: O sistema deve permitir comparar o desempenho de hoje com o dia anterior
- RQ64: O sistema deve gerar alertas para produtos com baixa venda

---

## Controle de Versao

| Versao | Data | Autor(es) | Alteracoes |
|---|---|---|---|
| 1.0 | 2026-03-27 | Daniel Ferreira Nunes | Criacao inicial do documento com 15 historias de usuario e 56 requisitos funcionais |
| 2.0 | 2026-03-29 | Daniel Ferreira Nunes | Remocao de US08 (Controle de Estoque), ajuste de Fidelidade por telefone com validade, expansao de Gestao de Cardapio, adicao de Dashboard de Vendas e Insight de Produtos Mais Vendidos, totalizando 16 US com 64 requisitos funcionais |
| 3.0 | 2026-03-29 | Daniel Ferreira Nunes | Remocao de US06 (Fluxo e Status de Preparo), mantendo apenas cancelamento de pedidos, totalizando 15 US com 60 requisitos funcionais |

---

