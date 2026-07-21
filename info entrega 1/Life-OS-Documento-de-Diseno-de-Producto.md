# Life OS — Documento de Diseño de Producto
### Un sistema operativo de vida para estudiantes-emprendedores de alto rendimiento

**Versión:** 1.0
**Equipo:** Product Manager · UX/UI Designer · Full Stack Engineer · Data Analyst · Especialista en Productividad
**Fecha:** Julio 2026

---

## 0. Resumen ejecutivo

Life OS no es un habit tracker. Es un **sistema de inteligencia personal** que convierte datos de comportamiento diario (hábitos, tiempo, sueño, energía, trabajo) en **decisiones**. La diferencia frente a Habitica, Loop, TickTick, Todoist o Notion es que esas herramientas *registran*; Life OS *interpreta*.

El producto se construye sobre tres pilares:

1. **Captura de fricción mínima** — registrar el día debe tomar менos de 60 segundos.
2. **Motor analítico** — correlaciones, tendencias, predicciones, Life Score.
3. **Voz de coach** — cada dato se traduce en lenguaje humano y accionable, no en tablas frías.

Está diseñado específicamente para tu contexto: estudiante universitario con 4 frentes activos — Universidad, Gimnasio, Dropshipping (en fase de construcción y búsqueda continua de producto) y Upwork (en fase de prospección de clientes, aún sin clientes activos) — más sueño y descanso como variables críticas de todo el sistema.

> **Nota de fase:** Dropshipping y Upwork no están en la misma etapa. La búsqueda de producto en Dropshipping es una actividad **permanente** (se sigue haciendo incluso con tienda activa), mientras que la prospección en Upwork es una fase de **arranque** que se transformará en trabajo facturable en cuanto consigas tu primer cliente. El sistema está diseñado para reflejar esto y evolucionar contigo sin perder histórico.

---

## 1. Arquitectura completa

### 1.1 Stack tecnológico propuesto

| Capa | Tecnología | Justificación |
|---|---|---|
| Frontend | **Next.js 15 (App Router) + React 19 + TypeScript** | SSR/streaming para dashboards rápidos, server components para reducir JS en cliente, ecosistema maduro, ideal para UI tipo Linear/Vercel. |
| Estilos / UI | **Tailwind CSS + shadcn/ui + Radix UI** | Permite el look "premium minimalista" (Notion/Linear/Arc) sin diseñar cada átomo desde cero; Radix da accesibilidad gratis. |
| Animaciones | **Framer Motion** | Transiciones suaves en cambios de vista, streaks, logros — clave para la sensación "premium". |
| Gráficos | **Recharts (gráficos estándar) + D3.js (heatmaps y radar personalizados) + Visx para calendarios de streaks** | Recharts cubre el 80% rápido; D3 se reserva para visualizaciones a medida (heatmap estilo GitHub, radar de balance de vida). |
| Backend | **Node.js + tRPC (o NestJS si prefieres arquitectura más formal)** | tRPC da tipado end-to-end con TypeScript, ideal para una app personal/mono-usuario donde la velocidad de iteración importa más que microservicios. |
| Base de datos | **PostgreSQL** (vía Supabase o Neon) | Datos altamente relacionales (hábitos, entradas diarias, objetivos, correlaciones) + soporte nativo para *time-series* con extensiones como TimescaleDB si el volumen crece. |
| ORM | **Prisma** | Migraciones tipadas, excelente DX, se integra perfecto con tRPC. |
| Autenticación | **Supabase Auth / Clerk** | Mono-usuario hoy, pero deja la puerta abierta a multiusuario (familia, coach, comunidad) sin reescribir nada. |
| Motor de IA / Analista | **API de Anthropic (Claude) vía backend**, con un pipeline de *function calling* que consulta la base de datos antes de responder | Claude actúa como "analista de datos", no como chatbot: recibe agregados (no todo el histórico crudo) y responde con lenguaje de coach. |
| Jobs programados | **Cron jobs (Vercel Cron / Supabase Edge Functions)** | Generación automática del informe semanal (domingos) y mensual (fin de mes), cálculo nocturno del Life Score. |
| Notificaciones | **Web Push API + (opcional) integración con Telegram/WhatsApp Bot** | Recordatorios inteligentes sin depender de que la app esté abierta. |
| Cache / tiempo real | **Redis (Upstash)** | Cache de cálculos pesados (correlaciones, promedios móviles) y estado en tiempo real del "streak actual". |
| Despliegue | **Vercel (frontend + edge functions) + Supabase/Neon (DB)** | Cero DevOps, autoescalado, ideal para un proyecto personal que puede crecer a producto público. |

