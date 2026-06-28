---
name: Botanical Heritage
colors:
  surface: '#fbf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#fbf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ef'
  surface-container: '#efeeea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e4e2de'
  on-surface: '#1b1c1a'
  on-surface-variant: '#414943'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f0ed'
  outline: '#717973'
  outline-variant: '#c1c8c1'
  surface-tint: '#3d6751'
  primary: '#3d6751'
  on-primary: '#ffffff'
  primary-container: '#a8d5ba'
  on-primary-container: '#345d48'
  inverse-primary: '#a4d1b6'
  secondary: '#735664'
  on-secondary: '#ffffff'
  secondary-container: '#fed8e9'
  on-secondary-container: '#795c6a'
  tertiary: '#6c5777'
  on-tertiary: '#ffffff'
  tertiary-container: '#dcc2e7'
  on-tertiary-container: '#624e6d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bfedd1'
  primary-fixed-dim: '#a4d1b6'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#254f3a'
  secondary-fixed: '#fed8e9'
  secondary-fixed-dim: '#e1bdcd'
  on-secondary-fixed: '#2a1520'
  on-secondary-fixed-variant: '#593f4c'
  tertiary-fixed: '#f4d9ff'
  tertiary-fixed-dim: '#d8bee3'
  on-tertiary-fixed: '#261430'
  on-tertiary-fixed-variant: '#533f5e'
  background: '#fbf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2de'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

The design system is engineered for an intersection of high-end floral artistry and professional corporate reporting. The brand personality is **sophisticated, serene, and authoritative**, moving away from "rustic" tropes toward a **premium international** aesthetic. 

The visual style leans into **Minimalism** with a touch of **Glassmorphism** for data overlays. It prioritizes expansive whitespace, precise alignment, and a curated color palette to evoke a sense of calm reliability. The emotional response should be one of "effortless luxury"—where complex business data feels as organic and organized as a well-tended garden.

## Colors

The palette is a sophisticated "Floral Pastel" arrangement, designed to maintain professional legibility while reflecting the product's core industry.

- **Primary (Mint Green):** Used for growth indicators, primary actions, and brand accents. It provides a refreshing, stable base.
- **Secondary (Soft Pink):** Used for highlights, decorative elements, and softer call-to-actions.
- **Tertiary (Lavender):** Reserved for data visualization categories and subtle background accents.
- **Neutral (Creamy White):** The "Paper" of the system. We avoid pure white (#FFFFFF) in favor of a warm, premium off-white to reduce eye strain and feel more organic.
- **Accent (Deep Moss):** (Implementation note) Use a high-contrast dark green (#2D4033) for all body text and icons to ensure WCAG AA accessibility against pastel backgrounds.

## Typography

This design system utilizes a high-contrast typographic pairing to balance editorial elegance with functional data density.

- **Headings:** The use of **Playfair Display** introduces a traditional, literary feel suitable for international reports. Use "Optical Sizing" features where available to maintain sharpness at smaller sizes.
- **Body & Interface:** **Hanken Grotesk** provides a clean, neutral, and modern counterpoint. Its open counters ensure readability in complex data tables and financial summaries.
- **Hierarchy:** Maintain a generous vertical rhythm. Headings should always have significant top-margin spacing to allow the "content to breathe."

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop reporting to ensure data visualizations remain consistent and proportional, transitioning to a **Fluid** model for mobile.

- **Grid:** A 12-column grid is standard for desktop. For business analysis dashboards, utilize a 4-column "Sidebar + Content" split (3 cols for navigation, 9 cols for data).
- **Spacing Rhythm:** Based on an 8px baseline. Use 16px (2 units) for internal component padding and 48px-64px (6-8 units) for section vertical spacing.
- **Breakpoints:**
  - **Mobile:** < 768px (1 column, 16px margins)
  - **Tablet:** 768px - 1024px (6 columns, 24px margins)
  - **Desktop:** > 1024px (12 columns, 48px margins)

## Elevation & Depth

This design system uses **Tonal Layers** and **Ambient Shadows** to create a sense of organized hierarchy without visual clutter.

- **Surface Levels:** 
  - **Level 0 (Background):** Neutral Cream (#FDFBF7).
  - **Level 1 (Cards/Containers):** Pure White (#FFFFFF) with a 1px stroke in a slightly darker cream or 5% opacity primary color.
- **Shadows:** Avoid heavy black shadows. Use "Botanical Shadows"—soft, diffused blurs with a tiny hint of the primary green tint (`box-shadow: 0 10px 30px rgba(168, 213, 186, 0.15)`).
- **Glassmorphism:** Use for floating navigation bars or data tooltips. Apply a 12px backdrop-blur and 80% opacity on the White surface.

## Shapes

The shape language is **Rounded**, reflecting the organic curves of petals and leaves while maintaining the structure of a professional report.

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) radius.
- **Large Containers:** Section-level cards or hero images use a 1.5rem (24px) radius to soften the layout.
- **Icons:** Use a 1.5px or 2px stroke weight with rounded caps and joins to match the typography's softness.

## Components

- **Buttons:** 
  - *Primary:* Solid Mint Green with Deep Moss text. No bold shadows; use a subtle hover lift.
  - *Secondary:* Outlined (1px) in Soft Pink with matching text.
- **Data Cards:** White background, 24px padding, with a top-accent border (2px) in the color corresponding to the data category (Mint, Pink, or Lavender).
- **Input Fields:** Soft Cream background with a 1px border that transitions to Mint Green on focus. Labels use the `label-sm` style.
- **Chips/Tags:** Used for "Region" or "Flower Category." These should be pill-shaped (radius: 100px) with low-saturation pastel backgrounds and high-saturation text.
- **Progress Indicators:** Use thin, elegant lines rather than thick bars. Use the primary Mint for positive growth and a muted Terracotta (system-only color) for negative trends.
- **Reports/Tables:** Row-based layouts with no vertical borders. Use alternating row tints (1% Mint Green) for readability in dense internationalization reports.