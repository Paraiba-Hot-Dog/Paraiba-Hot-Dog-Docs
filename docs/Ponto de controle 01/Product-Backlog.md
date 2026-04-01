# Histórias de Usuário (US)

## Visão Geral

Este documento contém as **15 Histórias de Usuário** com seus respectivos requisitos funcionais, organizadas por 7 épicos principais.

---

## Épico 1: Experiência do Cliente (Landing Page)

### US01 – Interface de Navegação Visual

Como cliente, quero navegar por uma interface visualmente atraente e rápida, para encontrar informações sem atritos.

Requisitos Funcionais:

- RQ01: O sistema deve possuir um menu de navegação fixo no rodapé
- RQ02: O sistema deve utilizar imagens em formatos otimizados (WebP) para garantir carregamento rápido
- RQ03: O sistema deve aplicar a identidade visual da marca em todos os elementos (Cores e Favicon)

---

### US02 – Nossa História e Blog de Novidades

Como cliente, quero ler sobre a origem da lanchonete e ver notícias recentes, para criar uma conexão emocional com a marca.

Requisitos Funcionais:

- RQ04: O sistema deve apresentar a seção "Sobre Nós" com texto institucional e fotos
- RQ05: O sistema deve listar notícias e promoções recentes em formato de feed (Blog)
- RQ06: O sistema deve permitir a expansão/recolhimento de Perguntas Frequentes (FAQ)
- RQ07: O sistema deve exibir depoimentos e feedbacks reais de outros clientes

---

### US03 – Localizador de Lojas e Horários

Como cliente, quero localizar a unidade mais próxima por região, para planejar minha visita ou pedido.

Requisitos Funcionais:

- RQ08: O sistema deve permitir filtrar lojas por bairro, cidade ou região
- RQ09: O sistema deve exibir o horário de funcionamento detalhado por unidade
- RQ10: O sistema deve indicar visualmente se a loja está "Aberta" ou "Fechada" em tempo real
- RQ11: O sistema deve fornecer um botão "Como Chegar" integrado ao Google Maps

---

### US04 – Visualização de Cardápio Interativo

Como cliente, quero ver o cardápio detalhado com filtros, para escolher o lanche ideal.

Requisitos Funcionais:

- RQ12: O sistema deve organizar o cardápio por categorias (Prensados, Bebidas, Combos)
- RQ13: O sistema deve exibir selos informativos (Ex: "Mais Vendido", "Veggie", "Picante")
- RQ14: O sistema deve permitir abrir fotos ampliadas e descrições de alérgenos de cada item


---

## Épico 2: Operação de Vendas

### US05 – Registro de Pedidos

Como caixa, quero registrar pedidos rapidamente através de uma interface tátil, para agilizar o atendimento.

Requisitos Funcionais:

- RQ15: O sistema deve fornecer uma grade de produtos com fotos para seleção rápida por toque
- RQ16: O sistema deve permitir a inserção de observações personalizadas por item
- RQ17: O sistema deve calcular automaticamente o subtotal, taxas e o valor total do pedido
- RQ18: O sistema deve permitir selecionar múltiplos métodos de pagamento (Pix, Cartão, Dinheiro)

---


### US06 – Gestão de Cancelamentos e Erros

Como administrador, quero registrar justificativas para cancelamentos para entender falhas na operação.

Requisitos Funcionais:

- RQ19: O sistema deve exigir login de administrador para autorizar cancelamentos
- RQ20: O sistema deve obrigar a seleção de um motivo para cada pedido cancelado
- RQ21: O sistema deve registrar logs técnicos de mensagens de erro ocorridas durante a venda
- RQ22: O sistema deve gerar um relatório mensal de "Perdas por Cancelamento"

---

## Épico 3: Gestão de Insumos e Retenção

### US07 – Sistema de Fidelidade por Telefone

Como cliente, quero acumular pontos pelo meu número de telefone para trocar por benefícios.

Requisitos Funcionais:

