# Documentação

Este repositório centraliza a documentação do ecossistema Paraíba Hot Dog, publicada via **MkDocs**.

## Executar localmente

```bash
cd Paraiba-Hot-Dog
pip install -r requirements-docs.txt
mkdocs serve
```

Acesse `http://127.0.0.1:8000`.

## Publicar alterações

O deploy é realizado pelo pipeline de CI configurado no repositório. Para publicação manual:

```bash
mkdocs gh-deploy
```

## Estrutura da documentação

```text
docs/
├── index.md              # Página inicial
├── sobre.md              # Contexto e objetivos
├── modulos.md            # Funcionalidades por área
├── arquitetura.md        # Visão técnica
├── guia-inicio.md        # Setup do ambiente
├── design/
│   ├── prototipos.md     # Figma
│   └── diagramas.md      # DER e schema do banco
├── requisitos/
│   └── backlog.md        # Histórias de usuário
├── desenvolvimento/
│   ├── frontend.md
│   ├── backend.md
│   └── documentacao.md
└── img/                  # Imagens e diagramas
```

## Configuração

O arquivo `mkdocs.yml` na raiz define tema, navegação e metadados do site.
