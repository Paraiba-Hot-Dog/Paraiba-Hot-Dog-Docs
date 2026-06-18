# Frontend

Documentação de referência da interface web do Paraíba Hot Dog.

## Tecnologias

- React 18
- TypeScript
- Vite
- Tailwind CSS

## Como executar

```bash
cd Paraiba-Hot-Dog-Front
npm install
cp .env.example .env
npm run dev
```

Disponível em `http://localhost:5173`.

## Estrutura do projeto

```text
src/
├── componentes/
│   ├── globais/        # Componentes compartilhados
│   ├── usuario/        # Área pública
│   └── administrador/  # Área administrativa
├── telas/
│   ├── usuario/
│   └── administrador/
├── contextos/
├── dados/
└── imagens/
    ├── itens/          # Fotos de produtos
    ├── local/          # Imagens de unidades
    ├── logos/
    ├── outros/
    └── social/         # Ícones de redes sociais
```

## Scripts

| Comando | Descrição |
|---------|-----------|
| `npm run dev` | Servidor de desenvolvimento |
| `npm run build` | Build de produção |
| `npm run preview` | Preview da build |

## Variáveis de ambiente

Todas as configurações sensíveis devem ser definidas no arquivo `.env`, a partir do modelo `.env.example`:

| Variável | Descrição |
|----------|-----------|
| `VITE_API_URL` | URL base da API |
| `VITE_API_BASE_URL` | URL alternativa da API |
| `VITE_KEYCLOAK_URL` | URL do servidor de autenticação |
| `VITE_KEYCLOAK_REALM` | Realm do provedor |
| `VITE_KEYCLOAK_CLIENT_ID` | Client ID da aplicação |

## Rotas

Consulte o mapa completo em [Módulos](../modulos.md).