- RQ23: O sistema deve permitir o cadastro/identificação de clientes via número de telefone no checkout
- RQ24: O sistema deve calcular e acumular pontos automaticamente com base no valor da compra
- RQ25: O sistema deve exibir o saldo de pontos disponível para resgate na tela do caixa
- RQ26: O sistema deve permitir a aplicação de prêmios via pontuação
- RQ27: O sistema deve registrar uma data de validade para os pontos acumulados
- RQ28: O sistema deve permitir criar campanhas de promoção com título, descrição e mídia
- RQ29: O sistema deve agendar o envio automático para data e horário específicos
- RQ30: O sistema deve segmentar clientes por tipo (VIP, novo, frequente, inativo)
- RQ31: O sistema deve enviar notificações via WhatsApp e/ou Push notification
- RQ32: O sistema deve rastrear taxa de entrega, abertura e cliques nas campanhas

---

## Épico 4: Business Intelligence (Dashboard)

### US08 – BI: Dashboard Financeiro e Lucratividade

Como administrador, quero ver o lucro real para avaliar a saúde financeira do negócio.

Requisitos Funcionais:

- RQ33: O sistema deve exibir gráficos de faturamento bruto diário, semanal e mensal
- RQ34: O sistema deve calcular o lucro líquido (Vendas - Custo de Insumos)
- RQ35: O sistema deve exibir o Ticket Médio por cliente em tempo real
- RQ36: O sistema deve mostrar a margem de lucro percentual de cada item vendido
- RQ37: O sistema deve gerar um ranking (Top 10) de produtos mais vendidos
- RQ38: O sistema deve exibir um dashboard com os produtos mais vendidos no final do dia
- RQ39: O sistema deve identificar o "Produto Mais Lucrativo" (maior margem, não só venda)
- RQ40: O sistema deve exibir um gráfico de pizza com a distribuição de vendas por categoria
- RQ41: O sistema deve permitir filtrar o desempenho de produtos por unidade/loja específica
- RQ42: O sistema deve exibir um gráfico de barras com o volume de vendas por hora
- RQ43: O sistema deve identificar os "Dias da Semana Mais Movimentados"
- RQ44: O sistema deve permitir a comparação de desempenho entre diferentes períodos (Filtro de Tempo)
- RQ45: O sistema deve consolidar ao final do dia os Top 5 produtos mais vendidos
- RQ46: O sistema deve exibir a quantidade vendida e a receita gerada por cada produto
- RQ47: O sistema deve permitir comparar o desempenho de hoje com o dia anterior
- RQ48: O sistema deve gerar alertas para produtos com baixa venda
- RQ49: O sistema deve exibir um dashboard com resumo de vendas do dia (quantidade de pedidos, total faturado)
- RQ50: O sistema deve listar os produtos mais vendidos no período atual
- RQ51: O sistema deve mostrar o ticket médio de vendas do dia
- RQ52: O sistema deve permitir filtrar por período (hora, turno ou período personalizado)

---

## Épico 5: Administração e Segurança

### US09 – Gestão de Acessos e Segurança

Como administrador, quero controlar o nível de acesso dos colaboradores para garantir a integridade dos dados e evitar fraudes.

Requisitos Funcionais:

- RQ53: O sistema deve exigir autenticação com senha criptografada para acesso administrativo
- RQ54: O sistema deve separar permissões entre perfis de "Caixa" e "Administrador" e "cozinheiro"
- RQ55: O sistema deve registrar logs de auditoria (quem alterou preços ou deletou pedidos)

---

### US10 – Gestão de Cardápio

Como administrador, quero gerenciar o catálogo de produtos na área logada para manter o cardápio atualizado e controlar ofertas sazonais.

Requisitos Funcionais:

- RQ56: O sistema deve permitir criar/editar produtos, preços e fotos via painel administrativo
- RQ57: O sistema deve permitir remover itens do cardápio com confirmação obrigatória
- RQ58: O sistema deve permitir a alteração de banners da página inicial para campanhas
- RQ59: O sistema deve permitir o reajuste de preços em massa (por porcentagem)
- RQ60: O sistema deve exibir a data da última atualização de cada item do cardápio

---

### US11 – Relatórios e Exportação

Como administrador, quero extrair dados consolidados em formato PDF, para facilitar a conferência contábil e o acompanhamento histórico do negócio.

Requisitos Funcionais:

