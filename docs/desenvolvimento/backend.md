# Backend

Documentação de referência da API REST do Paraíba Hot Dog.

## Tecnologias

- Python 3.12+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Poetry
- Docker

## Como executar (Docker)

```bash
cd Paraiba-Hot-Dog-Back
cp .env.example .env
docker-compose up -d
```

| Serviço | URL local padrão |
|---------|------------------|
| API | `http://localhost:8000` |
| Swagger | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

## Desenvolvimento local

```bash
poetry install
poetry shell
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

### Variáveis de ambiente

As credenciais e parâmetros de conexão ficam no `.env`. Utilize o `.env.example` como referência — **não publique valores reais de banco ou autenticação**.

| Variável | Descrição |
|----------|-----------|
| `POSTGRES_USER` | Usuário do banco |
| `POSTGRES_PASSWORD` | Senha do banco |
| `POSTGRES_DB` | Nome do banco |
| `POSTGRES_HOST` | Host do banco |
| `POSTGRES_PORT` | Porta do banco |

## Documentação interativa da API

A API expõe documentação automática via OpenAPI nos endpoints `/docs` (Swagger) e `/redoc` (ReDoc), disponíveis apenas no ambiente configurado.

## Modelo de dados

O schema do banco está documentado em [Diagramas](../design/diagramas.md).