**Por qué este stack y no otro:** prioriza velocidad de desarrollo para un producto que vive de iterar rápido sobre lo que realmente usas, mantiene todo tipado de punta a punta (menos bugs en cálculos críticos como el Life Score), y separa claramente "lo que se mide" (Postgres) de "lo que se interpreta" (capa de IA), que es exactamente la distinción conceptual que pediste entre tracker y sistema operativo de vida.

### 1.2 Arquitectura de alto nivel

```
┌─────────────────────────────────────────────────────────────┐
│  CLIENTE (Next.js — Web App + PWA instalable en móvil)        │
│  Dashboard · Hábitos · Tiempo · Objetivos · Stats · Calendario│
└───────────────────────┬─────────────────────────────────────┘
                         │ tRPC (typed API)
┌───────────────────────▼─────────────────────────────────────┐
│  BACKEND (Node.js)                                            │
│  ┌───────────────┐ ┌────────────────┐ ┌────────────────────┐ │
│  │ Habit Engine  │ │ Scoring Engine │ │ Insight Engine (IA) │ │
│  │ CRUD + streaks│ │ Life Score     │ │ Claude + análisis   │ │
│  └───────┬───────┘ └────────┬───────┘ └──────────┬──────────┘ │
│          │                  │                     │            │
│  ┌───────▼──────────────────▼─────────────────────▼─────────┐ │
│  │              Capa de datos (Prisma + PostgreSQL)          │ │
│  └────────────────────────────────────────────────────────────┘│
│  Cron: reporte semanal, reporte mensual, recálculo Life Score  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Modelo de datos

Entidades principales (simplificado, listo para traducir a schema de Prisma):

```
User
 ├── id, nombre, timezone, preferencias (tema, unidades, hora de reset del día)

Habit
 ├── id, nombre, categoría (Universidad/Gym/Dropshipping/Upwork/Sueño/Ocio/Salud)
 ├── subcategoría (opcional, ej. Dropshipping→Investigación de producto/Tienda-Ads; Upwork→Prospección/Portafolio)
 ├── tipo (booleano ✔/✘, parcial, numérico, duración)
 ├── frecuencia objetivo (diaria, X veces/semana, días específicos)
 ├── peso (impacto relativo en el Life Score, 1-10)
 ├── activo (bool), fecha_creación, orden_de_visualización

BusinessCategory (para Dropshipping y Upwork)
 ├── id, categoría, fase_actual (ej. "construcción", "prospección", "activo con clientes")
 ├── fecha_cambio_fase (permite ver en el histórico cuándo pasaste de una fase a otra)
 ├── hábitos_asociados (se ajustan automáticamente al cambiar de fase, sin perder histórico)

HabitEntry
 ├── id, habit_id, fecha, estado (completado/parcial/no completado)
 ├── nota (texto libre), valor_numérico (si aplica), hora_de_registro

TimeLog
 ├── id, categoría (Estudio/Dropshipping/Upwork/Gym/Ocio/Sueño), fecha
 ├── hora_inicio, hora_fin, duración_minutos, nota

SleepLog
 ├── id, fecha, hora_dormido, hora_despierto, duración, calidad_subjetiva (1-5)