- RQ61: O sistema deve permitir a exportação de relatórios financeiros (faturamento, custos e lucro) exclusivamente no formato PDF, garantindo a integridade visual dos dados para impressão ou arquivamento
- RQ62: O sistema deve permitir a geração de relatórios baseada em datas personalizadas (filtro de data inicial e final), permitindo análises mensais, quinzenais ou anuais
- RQ63: O sistema deve enviar um resumo do faturamento diário automaticamente para o e-mail cadastrado do proprietário assim que o fechamento do caixa for concluído
- RQ64: O relatório gerado deve destacar claramente a margem de lucro por categoria de produto, facilitando a identificação de itens que trazem maior retorno financeiro

---

## Épico 6: Operação de Cozinha

### US12 – Gestão de Fila de Produção (Tela da Cozinha)

Como chapeiro/cozinheiro, quero visualizar os pedidos em uma tela organizada por tempo de espera, para que eu possa priorizar a produção e evitar atrasos.

Requisitos Funcionais:

- RQ65: O sistema deve exibir os pedidos em "cards" contendo itens, observações e tempo decorrido desde o pagamento
- RQ66: O sistema deve mudar a cor do card (Verde > Amarelo > Vermelho) conforme o tempo de preparo ultrapassa o limite estipulado
- RQ67: O sistema deve permitir dar "baixa" no item ou no pedido completo via toque na tela ou atalho

---

### US13 – Interface Exclusiva da Cozinha (Login e Permissões)

Como cozinheiro, quero acessar uma interface restrita e simplificada, para visualizar apenas os dados necessários para a preparação do lanche, sem acesso a informações financeiras ou administrativas.

Requisitos Funcionais:

- RQ68: O sistema deve possuir um nível de acesso específico para "Cozinha", que oculte faturamento, relatórios e dados sensíveis de clientes
- RQ69: A interface do cozinheiro deve exibir apenas a composição do lanche, observações (Ex: "sem cebola") e o número do pedido
- RQ70: O sistema deve impedir que o perfil de cozinheiro realize cancelamentos ou alteração de preços no cardápio

---

### US14 – Painel de Chamada de Pedidos (Visualizador do Cliente)

Como cliente na loja, quero visualizar o status do meu pedido em um monitor, para saber o momento exato de ir ao balcão retirá-lo.

Requisitos Funcionais:

- RQ71: O sistema deve exibir uma interface de "Pronto" e "Em Preparo" otimizada para Smart TVs
- RQ72: O sistema deve emitir um alerta sonoro padrão quando um pedido for movido para o status "Pronto"
- RQ73: O sistema deve remover automaticamente o nome/número da lista de "Pronto" após um tempo configurável (Ex: 5 minutos)

---

## Épico 7: Manutenção e Expansão (Multilojas)

### US15 – Controle de Turno e Fechamento de Caixa

Como operador de caixa, quero realizar a conferência de valores ao final do dia, para garantir que o dinheiro físico bate com as vendas registradas.

Requisitos Funcionais:

- RQ74: O sistema deve gerar um relatório de fechamento de turno mostrando a diferença entre o valor esperado e o valor informado

---

## Controle de Versao

| Versao | Data | Autor(es) | Alteracoes |
|---|---|---|---|
| 1.0 | 2026-03-27 | Daniel Ferreira Nunes | Criacao inicial do documento com 15 historias de usuario e 56 requisitos funcionais |
| 2.0 | 2026-03-29 | Daniel Ferreira Nunes | Remocao de US08 (Controle de Estoque), ajuste de Fidelidade por telefone com validade, expansao de Gestao de Cardapio, adicao de Dashboard de Vendas e Insight de Produtos Mais Vendidos, totalizando 16 US com 64 requisitos funcionais |
| 3.0 | 2026-03-29 | Daniel Ferreira Nunes | Remocao de US06 (Fluxo e Status de Preparo), mantendo apenas cancelamento de pedidos, totalizando 15 US com 60 requisitos funcionais |
| 4.0 | 2026-03-29 | Daniel Ferreira Nunes | Adicao de US17 - Alertas de Promocao por Push/WhatsApp para engajamento e marketing, totalizando 16 US com 65 requisitos funcionais |
| 5.0 | 2026-03-29 | Samuel Ribeiro | Ajuste de sequencia de US e RQ e revisao do documento |
| 6.0 | 2026-03-31 | Daniel Ferreira Nunes | Correção dos erros apontados pelo professor e adição de novas US |

---

