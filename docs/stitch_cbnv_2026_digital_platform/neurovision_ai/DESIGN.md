---
name: NeuroVision AI
colors:
  surface: '#04132b'
  surface-dim: '#04132b'
  surface-bright: '#2b3953'
  surface-container-lowest: '#000e26'
  surface-container-low: '#0c1b34'
  surface-container: '#111f38'
  surface-container-high: '#1c2a43'
  surface-container-highest: '#27354e'
  on-surface: '#d7e2ff'
  on-surface-variant: '#c4c5d9'
  inverse-surface: '#d7e2ff'
  inverse-on-surface: '#23304a'
  outline: '#8e8fa3'
  outline-variant: '#444656'
  surface-tint: '#bac3ff'
  primary: '#bac3ff'
  on-primary: '#001f90'
  primary-container: '#214bff'
  on-primary-container: '#dcdfff'
  inverse-primary: '#1644fa'
  secondary: '#44f796'
  on-secondary: '#00391c'
  secondary-container: '#00da7d'
  on-secondary-container: '#005930'
  tertiary: '#bbc7df'
  on-tertiary: '#263144'
  tertiary-container: '#596479'
  on-tertiary-container: '#d6e1fb'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dee0ff'
  primary-fixed-dim: '#bac3ff'
  on-primary-fixed: '#00105b'
  on-primary-fixed-variant: '#002fc8'
  secondary-fixed: '#5bffa1'
  secondary-fixed-dim: '#20e385'
  on-secondary-fixed: '#00210e'
  on-secondary-fixed-variant: '#00522c'
  tertiary-fixed: '#d7e3fc'
  tertiary-fixed-dim: '#bbc7df'
  on-tertiary-fixed: '#101c2e'
  on-tertiary-fixed-variant: '#3c475b'
  background: '#04132b'
  on-background: '#d7e2ff'
  surface-variant: '#27354e'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The brand personality for this design system is authoritative, cutting-edge, and intellectually rigorous. It targets a sophisticated audience of researchers, clinicians, and AI engineers. The UI must evoke a sense of "Scientific Precision meets Future Intelligence," balancing the established tradition of ophthalmology and neuroscience with the disruptive nature of artificial intelligence.

The chosen style is **Glassmorphism mixed with High-Tech Minimalism**. This involves using deep navy depths with translucent, frosted layers that mimic the clarity of the eye's lens. Visual motifs like neural pathways and cortical maps are integrated via subtle background patterns and glowing green accents, representing the firing of neurons and data processing. The result is a premium, institutional interface that feels like a professional research terminal from the near future.

## Colors

The palette is anchored in a dark-mode first experience to emphasize the "high-tech" and "medical imaging" aesthetic. 

- **Deep Navy (#081426):** The primary canvas. It provides the necessary depth for neon accents to pop without causing eye strain.
- **Electric Blue (#214BFF):** Used for primary cognitive actions, data links, and high-importance UI elements.
- **Neuro Green (#2FEA8B):** Reserved for "active" neural states, success signals, and decorative biological motifs like wave patterns.
- **Functional Neutrals:** Light Text (#E7ECF7) ensures high readability against the dark background, while Secondary Text (#9AA8C7) manages the information hierarchy for metadata.

## Typography

This design system utilizes a high-contrast typographic pairing to bridge academia and technology.

- **Headlines:** Uses **Newsreader**. This serif font provides a "Literary/Academic" weight, grounding the congress in scientific tradition and prestige.
- **Body:** Uses **Inter**. Its systematic and neutral nature ensures maximum legibility for dense scientific abstracts and program schedules.
- **Technical Labels:** Uses **Space Grotesk**. This font is applied to badges, status indicators, and data points to provide a futuristic, monospaced feel that resonates with the AI theme.

## Layout & Spacing

The system follows a **Fixed Grid** philosophy for desktop (12-column) and a fluid model for mobile. To maintain a scientific and organized feel, the layout uses a rigid 4px baseline grid. 

Margins and gutters are generous (#xl) to prevent information density from becoming overwhelming. Content should be grouped into logical "zones" or "modules," separated by significant whitespace to mirror the clean aesthetics of a laboratory or modern medical facility. High-priority information, such as the event countdown or keynote speakers, should span larger column groups (8-12), while schedule items utilize a structured 4-column stack.

## Elevation & Depth

Depth is achieved through **Glassmorphism and Tonal Layering** rather than traditional drop shadows. 

1.  **Base Layer:** The Deep Navy (#081426) solid background.
2.  **Surface Layer:** Cards and containers use a semi-transparent version of the primary color with a 20px backdrop blur and a 1px "ghost border" in Neuro Green or Electric Blue (at 20% opacity).
3.  **Active State:** Elements that are interactive or "hot" receive a subtle inner glow (box-shadow: inset) in Electric Blue, simulating a backlit screen.
4.  **Shadows:** When used, shadows must be extremely diffused and tinted with the background hue (Deep Navy) to avoid a "muddy" look.

## Shapes

The shape language is **Soft (0.25rem - 0.75rem)**. While a technical theme might suggest sharp corners, the biological "Neuro" aspect of the congress requires more organic, approachable edges. 

Standard components (inputs, buttons) use a base radius of 4px. Larger containers like scientific cards use 12px. Circular shapes are reserved strictly for avatar clusters of speakers and specific "neural node" icons in the background patterns.

## Components

- **Scientific Cards:** These are the primary vessels for information. They should feature a "header" area with a Newsreader title, a 1px divider, and a metadata footer using Space Grotesk labels. Use backdrop blur to separate them from background neural patterns.
- **Buttons:**
    - *Primary:* Electric Blue background with white text. No border.
    - *Ghost:* 1px Neuro Green border with high-tracking Space Grotesk text.
- **Status Badges:** 
    - *Confirmed:* Neuro Green background (15% opacity) with solid Green text and a small "dot" icon representing an active signal.
    - *Pending:* Neutral Gray (#9AA8C7) with a dashed border.
- **Timeline Schedules:** A vertical 2px line in Electric Blue connects nodes. Active sessions glow with a Neuro Green outer shadow.
- **Accessible Forms:** Input fields use a Deep Navy background with a subtle Light Text border. On focus, the border transitions to a solid Electric Blue glow. Labels must always remain visible above the input area for accessibility.
- **Neural Accents:** Use SVG-based "path" animations that move subtly behind the UI to represent vision signals being processed by AI.