Goal
 ├── id, título, tipo (diario/semanal/mensual/anual)
 ├── categoría, prioridad (alta/media/baja), fecha_límite
 ├── progreso (%), estado (no_iniciado/en_progreso/completado/fallido)
 ├── métrica_asociada (opcional: vincula a un Habit o TimeLog para autocálculo)

LifeScoreSnapshot
 ├── id, fecha, score_total (0-100)
 ├── subscores: {universidad, gym, dropshipping, upwork, sueño, balance}
 ├── factores_detectados (json: qué subió/bajó el score y por qué)

WeeklyReport / MonthlyReport
 ├── id, periodo, resumen_texto (generado por IA)
 ├── métricas_clave (json), comparación_periodo_anterior (json)
 ├── nivel_disciplina, nivel_consistencia, nivel_enfoque, riesgo_burnout, balance_vida_trabajo

Achievement / Badge
 ├── id, nombre, descripción, ícono, condición_desbloqueo
 ├── fecha_desbloqueo (null si aún no se logra)

UserLevel
 ├── nivel_actual, experiencia_actual, experiencia_siguiente_nivel
 ├── racha_actual, racha_máxima_histórica

Insight (generado por el motor de IA)
 ├── id, fecha, tipo (correlación/alerta/recomendación/predicción)
 ├── texto, confianza (%), datos_soporte (json), leído (bool)
