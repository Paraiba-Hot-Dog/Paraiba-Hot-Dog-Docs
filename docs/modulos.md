# Módulos do Sistema

Visão geral das funcionalidades organizadas por área de negócio.

## Experiência do Cliente

| Módulo | Rotas principais | Descrição |
|--------|------------------|-----------|
| Página inicial | `/` | Landing page com carrosséis, destaques e acesso rápido |
| Cardápio | `/cardapio` | Listagem de produtos por categoria com fotos e preços |
| Sobre nós | `/sobre-nos` | História da marca, FAQ e depoimentos |
| Unidades | `/unidades/{slug}` | Horários, status (aberto/fechado) e mapa da unidade |
| Cartão fidelidade | `/cartao-fidelidade` | Consulta e acúmulo de pontos por telefone |
| Autenticação | `/login`, `/esqueci-senha`, `/recuperar-senha` | Acesso e recuperação de credenciais |

## Operação de Vendas

| Módulo | Rotas principais | Descrição |
|--------|------------------|-----------|
| Anotar pedidos (PDV) | `/admin/anotar-pedidos` | Grade de produtos, observações, totais e pagamento |
| Cancelamentos | — | Registro de motivos e relatório de perdas |

## Cozinha

| Módulo | Rotas principais | Descrição |
|--------|------------------|-----------|
| Fila de produção | `/cozinha`, `/admin/cozinha` | Cards com semaforização por status e baixa de pedidos |

## Business Intelligence

| Módulo | Rotas principais | Descrição |
|--------|------------------|-----------|
| Dashboard | `/dashboard`, `/admin/dashboard` | Faturamento, ticket médio, rankings e comparativos |

Indicadores disponíveis incluem faturamento por período, margem de lucro, top produtos, vendas por hora, dias mais movimentados e alertas de itens parados.

## Administração

| Módulo | Rotas principais | Descrição |
|--------|------------------|-----------|
| Painel | `/admin` | Hub de acesso às áreas administrativas |
| Cardápio (admin) | `/admin/cardapio` | CRUD de produtos, preços, fotos e banners |
| Unidades | `/admin/configuracoes/unidades` | Cadastro de lojas, horários e geolocalização |
| Usuários | `/admin/configuracoes/usuarios` | Gestão de perfis (caixa / administrador) |
| Blog | `/admin/configuracoes/blog` | Publicação de notícias e promoções |

## Segurança e Auditoria

- Autenticação via Keycloak com perfis separados
- Logoff automático por inatividade na área administrativa
- Logs de auditoria para alterações sensíveis (preços, exclusões)

## Mapa de rotas (resumo)

```text
Público
├── /
├── /cardapio
├── /sobre-nos
├── /cartao-fidelidade
├── /unidades/{slug}
└── /login

Administrativo (requer autenticação)
├── /admin
├── /admin/anotar-pedidos
├── /admin/cardapio
├── /admin/dashboard
├── /admin/cozinha
├── /admin/configuracoes/usuarios
├── /admin/configuracoes/unidades
└── /admin/configuracoes/blog
```

Para o detalhamento de requisitos por história de usuário, consulte o [Backlog do Produto](requisitos/backlog.md).
