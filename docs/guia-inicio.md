# Guia de Início

Como configurar e executar o ecossistema Paraíba Hot Dog em ambiente local.

!!! warning "Configuração sensível"
    Credenciais, URLs de API e parâmetros de autenticação devem ser definidos apenas nos arquivos `.env` de cada componente, fornecidos pela equipe responsável pelo deploy. **Não versione nem publique valores reais de produção.**

## Pré-requisitos

| Ferramenta | Versão mínima | Uso |
|------------|---------------|-----|
| [Docker](https://docs.docker.com/get-docker/) + [Compose](https://docs.docker.com/compose/) | — | Backend + PostgreSQL |
| [Node.js](https://nodejs.org/) | 18+ | Frontend |
| [Python](https://www.python.org/) | 3.12+ | Documentação (MkDocs) |
| [Poetry](https://python-poetry.org/) | — | Backend local (opcional) |

## 1. Backend e banco de dados

```bash
cd Paraiba-Hot-Dog-Back
cp .env.example .env
# Edite o .env com as credenciais do seu ambiente
docker-compose up -d
```

| Serviço | URL local padrão |
|---------|------------------|
| API | `http://localhost:8000` |
| Swagger | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

As variáveis de conexão com o banco ficam no `.env` do backend. Consulte o `.env.example` do repositório para a lista completa.

## 2. Frontend

```bash
cd Paraiba-Hot-Dog-Front
npm install
cp .env.example .env
# Edite o .env com as URLs da API e do provedor de autenticação
npm run dev
```

A aplicação ficará disponível em `http://localhost:5173` (porta padrão do Vite).

### Variáveis de ambiente do frontend

Configure conforme o arquivo `.env.example` do repositório frontend:

| Variável | Descrição |
|----------|-----------|
| `VITE_API_URL` | URL base da API |
| `VITE_API_BASE_URL` | URL alternativa da API |
| `VITE_KEYCLOAK_URL` | URL do servidor de autenticação |
| `VITE_KEYCLOAK_REALM` | Realm configurado no provedor |
| `VITE_KEYCLOAK_CLIENT_ID` | Client ID da aplicação |

## 3. Documentação (este site)

```bash
cd Paraiba-Hot-Dog
pip install -r requirements-docs.txt
mkdocs serve
```

Acesse `http://127.0.0.1:8000` para visualizar localmente.

## Ordem recomendada de subida

1. Banco de dados e backend (`docker-compose up`)
2. Provedor de autenticação (se aplicável ao ambiente)
3. Frontend (`npm run dev`)

## Scripts úteis do frontend

| Comando | Descrição |
|---------|-----------|
| `npm run dev` | Servidor de desenvolvimento |
| `npm run build` | Build de produção |
| `npm run preview` | Preview da build local |

## Próximos passos

- Explore os [Módulos](modulos.md) para entender as funcionalidades
- Consulte a [Arquitetura](arquitetura.md) para detalhes técnicos
- Veja os [Diagramas](design/diagramas.md) para entender o schema
