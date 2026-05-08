## Why

O site público do XII CBNV precisa incorporar conteúdo institucional e histórico já disponível no acervo legado para reduzir lacunas editoriais antes da publicação. A atualização também alinha páginas-chave aos protótipos visuais do Stitch, mantendo a coerência com a página principal e com os contratos já definidos para o site público.

## What Changes

- Adicionar a marca da FAPEMIG no rodapé, com logotipo legado e nome institucional.
- Adicionar seção "Organização" na Home e na página Sobre, com logotipos das entidades organizadoras; na página Sobre, os nomes das entidades devem ser exibidos com links quando disponíveis.
- Reestruturar a página Sobre usando conteúdo do CBNV anterior como referência editorial e o protótipo Stitch como referência visual.
- Adicionar as seções "Bem vindos", "O evento", "Objetivos", "O que esperar", "Local e acessibilidade", "Comissão organizadora" e "Organização" na página Sobre.
- Remover a seção "eventos recentes" da página Sobre, porque o histórico passa a estar concentrado em "Edições Anteriores".
- Incluir a comissão organizadora do 11o CBNV, normalizando nomes de arquivos de fotos para os integrantes, e adicionar Hugo de Paula como Subcoordenador do Congresso.
- Reestruturar a página "Edições Anteriores" usando o protótipo Stitch, removendo duplicação e enriquecendo as edições com dados dos anais em `_legacy/cbnv/` e referências públicas disponíveis.
- Reestruturar a página "Programação" usando o protótipo Stitch correspondente.
- Adicionar link para o Instagram oficial do congresso.
- Adicionar `_legacy/save-the-date.jpg` à notícia "Save the Date: XII CBNV 2026 em Belo Horizonte!".

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `public-site`: Atualizar requisitos de conteúdo, layout e navegação para Home, Sobre, Programação, Edições Anteriores, rodapé, redes sociais e notícias.
- `sponsors`: Ampliar a exibição pública para contemplar organizações, apoiadores institucionais e FAPEMIG no rodapé sem depender apenas da página de patrocinadores.
- `proceedings`: Refinar a página de Edições Anteriores para consumir dados históricos e anais legados, eliminando conteúdo duplicado.
- `program`: Alinhar a página pública de Programação ao design Stitch atualizado sem alterar a estrutura de dados da programação.

## Impact

- Templates, partials e estilos do site público, especialmente Home, Sobre, Programação, Edições Anteriores, notícia de Save the Date e rodapé global.
- Assets estáticos ou mídia migrada a partir de `_legacy/`, incluindo logotipos, fotos de comissão, imagem de Save the Date e possíveis dados dos anais.
- Fixtures, modelos CMS ou conteúdo inicial, caso as páginas sejam alimentadas por Wagtail em vez de conteúdo estático.
- Testes de renderização pública, links externos, presença de imagens, remoção de duplicação e regressões de navegação.
