# Plan de Implementación — Aldea Global 2

## Visión General

Sitio web basado en el design system **Botanical Heritage** con la skill [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).

### Arquitectura de navegación — distinción clave

| Nivel | Qué es | Cómo se accede |
|---|---|---|
| **Navbar** | Secciones permanentes del sitio: Dashboard, Acuerdo, Realidad, Fase 2 | Siempre visible en todas las páginas |
| **Entregas** | Documentos de entrega del proyecto (Entrega 1, 2, 3) | **Solo desde la página de inicio**, mediante cards/botones. No aparecen en el navbar |

Las entregas son contenido interno accesible desde el hub central (inicio), no secciones de navegación global. El navbar refleja la arquitectura de información del sitio; las entregas son un recurso del proyecto.

---

## Estructura del Proyecto

```
/
├── index.html                  ← Página de inicio (hub con acceso a entregas)
├── acuerdo/
│   └── index.html              ← Sección del navbar: Acuerdo
├── realidad/
│   └── index.html              ← Sección del navbar: Realidad
├── fase2/
│   └── index.html              ← Sección del navbar: Fase 2
├── entregas/
│   ├── entrega-1/
│   │   └── index.html          ← Entrega 1 (acceso solo desde inicio)
│   ├── entrega-2/
│   │   └── index.html          ← Entrega 2 (acceso solo desde inicio)
│   └── entrega-3/
│       └── index.html          ← Entrega 3 (acceso solo desde inicio)
├── diseño/
│   └── DESIGN.md               ← Tokens y directrices del sistema
└── assets/
    ├── fonts/
    ├── images/
    └── css/
        └── botanical.css       ← Variables y utilidades globales
```

> **Nota:** Las páginas bajo `/entregas/` no tienen ítem en el navbar. El navbar de esas páginas es idéntico al global pero sin marcar ningún ítem activo, ya que son documentos independientes, no secciones del sitio.

---

## Sistema de Diseño a Implementar

### Fuentes (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&family=Hanken+Grotesk:wght@400;600&display=swap" rel="stylesheet">
```

### Variables CSS Globales (`botanical.css`)
```css
:root {
  /* Superficies */
  --surface:               #fbf9f5;
  --surface-container-low: #f5f3ef;
  --surface-container:     #efeeea;
  --on-surface:            #1b1c1a;
  --on-surface-variant:    #414943;
  --outline:               #717973;
  --outline-variant:       #c1c8c1;

  /* Colores de marca */
  --primary:               #3d6751;
  --on-primary:            #ffffff;
  --primary-container:     #a8d5ba;
  --secondary:             #735664;
  --secondary-container:   #fed8e9;
  --tertiary:              #6c5777;
  --tertiary-container:    #dcc2e7;
  --error:                 #ba1a1a;

  /* Tipografía */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body:    'Hanken Grotesk', system-ui, sans-serif;

  /* Radios */
  --radius-sm:   0.25rem;
  --radius:      0.5rem;
  --radius-md:   0.75rem;
  --radius-lg:   1rem;
  --radius-xl:   1.5rem;
  --radius-full: 9999px;

  /* Sombra botánica */
  --shadow-botanical: 0 10px 30px rgba(168, 213, 186, 0.15);
}
```

---

## Página Principal (`index.html`)

### Propósito
Presentar el proyecto **Aldea Global 2** y ofrecer acceso claro a cada entrega mediante botones/cards destacados.

### Secciones

#### 1. Navbar
- Logo "Aldea Global 2" (círculo verde con ícono de hoja)
- Links: `Dashboard` · `Acuerdo` · `Realidad` · `Fase 2`
- **Las entregas NO aparecen aquí.** El navbar es la navegación del sitio, no del proyecto.
- Sticky con glassmorphism: `backdrop-filter: blur(12px)` + `background: rgba(251,249,245,0.8)`
- Ítem activo subrayado con línea de 2px `var(--primary)` debajo del texto

#### 2. Hero
```
┌─────────────────────────────────────────┐
│  [eyebrow] CULTURA DE EXCELENCIA        │
│                                         │
│  Aldea Global 2                         │
│  — Proyecto de Equipo                   │
│                                         │
│  Subtítulo: Tejiendo una red de...      │
│                                         │
│  [CTA primario]  [CTA secundario]       │
└─────────────────────────────────────────┘
```
- Fondo `--surface` (crema cálido)
- Headline en `Playfair Display 600`, con palabra clave en itálica
- Sin imagen de fondo; el espacio negativo es el lujo

#### 3. Sección de Entregas ← **núcleo de la página principal**
```
┌─────────────────────────────────────────────────────────┐
│  [eyebrow] AVANCE DEL PROYECTO                          │
│  Nuestras Entregas                                       │
│                                                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │
│  │ 01           │ │ 02           │ │ 03           │    │
│  │              │ │              │ │              │    │
│  │  Acuerdo     │ │  Realidad    │ │  Fase 2      │    │
│  │  de Equipo   │ │  del Equipo  │ │  Estratégica │    │
│  │              │ │              │ │              │    │
│  │ Descripción  │ │ Descripción  │ │ Descripción  │    │
│  │ breve (2     │ │ breve        │ │ breve        │    │
│  │ líneas max)  │ │              │ │              │    │
│  │              │ │              │ │              │    │
│  │ [→ Ver]      │ │ [→ Ver]      │ │ [→ Ver]      │    │
│  └──────────────┘ └──────────────┘ └──────────────┘    │
└─────────────────────────────────────────────────────────┘
```

**Especificaciones de las cards de entrega:**
- Fondo `#ffffff`, padding `24px`, `border-radius: var(--radius-xl)`
- Borde superior de `2px` con color por entrega:
  - Entrega 1 → `var(--primary)` (mint verde)
  - Entrega 2 → `var(--secondary)` (rosa suave)
  - Entrega 3 → `var(--tertiary)` (lavanda)
