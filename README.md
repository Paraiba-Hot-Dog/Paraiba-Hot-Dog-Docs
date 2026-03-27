# Paraiba Hot Dog

Sistema de gerenciamento de vendas, pedidos e análise de dados para a rede de lanchonetes Paraiba Hot Dog.

## 📋 Sobre o Projeto

Projeto desenvolvido para a disciplina **Técnicas de Programação em Plataformas Emergentes** sob orientação do Professor **Thiago Luiz de Souza Gomes**.

- **Cliente**: Paraiba Hot Dog (loja de cachorro-quente em Brasília)
- **Período**: 2026
- **Stack**: Python (FastAPI) + React + Docker

## 👥 Integrantes do Grupo

| Nome | Matrícula |
|------|-----------|
| Daniel Ferreira Nunes | 211061565 |
| Samuel Ribeiro da Costa¹ | 211031486 |
| Daniel Ferreira Santos Rabelo | 222006632 |
| Magno Luiz | 180042696 |
| Camila Careli | 221007582 |
| João Victor Marques | 200058576 |
| Guilherme Coelho Mendonça | 202016364 |

¹ Líder do projeto

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose
- Python 3.12+
- Node.js 18+ (para desenvolvimento frontend)

### Opção 1: Com Docker (Recomendado)

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/Paraiba-Hot-Dog.git
cd Paraiba-Hot-Dog

# Iniciar os serviços
docker-compose up -d

# Acessar a aplicação
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# Documentação API: http://localhost:8000/docs
```

### Opção 2: Desenvolvimento Local

#### Backend (FastAPI)

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
uvicorn app.main:app --reload --port 8000
```

#### Frontend (React)

```bash
# Navegar até a pasta do frontend
cd frontend

# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm start
```

### Opção 3: Documentation (MkDocs)

```bash
# alterar para a branch docs 

# Instalar dependências da documentação
pip install -r requirements-docs.txt

# Servir documentação localmente
mkdocs serve

# Acessar em http://127.0.0.1:8000
```

## 📁 Estrutura do Projeto

```
Paraiba-Hot-Dog/
├── backend/                 # API FastAPI
│   ├── app/
│   ├── tests/
│   └── requirements.txt
├── frontend/                # Aplicação React
│   ├── src/
│   ├── public/
│   └── package.json
├── docs/                    # Documentação
│   ├── index.md
│   ├── Reuniões/
│   └── Ponto de controle 01/
├── docker-compose.yml       # Orquestração de containers
├── mkdocs.yml               # Configuração de documentação
└── README.md                # Este arquivo
```

## 🛠 Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python, FastAPI, SQLAlchemy |
| Frontend | React, TypeScript, Tailwind CSS |
| Banco de Dados | PostgreSQL/SQLite |
| Infraestrutura | Docker, Docker Compose |
| Documentação | MkDocs, Material Theme |
| CI/CD | GitHub Actions |

## 📚 Documentação

A documentação completa está disponível em:
- **Local**: `mkdocs serve` e acessar http://127.0.0.1:8000
- **Online**: GitHub Pages (após deploy)

Seções disponíveis:
- [Atas de Reuniões](docs/Reuniões/)
- [Histórias de Usuário](docs/Ponto%20de%20controle%2001/)

