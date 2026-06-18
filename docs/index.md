# Paraíba Hot Dog

Bem-vindo à documentação oficial do **Paraíba Hot Dog** — plataforma integrada de gestão de vendas, pedidos e inteligência de negócios para a rede de lanchonetes.

## O que é o sistema

O Paraíba Hot Dog centraliza a operação da rede em um único ecossistema digital, conectando a experiência do cliente à gestão interna da loja. A solução foi pensada para escalar com múltiplas unidades, reduzir retrabalho operacional e apoiar decisões com dados em tempo real.

### Principais capacidades

| Área | O que o sistema oferece |
|------|-------------------------|
| **Cliente** | Site institucional, cardápio online, localização de unidades e cartão fidelidade |
| **Operação** | PDV para registro de pedidos e cozinha |
| **Gestão** | Dashboard de BI, gestão de cardápio, unidades, usuários e blog |
| **Segurança** | Autenticação com perfis de acesso e auditoria de ações administrativas |

## Componentes do ecossistema

| Componente | Descrição |
|-------------|-----------|
| Frontend | Interface web (React + TypeScript) |
| Backend | API REST (FastAPI + PostgreSQL) |
| Documentação | Site central de referência (este site) |

## Navegação rápida

- **[Sobre o Projeto](sobre.md)** — contexto, objetivos e escopo
- **[Módulos](modulos.md)** — funcionalidades por área do sistema
- **[Arquitetura](arquitetura.md)** — visão técnica e integração entre serviços
- **[Guia de Início](guia-inicio.md)** — como rodar o ambiente localmente
- **[Design e Diagramas](design/prototipos.md)** — protótipos Figma e diagramas do sistema
- **[Backlog do Produto](requisitos/backlog.md)** — histórias de usuário e requisitos

## Stack tecnológica

| Camada | Tecnologias |
|--------|-------------|
| Frontend | React, TypeScript, Vite, Tailwind CSS |
| Backend | Python, FastAPI, SQLAlchemy, Alembic |
| Banco de dados | PostgreSQL |
| Autenticação | Keycloak |
| Infraestrutura | Docker, Docker Compose |
| Documentação | MkDocs, Material Theme |
| CI/CD | GitHub Actions |

