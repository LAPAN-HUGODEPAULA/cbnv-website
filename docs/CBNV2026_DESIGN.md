# DESIGN.md — XII CBNV 2026

## Product

Website and digital platform for the XII Congresso Brasileiro de Neurociências da Visão — CBNV 2026.

## Brand essence

Scientific, translational, accessible, modern, institutional, visually memorable.

The design should combine vision neuroscience, responsible artificial intelligence, clinical translation, public science, and Brazilian academic identity.

## Core message

XII Congresso Brasileiro de Neurociências da Visão  
CBNV 2026  
Neurovisão na Era da Inteligência Artificial  
11–13 de novembro de 2026  
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha

R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
Google maps location: https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6

Google maps embed map code:
```javascript
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3752.375224166495!2d-43.96900072425095!3d-19.86637168150776!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xa690f5cd6fa2db%3A0xa63066267bf8fe3f!2sCentro%20de%20Atividades%20Did%C3%A1ticas%201%20-%20CAD%201!5e0!3m2!1spt-BR!2sbr!4v1778262291254!5m2!1spt-BR!2sbr"
 width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
</iframe>
```

## Visual direction

Use a deep navy scientific interface with electric blue and neuro-green accents. Use abstract visual motifs inspired by retina, visual signals, neural circuits, AI graphs, cortical maps, electrophysiological traces and visual fields.

The design must look modern and premium, but not decorative at the expense of clarity. It should feel like a serious scientific congress with a strong contemporary technology theme.

## Color tokens

```css
:root {
  --cbnv-navy-950: #081426;
  --cbnv-navy-900: #0E1E3A;
  --cbnv-blue-600: #214BFF;
  --cbnv-green-400: #2FEA8B;
  --cbnv-text-light: #E7ECF7;
  --cbnv-text-muted: #9AA8C7;
  --cbnv-bg-light: #F5F7FB;
  --cbnv-text-dark: #111827;
  --cbnv-warning: #F59E0B;
  --cbnv-white: #FFFFFF;
}
```

## Typography

Use a refined display style for major headings and a highly legible sans-serif for body and interface.

Guidelines:
- Hero title: large, confident, high contrast.
- Section titles: clear and structured.
- Body text: generous line height.
- Program times: large, tabular, highly legible.
- Avoid small low-contrast text.

## Layout principles

1. Mobile-first responsiveness.
2. Clear hierarchy above visual complexity.
3. Dates, location and primary CTAs visible immediately.
4. Program timeline must be readable on mobile.
5. Cards should have strong spacing and clear labels.
6. Avoid dense text blocks on the Home page.
7. Use progressive disclosure for details.
8. Support users who arrive with a specific task: submit, register, check program, find location.

## Components

### Header

- Desktop: horizontal nav with primary CTA.
- Mobile: accessible menu.
- Must include: Início, Sobre, Programação, Palestrantes, Submissões, Inscrição, Edições anteriores, Contato.

### Hero

Must include:
- event name;
- theme;
- dates;
- location;
- format;
- CTA buttons;
- subtle scientific visual motif.

### Cards

Use for:
- key facts;
- program days;
- speakers;
- submission steps;
- editions;
- sponsors.

### Badges

Use for:
- Confirmado;
- A confirmar;
- Híbrido;
- Presencial;
- Plenária;
- Palestra;
- Sessão temática;
- Pôsteres;
- Apresentação oral;
- Mesa-redonda.

Badges must not rely only on color.

### Program timeline

Desktop:
- timeline/grid by day;
- filters;
- expanded cards for session details.

Mobile:
- vertical cards;
- time prominent;
- type badge;
- title and short description;
- expandable details.

### Forms

- Large labels.
- Clear required markers.
- Inline validation.
- Error summaries.
- Stepper for submission.
- Save draft and submit actions clearly separated.

### Tables

For internal dashboards:
- filters;
- search;
- status badges;
- clear action buttons;
- export buttons.

## Accessibility

Target WCAG 2.2 AA.

Rules:
- High contrast.
- Keyboard accessible.
- Visible focus.
- Semantic headings.
- Alt text for images.
- No color-only status.
- Respect reduced motion.
- Avoid tiny text.
- Avoid visual noise behind text.
- Make forms understandable.

## Motion

Use minimal motion:
- subtle hover states;
- gentle fades;
- no heavy parallax;
- no flashing;
- respect reduced motion.

## Content tone

Portuguese Brazilian. Scientific, objective, institutional and accessible.

Examples:
- “Submeta seu trabalho”
- “Ver programação”
- “Inscrição em breve”
- “Vídeo solicitado apenas na etapa final”
- “Participantes a confirmar”
- “Aguardando parecer da Comissão Científica”

## Screens to generate first

1. Home.
2. Programação.
3. Submissões.
4. Área do Autor.
5. Formulário de Submissão.
6. Palestrantes.
7. Sobre/Local/Acessibilidade.
8. Edições anteriores.
9. Dashboard da Comissão.

## Do not design

- Native mobile app.
- Payment system.
- QR code check-in system.
- Certificate generator.
- Video hosting platform.
- Complex editorial RBAC.
- Notion-like project management interface.

## Implementation target

The design should be implementable with Django templates, Wagtail CMS, Tailwind CSS and light HTMX/Alpine.js interactions. Avoid designs that require a full React SPA unless strictly necessary.