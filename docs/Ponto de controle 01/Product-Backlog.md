# Histórias de Usuário (US's)

> Este documento contém as **15 Histórias de Usuário** com seus respectivos requisitos funcionais, organizadas por 6 épicos principais.

---

## Épico 1: Experiência do Cliente (Landing Page)

### US01 – Interface de Navegação Visual
Como cliente, quero navegar por uma interface visualmente atraente e rápida, para encontrar informações sem atritos.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ01** | O sistema deve possuir um menu hambúrguer no cabeçalho e links de navegação estruturados no rodapé. |
| **RQ02** | O sistema deve utilizar imagens em formatos otimizados (WebP) para garantir carregamento rápido. |
| **RQ03** | O sistema deve aplicar a identidade visual da marca em todos os elementos (Cores e Favicon). |
| **RQ04** | O sistema deve exibir ícones flutuantes de contato e acesso rápido a redes sociais (WhatsApp/Instagram/iFood). |

### US02 – Nossa História e Blog de Novidades
Como cliente, quero ler sobre a origem da lanchonete e ver notícias recentes, para criar uma conexão emocional com a marca.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ05** | O sistema deve apresentar a seção "Sobre Nós" com texto institucional e fotos. |
| **RQ06** | O sistema deve listar notícias e promoções recentes em formato de feed (Blog). |
| **RQ07** | O sistema deve permitir a expansão/recolhimento de Perguntas Frequentes (FAQ). |
| **RQ08** | O sistema deve exibir depoimentos e feedbacks reais de outros clientes. |

### US03 – Localizador de Lojas e Horários
Como cliente, quero localizar a unidade mais próxima por região, para planejar minha visita ou pedido.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ10** | O sistema deve exibir o horário de funcionamento detalhado por unidade. |
| **RQ11** | O sistema deve indicar visualmente se a loja está "Aberta" ou "Fechada" em tempo real. |
| **RQ12** | O sistema deve permitir que o administrador sobreponha o horário padrão para datas festivas. |
| **RQ13** | O sistema deve fornecer um botão "Como Chegar" integrado ao Google Maps. |

### US04 – Visualização de Cardápio Interativo
Como cliente, quero ver o cardápio detalhado com filtros, para escolher o lanche ideal.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ14** | O sistema deve listar os produtos com nome, composição detalhada dos ingredientes e preço em destaque. |
| **RQ15** | O sistema deve permitir a navegação entre categorias (Ex: Prensados, Bebidas, Combos) através de um menu de abas ou scroll lateral. |
| **RQ16** | O sistema deve exibir fotos reais dos produtos ao lado da descrição para facilitar a identificação visual. |


### US05 – Localização Inteligente via Mapa
Como cliente, quero visualizar as unidades em um mapa interativo, para identificar a loja mais próxima da minha localização atual.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ18** | O sistema deve exibir o horário de funcionamento e o status atual (Ex: Aberto agora) diretamente no card da unidade. |
| **RQ19** | O sistema deve integrar um mapa interativo que permite o uso de gestos (zoom e arrastar) para explorar as localizações. |
| **RQ20** | O sistema deve fornecer um link direto ("Open in Maps") que redireciona o usuário para o aplicativo de navegação externo. |

---

## Épico 2: Operação de Vendas

### US06 – Registro de Pedidos
Como caixa, quero registrar pedidos rapidamente através de uma interface tátil, para agilizar o atendimento.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ21** | O sistema deve fornecer uma grade de produtos com fotos para seleção rápida por toque. |
| **RQ22** | O sistema deve permitir a inserção de observações personalizadas por item. |
| **RQ23** | O sistema deve calcular automaticamente o subtotal, taxas, descontos e o valor total do pedido. |
| **RQ24** | O sistema deve permitir selecionar múltiplos métodos de pagamento (Pix, Cartão, Dinheiro). |