```

**Relaciones clave:** `Habit 1—N HabitEntry`, `Goal N—1 Habit` (opcional), `LifeScoreSnapshot` se genera diariamente a partir de `HabitEntry + TimeLog + SleepLog` agregados, y los reportes semanales/mensuales se generan a partir de N `LifeScoreSnapshot`.

---

## 3. Funcionalidades detalladas

### 3.1 Dashboard principal

Estructura de la pantalla de inicio (lo primero que ves cada mañana/noche):

```
┌──────────────────────────────────────────────────────────┐
│  Buenos días · Miércoles 15 Julio          🔥 Racha: 12   │
│  "Ayer tu productividad subió 8% vs el promedio semanal"  │
├──────────────────────┬───────────────────────────────────┤
│   LIFE SCORE          │   Objetivos de hoy                │
│   ┌────────────┐      │   ☐ Dormir antes de las 22:30     │
│   │    78/100  │      │   ☐ Gimnasio                      │
│   │  ▲ +3 vs   │      │   ☐ 2h Dropshipping               │
│   │   ayer     │      │   ☐ Enviar 3 propuestas Upwork    │
│   └────────────┘      │   ☐ Estudiar 90 min               │
├──────────────────────┴───────────────────────────────────┤
│  Distribución del tiempo hoy (barra horizontal apilada)   │
│  ██ Universidad  ██ Gym  ██ Dropship  ██ Upwork  ██ Ocio  │
├──────────────────────┬───────────────────────────────────┤
│  Semana en curso       │  Insight del día (IA)             │
│  L M X J V S D         │  "Tus últimas 3 semanas muestran  │
│  ✔ ✔ ✔ · · · ·         │  que duermes mejor los días que   │
│                        │  entrenas. Hoy no has registrado  │
│                        │  gimnasio — considera priorizarlo"│
└──────────────────────┴───────────────────────────────────┘
```

Muestra: resumen del día, objetivos diarios, estado semanal/mensual (barras de progreso compactas), nivel de productividad (derivado del Life Score de las últimas 24-72h), un mensaje motivacional contextual (no genérico — generado a partir de tus propios datos), y progreso general hacia objetivos anuales.

### 3.2 Seguimiento de hábitos

- Registro con un tap: ✔ / Parcial / ✘, más campo de nota opcional.
- Hábitos sugeridos preconfigurados para tu caso (los que listaste), pero totalmente personalizables (crear, archivar, reordenar, agrupar por categoría).
- Cada hábito tiene un **peso** configurable que alimenta el Life Score — no todos los hábitos importan igual (dormir antes de las 22:30 puede pesar más que "tomar agua").
- Vista de "Parcial" para hábitos no binarios (ej. "Estudié" puede ser parcial si estudiaste 20 min de los 90 planeados).

**Hábitos sugeridos para Dropshipping (fase construcción, actividad continua):**
- Investigación de producto (tiempo dedicado, número de productos evaluados)
- Trabajo en tienda / ads / contenido
- Análisis de métricas (una vez haya tienda corriendo)

**Hábitos sugeridos para Upwork (fase prospección, sin clientes aún):**
- Propuestas enviadas (número, no solo sí/no)
- Portafolio actualizado / nuevas muestras agregadas
- Seguimiento a propuestas anteriores

Estos hábitos están marcados en el sistema como pertenecientes a una **fase**; cuando consigas tu primer cliente en Upwork, la app te sugerirá automáticamente agregar hábitos nuevos de fase "activo" (horas facturables, cumplimiento de deadlines) sin borrar ni resetear lo que ya veníamos midiendo.

### 3.3 Seguimiento del tiempo

- Time logging manual (botón de inicio/fin tipo Toggl) o registro retroactivo rápido ("¿cuánto tiempo dedicaste hoy a X?").
- Categorías fijas mapeadas a tus 4 frentes + sueño + ocio, con posibilidad de subcategorías (ej. Dropshipping → Investigación de producto / Ads / Atención al cliente).
- Gráficos automáticos: distribución diaria (dona), evolución semanal (barras apiladas), comparación semana vs semana anterior (líneas).

### 3.4 Sistema de objetivos

- Cuatro niveles: diario, semanal, mensual, anual, con jerarquía visual (un objetivo anual se puede desglosar en mensuales, esos en semanales).
- Cada objetivo: % de progreso (manual o autocalculado si está vinculado a un hábito/time log), fecha límite, prioridad, estado.
- Vista tipo Kanban opcional (No iniciado / En progreso / Completado / Fallido) además de la vista de lista.

### 3.5 Dashboard de estadísticas

Visualizaciones incluidas, cada una con su propósito:

| Visualización | Qué responde |
|---|---|
| Heatmap estilo GitHub (por hábito o global) | "¿Qué tan consistente he sido en los últimos 90 días?" |
| Radar chart de balance de vida | "¿Estoy descuidando alguna área frente a las demás?" |
| Calendario con código de color por Life Score diario | "¿Qué días del mes fueron mis mejores/peores?" |
| Gráfico de rachas (streaks) | "¿Cuál es mi racha actual y mi récord histórico?" |
| Líneas de tendencia (Life Score, sueño, horas por categoría) | "¿Voy mejorando o empeorando en el tiempo?" |
| Distribución del tiempo (dona/barras apiladas) | "¿En qué se me va el tiempo realmente?" |
| Productividad por hora del día (heatmap horizontal) | "¿Cuál es mi horario de mayor rendimiento?" |
| Productividad por día de la semana (barras) | "¿Qué días rindo más/menos?" |
| Promedios móviles (7 y 30 días) | "¿Cuál es mi tendencia real, sin el ruido de un mal día?" |
| Comparación semana vs semana / mes vs mes | "¿Mejoré o empeoré respecto al periodo anterior?" |
| Matriz de correlaciones | "¿Qué hábitos se relacionan entre sí?" |

**Motor de correlaciones (cómo funciona):** cada noche, un job calcula el coeficiente de correlación de Pearson entre pares de variables numéricas (horas de sueño, horas de gimnasio, horas de trabajo profundo, Life Score del día siguiente, etc.) sobre ventanas móviles de 30/60/90 días. Solo se muestran correlaciones con |r| > 0.3 y un tamaño de muestra mínimo (para evitar conclusiones prematuras), presentadas siempre como *asociación*, no como causalidad garantizada — el lenguaje del insight usa "parece estar relacionado con" en vez de "causa".

### 3.6 Sistema de puntuación — Life Score

**Fórmula propuesta (0-100):**

```
Life Score = Σ (peso_categoría × desempeño_categoría) − penalizaciones + bonos

