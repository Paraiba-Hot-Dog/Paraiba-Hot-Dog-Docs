# Paraiba Hot Dog

Sistema de gerenciamento de vendas, pedidos e análise de dados para a rede de lanchonetes Paraiba Hot Dog.

## Sobre o Projeto

Projeto desenvolvido para a disciplina **Técnicas de Programação em Plataformas Emergentes** sob orientação do Professor **Thiago Luiz de Souza Gomes**.

- **Cliente**: Paraiba Hot Dog (loja de cachorro-quente em Brasília)
- **Período**: 2026
- **Stack**: Python (FastAPI) + React + Docker

## Membros do Grupo

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/camilascareli.png" width="100px"><br>
      <small><strong>Camila Careli</strong><br>221007582</small>
    </td>
    <td align="center">
      <img src="https://github.com/DanielFsR.png" width="100px"><br>
      <small><strong>Daniel Ferreira</strong><br>222006632</small>
    </td>
    <td align="center">
      <img src="https://github.com/Mach1r0.png" width="100px"><br>
      <small><strong>Daniel Nunes</strong><br>211061565</small>
    </td>
    <td align="center">
      <img src="https://github.com/guilermanoo.png" width="100px"><br>
      <small><strong>Guilherme Coelho</strong><br>202016364</small>
    </td>
    <td align="center">
      <img src="https://github.com/jmarquees.png" width="100px"><br>
      <small><strong>João Victor</strong><br>200058576</small>
    </td>
    <td align="center">
      <img src="https://github.com/magnluiz.png" width="100px"><br>
      <small><strong>Magno Luiz</strong><br>180042696</small>
    </td>
    <td align="center">
      <img src="https://github.com/SamuelRicosta.png" width="100px"><br>
      <small><strong>Samuel Ribeiro</strong><br>211031486</small>
    </td>
  </tr>
</table>

## Como Executar

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

## Estrutura do Projeto

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

## Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python, FastAPI, SQLAlchemy |
| Frontend | React, TypeScript, Tailwind CSS |
| Banco de Dados | PostgreSQL/SQLite |
| Infraestrutura | Docker, Docker Compose |
| Documentação | MkDocs, Material Theme |
| CI/CD | GitHub Actions |

## Documentação
A documentação completa está disponível nas seguintes formas:
- **Local:** executar `mkdocs serve` e acessar http://127.0.0.1:8000  
- **Online:** acesse em https://tppe-gp-09.github.io/Paraiba-Hot-Dog/

### Como executar

```bash
# Alterar para a branch de documentação
git checkout docs

# Instalar dependências
pip install -r requirements-docs.txt

# Servir documentação
mkdocs serve

# Salvar as alterações no Git (Branch docs)
git add .
git commit -m "docs: descrição do que foi alterado"
git push origin docs

# Realizar o Deploy para o GitHub Pages
mkdocs gh-deploy