### US07 – Gestão de Cancelamentos e Erros
Como administrador, quero registrar justificativas para cancelamentos para entender falhas na operação.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ25** | O sistema deve exigir permissão de administrador e/ou caixa para autorizar cancelamentos. |
| **RQ26** | O sistema deve obrigar a seleção de um motivo para cada pedido cancelado. |
| **RQ27** | O sistema deve registrar logs técnicos de mensagens de erro ocorridas durante a venda. |
| **RQ28** | O sistema deve gerar um relatório mensal de "Perdas por Cancelamento". |

---

## Épico 3: Gestão de Insumos e Retenção

### US08 – Sistema de Fidelidade por Telefone
Como cliente, quero acumular pontos pelo meu número de telefone para trocar por benefícios.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ29** | O sistema deve permitir o cadastro/identificação de clientes via número de telefone no checkin/checkout. |
| **RQ30** | O sistema deve calcular e acumular ponto(s) automaticamente com base no valor da compra. |
| **RQ31** | O sistema deve exibir o saldo de ponto(s) disponível(eis) para resgate. |
| **RQ33** | O sistema deve registrar uma data de validade para os pontos acumulados. |
| **RQ34** | O sistema deve permitir criar campanhas de promoção com título, descrição e mídia. |
| **RQ37** | O sistema deve enviar notificações via WhatsApp e/ou Push notification. |

---

## Épico 4: Business Intelligence (Dashboard)

### US09 – Dashboard de Business Intelligence e Relatórios
Como administrador, quero visualizar métricas detalhadas de vendas e lucratividade, para tomar decisões estratégicas baseadas em dados.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ39** | O sistema deve exibir gráficos de faturamento bruto diário, semanal e mensal. |
| **RQ40** | O sistema deve calcular o lucro líquido ($Vendas - Custos$). |
| **RQ41** | O sistema deve exibir o Ticket Médio por cliente em tempo real. |
| **RQ42** | O sistema deve mostrar a margem de lucro percentual de cada item vendido. |
| **RQ43** | O sistema deve gerar um ranking (Top 10) de produtos mais vendidos. |
| **RQ44** | O sistema deve exibir um dashboard com os produtos mais vendidos no final do dia. |
| **RQ45** | O sistema deve identificar o "Produto Mais Lucrativo" (maior margem). |
| **RQ46** | O sistema deve exibir um gráfico de pizza com a distribuição de vendas por categoria. |
| **RQ47** | O sistema deve permitir filtrar o desempenho de produtos por unidade/loja específica. |
| **RQ48** | O sistema deve exibir um gráfico de barras com o volume de vendas por hora. |
| **RQ49** | O sistema deve identificar os "Dias da Semana Mais Movimentados". |
| **RQ50** | O sistema deve permitir a comparação de desempenho entre diferentes períodos. |
| **RQ51** | O sistema deve consolidar ao final do dia os Top 5 produtos mais vendidos. |
| **RQ52** | O sistema deve exibir a quantidade vendida e a receita gerada por cada produto. |
| **RQ53** | O sistema deve permitir comparar o desempenho de hoje com o dia anterior. |
| **RQ54** | O sistema deve gerar alertas para produtos com baixa venda (itens parados). |
| **RQ55** | O sistema deve exibir um dashboard com resumo de vendas do dia. |
| **RQ56** | O sistema deve listar os produtos mais vendidos no período atual de visualização. |
| **RQ57** | O sistema deve mostrar o ticket médio de vendas especificamente do dia atual. |
| **RQ58** | O sistema deve permitir filtrar dados por período (hora, turno ou personalizado). |

---

## Épico 5: Administração e Segurança

### US10 – Gestão de Acessos e Segurança
Como administrador, quero controlar o nível de acesso dos colaboradores para garantir a integridade dos dados.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ59** | O sistema deve exigir autenticação com senha criptografada para acesso administrativo. |
| **RQ60** | O sistema deve separar permissões entre perfis de "Caixa" e "Administrador". |
| **RQ61** | O sistema deve registrar logs de auditoria (quem alterou preços ou deletou pedidos). |
| **RQ62** | O sistema deve realizar o logoff automático após "X" minutos de inatividade na área administrativa. |

