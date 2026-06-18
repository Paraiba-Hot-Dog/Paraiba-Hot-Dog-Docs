# Paraíba Hot Dog

Documentação central do ecossistema **Paraíba Hot Dog** — sistema de gerenciamento de vendas, pedidos e business intelligence para a rede de lanchonetes.

## Ecossistema

| Componente | Descrição |
|-------------|-----------|
| Frontend | Interface web (React + TypeScript) |
| Backend | API REST (FastAPI + PostgreSQL) |
| **Este repositório** | Documentação oficial (MkDocs) |

## Executar a documentação localmente

```bash
cd Paraiba-Hot-Dog
pip install -r requirements-docs.txt
mkdocs serve
```

Acesse `http://127.0.0.1:8000`.

## Publicar no GitHub Pages

O deploy é realizado pelo workflow `.github/workflows/deploy-docs.yml` ou manualmente com `mkdocs gh-deploy`.

## Estrutura deste repositório

```text
Paraiba-Hot-Dog/
├── docs/                    # Conteúdo da documentação
├── mkdocs.yml               # Configuração do site
├── requirements-docs.txt    # Dependências Python
└── .github/workflows/       # Deploy automático
```

## Stack do projeto

| Camada | Tecnologia |
|--------|-----------|
| Frontend | React, TypeScript, Vite, Tailwind CSS |
| Backend | Python, FastAPI, SQLAlchemy, Alembic |
| Banco de Dados | PostgreSQL |
| Autenticação | Keycloak (OIDC) |
| Infraestrutura | Docker, Docker Compose |
| Documentação | MkDocs, Material Theme |

## Equipe

Camila Careli · Daniel Ferreira · Daniel Nunes · Guilherme Coelho · João Victor · Magno Luiz · Samuel Ribeiro

## Demonstração do Produto com o Cliente

Assista ao vídeo que gravamos junto com o cliente para conferir a apresentação e o funcionamento do nosso produto:

[![Demonstração do Produto Paraíba Hot Dog](https://img.youtube.com/vi/Z70tKV3NypQ/maxresdefault.jpg)](https://youtu.be/Z70tKV3NypQ)

*Clique na imagem acima para assistir ao vídeo no YouTube.*