- Número (`01`, `02`, `03`) en `Playfair Display`, tamaño grande, color `--outline-variant`
- Título en `Playfair Display 600 24px`
- Descripción en `Hanken Grotesk 16px`, color `--on-surface-variant`
- Botón "Ver entrega →": ghost button con color del acento de la card
- Sombra: `var(--shadow-botanical)` en hover
- Transición hover: `transform: translateY(-4px)` suave

#### 4. Footer
- Logo + "International Excellence © 2024"
- Links: Privacidad · Términos · Soporte
- Iconos de compartir e imprimir (alineados a la derecha)
- Fondo `--surface-container-low`, sin borde superior visible

---

## Entrega 1: Acuerdo de Equipo (`/entregas/entrega-1/`)

> Accesible solo desde la card "Entrega 1" en el inicio. El diseño de referencia es `screen.png`.

| # | ID en diseño | Sección | Componentes clave |
|---|---|---|---|
| 1 | Hero | Acuerdo de Equipo & Gestión Humana | Headline bilingüe itálica + 2 CTAs |
| 2 | 01 Convivencia | Compromisos de Armonía Grupal | Card 2 cols: texto izq + imagen der, 3 métricas, quote overlay |
| 3 | 02 Ecosistema Digital | Canales de Fluidez | 3 íconos centrados con label + sublabel |
| 4 | 03 El Camino del Diálogo | Resolución Orgánica | 2 cols: texto izq + lista de 3 pasos con bullet verde/gris |
| 5 | Protocolo de Integridad | Salvaguardando el Propósito | Card grande con 3 sub-cards: Acompañamiento, Formalización, Reasignación |

### Componentes específicos

**Hero de sección:**
```css
.section-hero {
  text-align: center;
  padding: 80px 48px;
  background: var(--surface);
}
.section-hero .eyebrow {
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--on-surface-variant);
}
.section-hero h1 em {
  font-style: italic;
  color: var(--primary); /* palabra clave en verde */
}
```

**Card 2 columnas (Convivencia):**
```
┌─────────────────────────────────────────────────┐
│ [eyebrow] 01. CONVIVENCIA                       │
│                                                 │
│  Texto + cita         │  Imagen redondeada      │
│  blockquote           │  + overlay quote        │
│  ─────────────────    │  (glassmorphism)        │
│  100%  Plena  Total   │                         │
│  label label label    │                         │
└─────────────────────────────────────────────────┘
```

**Métricas:**
```css
.metric-value {
  font-family: var(--font-display);
  font-size: 32px;
  font-weight: 600;
  color: var(--on-surface);
}
.metric-label {
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--on-surface-variant);
}
```

**Quote overlay (glassmorphism):**
```css
.quote-overlay {
  background: rgba(255,255,255,0.8);
  backdrop-filter: blur(12px);
  border-radius: var(--radius-lg);
  padding: 16px 20px;
  font-family: var(--font-display);
  font-style: italic;
  font-size: 14px;
}
```