Categorías y peso sugerido (ajustable por ti):
  Universidad ........ 20%
  Gimnasio ............ 15%
  Dropshipping ........ 15%
  Upwork / Freelance .. 15%
  Sueño ............... 20%   ← mayor peso: es la variable que más correlaciona con todo lo demás
  Balance/ocio ........ 15%

desempeño_categoría (0-100) se calcula como:
  promedio ponderado de (hábitos completados de esa categoría × su peso individual)
  + cumplimiento de horas objetivo (si definiste horas meta para esa categoría)

  Nota sobre Dropshipping y Upwork, dado que aún no generan ingresos:
  el desempeño de estas dos categorías se mide 100% por ACTIVIDAD
  (horas invertidas, propuestas enviadas, productos investigados),
  no por resultados económicos. Esto evita que el score caiga solo
  porque "todavía no hay ventas/clientes" — lo que se premia es la
  consistencia del esfuerzo, no un resultado que aún no depende
  únicamente de ti. Cuando Upwork pase a "fase activa" (con clientes),
  el desempeño podrá incorporar métricas de resultado sin perder
  comparabilidad con el histórico de actividad.

Penalizaciones:
  - Racha rota en hábito de alto peso: -3 a -8 puntos (según peso del hábito)
  - Dormir menos de X horas definidas por ti: -5 puntos ese día
  - 3+ días consecutivos sin actividad en un frente prioritario: alerta + -2/día

Bonos:
  - Racha activa (streak) ≥ 7 días en un hábito: +2
  - Cumplir el 100% de los objetivos del día: +5
  - Superar el promedio móvil de 30 días: +3
