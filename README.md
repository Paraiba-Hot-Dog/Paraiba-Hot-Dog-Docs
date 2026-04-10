## Deploy e Branch de Publicação

> [!IMPORTANT]
> **Não realizem commits manuais na branch `gh-pages`.**

Esta branch é utilizada exclusivamente para o deploy automático via GitHub Pages. Ela é gerada e sobrescrita pelo comando `mkdocs gh-deploy`. 
- Todo o desenvolvimento deve ser feito na branch `docs`.
- Alterações feitas diretamente na `gh-pages` serão perdidas na próxima atualização do site.