**Chips / Tags (valores):**
```css
.chip {
  display: inline-flex;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 600;
  background: var(--primary-container);
  color: var(--on-primary-container);
}
```

**Cards numeradas (Protocolo de Integridad):**
- Número en círculo: `01`, `02`, `03`
- Borde superior 2px: verde / rosa / rojo (`--error` para Reasignación)
- Fondo blanco, sombra botánica

---

## Patrón de Navegación

### Navbar global (todas las páginas)
Presente en `index.html`, `/acuerdo/`, `/realidad/`, `/fase2/` y también en las páginas de entrega (sin ítem activo en éstas últimas).

```html
<nav>
  <a href="/">Dashboard</a>
  <a href="/acuerdo/" class="active">Acuerdo</a>  <!-- active según la página -->
  <a href="/realidad/">Realidad</a>
  <a href="/fase2/">Fase 2</a>
</nav>
```

### Acceso a entregas (solo desde inicio)
Las cards de la sección de entregas en `index.html` son la **única entrada** a esas páginas. No hay link en el navbar ni en los footers de otras secciones.

```html
<!-- index.html — sección de entregas -->
<a href="/entregas/entrega-1/" class="delivery-card delivery-card--1">
  <span class="delivery-number">01</span>
  <h3>Acuerdo de Equipo</h3>
  <p>Compromisos de convivencia, canales de comunicación y protocolo de resolución.</p>
  <span class="delivery-cta">Ver entrega →</span>
</a>
```

### Página de entrega — navbar sin ítem activo
```html
<!-- /entregas/entrega-1/index.html -->
<nav>
  <a href="/">Dashboard</a>       <!-- ninguno marcado como active -->
  <a href="/acuerdo/">Acuerdo</a>
  <a href="/realidad/">Realidad</a>
  <a href="/fase2/">Fase 2</a>
</nav>
<!-- Opcionalmente: breadcrumb "Inicio → Entrega 1" para orientación -->
```

---

## Checklist de Implementación

### Fase 0 — Setup
- [ ] Instalar la skill [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) según su README
- [ ] Crear `assets/css/botanical.css` con las variables del design system
- [ ] Importar fuentes (Playfair Display + Hanken Grotesk) vía Google Fonts

### Fase 1 — Página principal
- [ ] Navbar sticky con glassmorphism
- [ ] Sección Hero
- [ ] Sección de entregas (3 cards navegables)
- [ ] Footer

### Fase 2 — Entrega 1: Acuerdo
- [ ] Hero "Acuerdo de Equipo & Gestión Humana"
- [ ] Sección 01: Compromisos de Armonía (card 2 cols + métricas + quote overlay)
- [ ] Sección 02: Canales de Fluidez (íconos + labels)
- [ ] Sección 03: Resolución Orgánica (2 cols + lista de pasos)
- [ ] Sección Protocolo de Integridad (3 sub-cards con borde de color)

### Fase 3 — Entregas 2 y 3
- [ ] Definir contenido de "Realidad" y "Fase 2"
- [ ] Replicar estructura de página con secciones propias

### Fase 4 — Calidad
- [ ] Responsivo mobile (< 768px): 1 columna, 16px márgenes
- [ ] Accesibilidad WCAG AA (contraste de texto sobre fondos pastel)
- [ ] Reduced-motion: desactivar transiciones si `prefers-reduced-motion`
- [ ] Focus visible en todos los elementos interactivos

---

## Notas para el Modelo (ui-ux-pro-max-skill)

Al generar cada página, referir siempre al archivo `diseño/DESIGN.md` para:

1. **Tokens de color** — no hardcodear hexadecimales, usar variables CSS
2. **Escala tipográfica** — `headline-xl / headline-lg / body-md / label-sm` según la jerarquía definida
3. **Sombras** — solo `box-shadow: 0 10px 30px rgba(168, 213, 186, 0.15)`, sin sombras oscuras
4. **Bordes** — sin bordes verticales en tablas; alternancia de filas con 1% tint verde
5. **Glassmorphism** — solo en navbar sticky y quotes overlay; `backdrop-filter: blur(12px)` + `opacity: 0.8`

---

*Plan generado el 26 de junio de 2026 — Aldea Global 2*