```

El Life Score se recalcula automáticamente cada noche y se guarda como snapshot histórico, lo que permite todas las comparaciones y tendencias. Es **transparente**: siempre puedes hacer clic en el número y ver el desglose exacto de qué subió o bajó el score ese día — nada de "caja negra".

### 3.7 Análisis semanal (automático, cada domingo)

Generado por el motor de IA a partir de los agregados de la semana (no del texto crudo de tus notas, por privacidad y eficiencia). Estructura del informe:

1. Resumen ejecutivo de la semana (2-3 líneas, tono coach)
2. Qué mejoró / qué empeoró (con números)
3. Hábitos que se están consolidando vs. hábitos en riesgo
4. Tiempo invertido por área + comparación con la semana anterior
5. Predicción de la próxima semana basada en tendencia actual
6. 2-3 consejos accionables y específicos (no genéricos)
7. Indicadores cualitativos: nivel de disciplina, consistencia, enfoque, riesgo de burnout, balance vida/trabajo — cada uno como una escala (Bajo/Medio/Alto) con la evidencia numérica detrás

### 3.8 Análisis mensual

Versión ampliada del semanal: tendencias de 4-5 semanas, gráfico de progreso hacia objetivos mensuales/anuales, objetivos alcanzados vs. incumplidos, comparación mes vs. mes anterior y vs. el mismo mes si hay histórico, y una sección de "predicción a 30 días" si continúas la tendencia actual.

### 3.9 Motor de IA — el "analista", no el chatbot

Diferencia clave de diseño: no es una ventana de chat abierta a cualquier pregunta. Es una **interfaz de preguntas frecuentes de analista** con respuestas basadas 100% en tus datos reales, más un campo de pregunta libre para casos no cubiertos.

Preguntas nativas (con UI dedicada, no solo texto):
- ¿Por qué bajó mi productividad esta semana? → compara snapshots y aísla la variable con mayor cambio
- ¿Qué hábito tiene más impacto en mi Life Score? → ranking por correlación + peso configurado
- ¿Qué debería mejorar esta semana? → identifica la categoría con peor desempeño relativo a su peso
- ¿Cuál es mi cuello de botella? → detecta el hábito/categoría con más incumplimientos recurrentes
- ¿Qué pasa si dejo el gimnasio? → simulación basada en la correlación histórica gym↔Life Score
- ¿Qué ocurre cuando duermo poco? → muestra el efecto histórico medido en tus propios datos
- ¿Cuál es mi mejor día de la semana? → agregación por día de semana

Bajo el capó: el backend arma un contexto agregado (JSON con snapshots, correlaciones, promedios) y se lo pasa a Claude vía API con un prompt de sistema que lo posiciona como analista cuantitativo, no como asistente conversacional genérico — así las respuestas son consistentes, basadas en evidencia y citando tus propios números.

### 3.10 Gamificación

- **Niveles y experiencia (XP):** cada hábito completado, objetivo cumplido o racha mantenida otorga XP; subir de nivel desbloquea temas visuales o funciones cosméticas (nunca funciones core, para no crear fricción de pago/progreso artificial).
- **Misiones semanales:** retos generados automáticamente ("Esta semana: 5 días de gimnasio" o "3 propuestas nuevas en Upwork").
- **Insignias:** por hitos (primera racha de 30 días, primer mes con Life Score >80, etc.)
- **Rachas (streaks):** por hábito individual y una racha "global" (días con Life Score sobre tu propio promedio).

Importante desde productividad real (Atomic Habits/GTD): la gamificación debe reforzar identidad ("soy alguien que entrena", no "gané puntos"), así que los logros están redactados en términos de identidad, no solo de números.

### 3.11 Calendario

Vistas semanal, mensual y anual unificando: hábitos completados (mini-indicadores de color), bloques de tiempo (time blocking real, estilo Google Calendar pero integrado con tus categorías), eventos puntuales (exámenes, entregas, citas) y rutinas recurrentes visualizadas como plantillas semanales editables.

### 3.12 Recordatorios inteligentes

No son alarmas fijas — son generados por reglas + datos:

- Basados en ausencia: "Llevas 3 días sin registrar Dropshipping"
- Basados en comparación: "Esta semana dormiste 2h menos que la anterior"
- Basados en patrón histórico: "Los miércoles a esta hora sueles entrenar — ¿vas hoy?"
- Basados en riesgo: "Tu racha de sueño está en riesgo, quedan 2 horas para tu hora límite"

---

## 4. Flujo de usuario (user flow) principal

```
Abrir app (mañana, 5:30-6:00 AM)
   → Dashboard: ver Life Score de ayer + insight del día
   → Revisar objetivos de hoy (auto-generados desde rutinas + metas activas)
   → Ir a clases (app en background, sin fricción)

Después de cada bloque del día
   → Registro rápido (1 tap por hábito completado, widget/notificación)
   → Time log de la actividad recién terminada (opcional, botón "iniciar/detener" si se usó en vivo)

Noche
   → Revisión rápida del día (checklist final, notas)
   → Registro de sueño planeado / hora de dormir
   → Job automático a medianoche: calcula Life Score del día, actualiza streaks, chequea logros

Domingo
   → Notificación: "Tu informe semanal está listo"
   → Usuario lee el reporte generado por IA → ajusta objetivos de la próxima semana

Fin de mes
   → Informe mensual + revisión de objetivos mensuales/anuales → replanificación