### US11 – Gestão de Cardápio
Como administrador, quero gerenciar o catálogo de produtos para manter o cardápio atualizado.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ63** | O sistema deve permitir criar produtos, preços e fotos via painel administrativo. |
| **RQ64** | O sistema deve permitir editar produtos, preços e fotos via painel administrativo. |
| **RQ65** | O sistema deve permitir remover itens do cardápio com confirmação obrigatória. |
| **RQ66** | O sistema deve permitir a alteração de banners da página inicial para campanhas. |
| **RQ67** | O sistema deve permitir o reajuste de preços em massa (por porcentagem). |
| **RQ68** | O sistema deve exibir a data da última atualização de cada item do cardápio. |

### US12 – Relatórios e Exportação
Como administrador, quero extrair dados consolidados em formato PDF, para facilitar a conferência contábil.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ69** | O sistema deve permitir a exportação de relatórios financeiros exclusivamente no formato PDF. |
| **RQ70** | O sistema deve permitir a geração de relatórios baseada em datas personalizadas. |
| **RQ71** | O sistema deve disparar um envio de resumo de faturamento diário automático por e-mail no fechamento. |
| **RQ72** | O sistema deve destacar a margem de lucro por categoria no relatório gerado. |

### US13 – Gestão Administrativa de Unidades (Mapa)
Como administrador, quero gerenciar as localizações no mapa para manter os pontos de venda atualizados.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ73** | O sistema deve permitir o cadastro de novas unidades com endereço e coordenadas. |
| **RQ74** | O sistema deve permitir editar horários de funcionamento e status de operação por unidade. |
| **RQ75** | O sistema deve disponibilizar os dados de geolocalização via API para consumo da interface. |
| **RQ76** | O sistema deve permitir desativar temporariamente uma unidade para ocultação no mapa. |

---

## Épico 6: Operação de Cozinha

### US14 – Gestão de Fila de Produção
Como cozinheiro, quero visualizar os pedidos em uma tela organizada por tempo de espera.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ77** | O sistema deve exibir pedidos em "cards" com itens, observações e tempo decorrido. |
| **RQ78** | O sistema deve mudar a cor do card (Semaforização) conforme o tempo de preparo. |
| **RQ79** | O sistema deve permitir dar "baixa" no item ou pedido completo via toque ou atalho. |
| **RQ79** | O sistema deve exibir o histórico dos pedidos por dia. |

### US15 – Painel de Chamada de Pedidos
Como cliente na loja, quero visualizar o status do meu pedido em um monitor para retirá-lo.

| ID | Descrição do Requisito Funcional |
| :--- | :--- |
| **RQ83** | O sistema deve exibir uma interface de status otimizada para Smart TVs. |
| **RQ84** | O sistema deve emitir um alerta sonoro padrão quando um pedido for marcado como "Pronto". |
| **RQ85** | O sistema deve remover o pedido da lista de "Pronto" após tempo configurável. |

---

## Controle de Versão

| Versão | Data | Autor(es) | Alterações |
| :--- | :--- | :--- | :--- |
| 1.0 | 27/03/2026 | Daniel  Nunes | Criação inicial do documento com 15 histórias de usuário e 56 requisitos funcionais. |
| 2.0 | 29/03/2026 | Daniel  Nunes | Remoção de US08 (Estoque) e US06 (Fluxo de Preparo), ajuste de Fidelidade, expansão de Cardápio e Dashboard de Vendas. |
| 3.0 | 29/03/2026 | Daniel Ferreira Nunes | Adição de US17 - Alertas de Promoção por Push/WhatsApp para marketing. |
| 4.0 | 29/03/2026 | Samuel Ribeiro | Ajuste de sequência de US e RQ e revisão do documento. |
| 4.1 | 31/03/2026 | Daniel  Nunes | Correção dos erros apontados pelo professor e adição de novas US. |
| 5.0 | 10/04/2026 | Camila Careli | Padronização estética, correção da sequência numérica (US/RQ) e refinamento das funcionalidades de Mapa e Caixa. |
| 5.1 | 26/04/2026 | Camila Careli | Refinamento das Histórias de Usuário. |