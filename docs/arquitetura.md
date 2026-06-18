# Arquitetura

Visão geral da arquitetura do ecossistema Paraíba Hot Dog.

## Visão de alto nível

```text
┌─────────────────────┐       ┌─────────────────────┐       ┌──────────────────┐
│   Frontend (Web)    │ HTTP  │   Backend (API)     │  SQL  │   PostgreSQL     │
│   React + Vite      │◄─────►│   FastAPI           │◄─────►│                  │
└─────────────────────┘       └──────────┬──────────┘       └──────────────────┘
                                         │
                                         │ OAuth2 / OIDC
                                         ▼
                              ┌─────────────────────┐
                              │  Provedor de auth   │
                              │  (ex.: Keycloak)    │
                              └─────────────────────┘
```

## Componentes e responsabilidades

| Componente | Responsabilidade |
|------------|------------------|
| Interface web | Telas do cliente e admin, roteamento, consumo da API |
| API REST | Regras de negócio, persistência, autenticação |
| Documentação | Referência funcional e técnica do sistema |

## Frontend

- **Framework:** React 18 com TypeScript
- **Build:** Vite
- **Estilização:** Tailwind CSS
- **Roteamento:** baseado em `window.location.pathname` (SPA sem React Router)
- **Autenticação:** integração com provedor OIDC via variáveis de ambiente

### Estrutura de pastas

```text
src/
├── componentes/
│   ├── globais/        # Componentes compartilhados
│   ├── usuario/        # Componentes da área pública
│   └── administrador/  # Componentes da área admin
├── telas/
│   ├── usuario/        # Páginas do cliente
│   └── administrador/  # Páginas administrativas
├── contextos/          # Estado global (ex.: autenticação)
├── dados/              # Mocks e dados estáticos
└── imagens/            # Assets visuais
```

## Backend

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Migrações:** Alembic
- **Banco:** PostgreSQL
- **Gerenciador de dependências:** Poetry
- **Documentação da API:** Swagger (`/docs`) e ReDoc (`/redoc`)

## Autenticação

O frontend se comunica com o provedor de identidade por meio de variáveis configuradas no `.env`:

| Variável | Descrição |
|----------|-----------|
| `VITE_KEYCLOAK_URL` | URL do servidor de autenticação |
| `VITE_KEYCLOAK_REALM` | Realm do ambiente |
| `VITE_KEYCLOAK_CLIENT_ID` | Client ID da aplicação |
| `VITE_API_URL` / `VITE_API_BASE_URL` | URL base da API |

Perfis de acesso:

- **Administrador** — acesso completo às rotas `/admin/*`
- **Caixa** — operações de venda (conforme permissões configuradas)

## Banco de dados

PostgreSQL com SQLAlchemy e Alembic. Os diagramas (DER e schema) estão em [Diagramas](design/diagramas.md).

## Deploy

- **Documentação:** publicada via MkDocs no GitHub Pages
- **Aplicação:** containers Docker para backend e banco; frontend servido como build estática

## Design e requisitos

- Protótipos interativos: [Figma](design/prototipos.md)
- Diagramas: [DER e schema do banco](design/diagramas.md)
- Requisitos funcionais: [Backlog do Produto](requisitos/backlog.md)