```

---

## 5. Diseño (dirección visual)

- **Filosofía:** espacio en blanco generoso, tipografía como protagonista (Inter o Geist), color usado con intención (no decorativo) — el color comunica estado (verde=on track, ámbar=en riesgo, rojo=atención), inspirado en la claridad de Linear y la calidez sutil del dashboard de Stripe.
- **Modo oscuro por defecto** (uso mayor de noche/madrugada), con modo claro igual de cuidado, no un simple invert de colores.
- **Micro-interacciones:** al marcar un hábito, una animación breve de confirmación (estilo "check" de Linear); al subir el Life Score, una animación sutil de conteo ascendente; los streaks tienen una llama animada que crece con la racha.
- **Densidad de información alta pero jerárquica:** el dashboard principal muestra lo esencial; el detalle vive un clic más adentro (evita el error de Notion de sentirse "vacío" o el de Habitica de sentirse "infantil").
- Totalmente **responsive**, con PWA instalable para que el registro rápido se sienta nativo en el móvil (crítico porque la mayoría de registros ocurrirán entre clases o en el gimnasio).

---

## 6. Roadmap de desarrollo por fases

**Fase 0 — Fundamentos (semana 1-2)**
Setup del proyecto (Next.js + Prisma + Postgres), autenticación, modelo de datos base, CRUD de hábitos y entradas diarias.

**Fase 1 — MVP funcional (semana 3-5)**
Dashboard principal, registro de hábitos y tiempo, calendario básico, cálculo simple del Life Score (sin IA todavía), modo claro/oscuro.

**Fase 2 — Estadísticas (semana 6-8)**
Todas las visualizaciones (heatmap, radar, tendencias, comparaciones), sistema de objetivos completo (4 niveles), promedios móviles.

**Fase 3 — Inteligencia (semana 9-11)**
Integración con Claude para el motor de análisis, generación automática de informes semanales/mensuales, motor de correlaciones, preguntas nativas del analista.

**Fase 4 — Gamificación y hábito de uso (semana 12-13)**
Niveles, XP, insignias, misiones semanales, recordatorios inteligentes, notificaciones push.

**Fase 5 — Pulido y PWA (semana 14-15)**
Optimización de performance, animaciones finales, instalabilidad PWA, onboarding guiado.

**Fase 6 — Futuro (post-lanzamiento personal)**
Ver sección 7.

---

## 7. Futuras funcionalidades (post-MVP)

- **Integraciones:** Google Calendar (bidireccional), Toggl/RescueTime (import automático de tiempo), Apple Health/Google Fit (sueño y ejercicio automáticos, eliminando registro manual).
- **Modo equipo/accountability:** compartir un resumen (no los datos crudos) con un amigo/mentor para rendición de cuentas.
- **Exportación de datos:** CSV/PDF de cualquier periodo, para análisis externo o respaldo.
- **App de IA proactiva:** notificaciones predictivas ("basado en tu patrón, hoy tienes alto riesgo de saltarte el gimnasio a las 16:00 — bloquéalo ahora").
- **Modo "temporada":** periodos configurables (ej. "temporada de exámenes") donde el Life Score y los pesos se ajustan automáticamente a prioridades temporales sin perder el histórico comparable.
- **Voz/atajos rápidos:** registro por comando de voz o atajos de teclado (Raycast-style) para reducir aún más la fricción de registro.

---

## 8. Por qué esto supera a las alternativas existentes

- **Habitica:** gamifica pero no analiza — no correlaciona sueño con productividad ni genera informes tipo coach.
- **Loop Habit Tracker:** solo streaks y gráficos básicos, cero inteligencia ni objetivos jerárquicos.
- **TickTick/Todoist:** excelentes para tareas, pero no entienden hábitos como sistema ni calculan un score de vida integrado.
- **Notion:** infinitamente flexible pero requiere que tú construyas y mantengas toda la lógica; aquí la lógica de análisis viene incorporada y automatizada.

Life OS ocupa el espacio que ninguna de ellas cubre: la intersección entre *seguimiento de hábitos*, *gestión de objetivos* y *análisis de datos personal con IA*, diseñado específicamente alrededor de tus 4 frentes reales y tu restricción más importante — el sueño — como eje central del sistema.

---

*Siguiente paso sugerido: validar contigo los pesos del Life Score y la lista definitiva de hábitos/categorías antes de pasar a la Fase 0 de desarrollo.*
