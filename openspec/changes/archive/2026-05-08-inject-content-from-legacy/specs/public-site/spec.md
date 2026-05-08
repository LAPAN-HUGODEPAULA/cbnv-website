# Site Público (public-site)

## Purpose

Definir os requisitos públicos para injetar conteúdo legado, atualizar páginas institucionais e manter coerência visual entre Home, Sobre, Programação, Edições Anteriores, notícia de Save the Date e rodapé.

## ADDED Requirements

### Requirement: Footer FAPEMIG acknowledgement
O rodapé público SHALL exibir o logotipo da FAPEMIG originado de `_legacy/fapemig-logo.svg` juntamente com o nome "FAPEMIG" ou "Fundação de Amparo à Pesquisa do Estado de Minas Gerais".

#### Scenario: Footer shows FAPEMIG
- **WHEN** qualquer página pública renderiza o rodapé
- **THEN** o rodapé SHALL exibir o logotipo da FAPEMIG com texto alternativo acessível
- **AND** SHALL exibir o nome da FAPEMIG junto ao logotipo

### Requirement: Organization section on Home and About
A Home e a página Sobre SHALL exibir uma seção "Organização" com os logotipos das entidades organizadoras do XII CBNV.

#### Scenario: Home organization section
- **WHEN** o visitante acessa a Home
- **THEN** SHALL ver uma seção "Organização" ao final do conteúdo principal com os logotipos das entidades organizadoras

#### Scenario: About organization section with names and links
- **WHEN** o visitante acessa a página Sobre
- **THEN** SHALL ver uma seção "Organização" com logotipos, nomes das entidades e links externos para as entidades que possuem URL cadastrada
- **AND** entidades sem URL SHALL aparecer sem link externo

### Requirement: About page editorial structure
A página Sobre SHALL ser reestruturada com base factual no conteúdo legado do CBNV anterior e layout inspirado em `docs/stitch_cbnv_2026_digital_platform/sobre_e_local_xii_cbnv_2026/`, mantendo o estilo do site atual.

#### Scenario: About page sections
- **WHEN** o visitante acessa a página Sobre
- **THEN** SHALL ver as seções "Bem vindos", "O evento", "Objetivos", "O que esperar", "Local e acessibilidade", "Comissão organizadora" e "Organização"
- **AND** SHALL NOT ver a seção "eventos recentes"

#### Scenario: About page tone
- **WHEN** a seção "O evento" é renderizada
- **THEN** o texto SHALL usar tom institucional e factual
- **AND** SHALL evitar linguagem sensacionalista ou promessas exageradas

### Requirement: About location and accessibility
A página Sobre SHALL apresentar uma seção "Local e acessibilidade" com informações do local do evento e um Google Maps incorporado inline.

#### Scenario: Inline map is available
- **WHEN** o visitante acessa a seção "Local e acessibilidade"
- **THEN** SHALL ver informações textuais do local do evento
- **AND** SHALL ver um iframe do Google Maps com título acessível e carregamento lazy

### Requirement: About organizing committee
A página Sobre SHALL exibir a comissão organizadora copiada do 11o CBNV e incluir Hugo de Paula como Subcoordenador do Congresso, Pós-Doutorado em Neurociências (UFMG).

#### Scenario: Organizer cards include photos
- **WHEN** o visitante acessa a seção "Comissão organizadora"
- **THEN** cada integrante com foto disponível SHALL aparecer com nome, função, afiliação ou descrição e imagem
- **AND** os arquivos de fotos copiados SHALL usar nomes normalizados baseados nos nomes dos integrantes

#### Scenario: Hugo de Paula is included
- **WHEN** a comissão organizadora é renderizada
- **THEN** SHALL incluir "Hugo de Paula" como "Subcoordenador do Congresso"
- **AND** SHALL exibir a descrição "Pós-Doutorado em Neurociências (UFMG)"

### Requirement: Save the Date news image
A notícia "Save the Date: XII CBNV 2026 em Belo Horizonte!" SHALL exibir a imagem `_legacy/save-the-date.jpg`.

#### Scenario: Save the Date article renders image
- **WHEN** o visitante acessa a notícia "Save the Date: XII CBNV 2026 em Belo Horizonte!"
- **THEN** SHALL ver a imagem de Save the Date com texto alternativo descritivo

### Requirement: Congress Instagram link
O site público SHALL exibir link para o Instagram oficial do congresso em local de navegação social persistente.

#### Scenario: Instagram link is available
- **WHEN** o visitante acessa o rodapé ou outra área persistente de redes sociais
- **THEN** SHALL ver um link para `https://www.instagram.com/cbnvufmg/`
- **AND** o link SHALL abrir de forma segura com `rel="noopener noreferrer"` quando usar nova aba
