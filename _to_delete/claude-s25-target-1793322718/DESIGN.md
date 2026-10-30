---
name: VATEK
description: Cold Jet 드라이아이스 세척 장비 공식 대리점 — 차가운 정밀함과 산업적 신뢰를 표현하는 디자인 시스템
colors:
  charcoal-navy: "#283739"
  void-navy: "#1b2426"
  dryice-teal: "#228896"
  teal-deep: "#1b6d78"
  teal-pale: "#e3f1f2"
  frost-white: "#f3f9fa"
  sublimation-ice: "#4fadb8"
  ice-deep: "#186973"
  vapor-pale: "#eaf6f7"
  chartreuse-mist: "#f3f7de"
  lime-accent: "#d8e58c"
  facility-gray: "#f5f5f5"
  steel-line: "#dfe3e3"
  graphite-body: "#46595b"
  slate-muted: "#6e8385"
  pure-white: "#ffffff"
  signal-red: "#c81e2c"
typography:
  display:
    fontFamily: "'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', -apple-system, BlinkMacSystemFont, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "clamp(34px, 4.6vw, 62px)"
    fontWeight: 800
    lineHeight: 1.16
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', -apple-system, BlinkMacSystemFont, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "clamp(28px, 3.6vw, 48px)"
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  body:
    fontFamily: "'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', -apple-system, BlinkMacSystemFont, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  label:
    fontFamily: "'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', -apple-system, BlinkMacSystemFont, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "13.5px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "2px"
rounded:
  sm: "8px"
  md: "12px"
  lg: "14px"
  xl: "16px"
  xxl: "20px"
  pill: "999px"
components:
  button-primary:
    backgroundColor: "{colors.teal-deep}"
    textColor: "{colors.pure-white}"
    rounded: "{rounded.lg}"
    padding: "12px 24px"
  button-primary-hover:
    backgroundColor: "{colors.dryice-teal}"
    textColor: "{colors.pure-white}"
    rounded: "{rounded.lg}"
    padding: "12px 24px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.dryice-teal}"
    rounded: "{rounded.lg}"
    padding: "12px 24px"
  button-secondary-hover:
    backgroundColor: "{colors.frost-white}"
    textColor: "{colors.dryice-teal}"
    rounded: "{rounded.lg}"
    padding: "12px 24px"
  badge-eyebrow:
    backgroundColor: "transparent"
    textColor: "{colors.dryice-teal}"
    padding: "0"
  card-default:
    backgroundColor: "{colors.pure-white}"
    textColor: "{colors.graphite-body}"
    rounded: "{rounded.lg}"
    padding: "24px 22px 20px"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.charcoal-navy}"
    padding: "27px 13px"
---

# Design System: VATEK

## Overview

**Creative North Star: "The Cold Precision Line"**

VATEK's visual world reads as controlled, engineered cold rather than consumer warmth: a deep charcoal-navy anchor, a single confident teal accent, and fluid, tightly-tracked headline type that scales with the viewport instead of jumping between breakpoints. The system deliberately runs on the visitor's own OS font (Malgun Gothic on Windows, falling through to Apple SD Gothic Neo on Mac) rather than a hosted webfont — a decision made explicitly after testing showed the hosted alternative rendered narrower and more cramped than the native system look the brand had already committed to. Nothing about the system chases trend or ornament; whitespace, a narrow color story, and a two-shade elevation habit (mostly flat, escalating only in response to interaction) do the work of feeling like an equipment vendor an engineer would trust with a six-figure purchase decision.

The aesthetic philosophy is **confident industrial calm**: cool teal and navy, generous whitespace, restrained motion. It projects reliability and competence, never excitement for its own sake — appropriate for a technical buyer comparing specs and support commitments, not being sold a mood.

**Key Characteristics:**
- Fluid `clamp()` typography instead of fixed per-breakpoint font sizes.
- One real accent color (dry-ice teal) carried in a tight family of tints/shades; navy is the dark anchor, not a second accent.
- OS-native sans-serif, deliberately not a hosted webfont.
- Flat-by-default cards with a whisper of shadow at rest, escalating on hover as tactile feedback.
- A single 14px corner radius used almost everywhere buttons, cards, and photos need softening — larger and smaller radii exist but are reserved for specific roles (pills, feature panels), not general use.

## Colors

The palette is a narrow, cool teal-and-navy story with two supporting families and one semantic outlier; it holds together because nearly everything on the site draws from one of these named roles rather than ad hoc hex values.

### Primary
- **Dry-Ice Teal** (`#228896`): the site's one true accent — CTA backgrounds, links, active nav states, eyebrow labels. Used sparingly and consistently so its appearance always means "act here."
- **Deep Industrial Teal** (`#1b6d78`): the darker end of the primary gradient and the resting state of `.cta-btn`; also used for hover-darkening text/border accents.
- **Pale Coolant Blue** (`#e3f1f2`): light teal wash for hover backgrounds on outline buttons and subtle section tints.
- **Frost White-Blue** (`#f3f9fa`): the palest teal tint, effectively an off-white with a cool cast, used for barely-there background separation.

### Secondary
- **Sublimation Ice-Blue** (`#4fadb8`): a cooler, lighter relative of the primary teal used for footer CTA emphasis (`.footer-btn.is-primary`) and focus rings — a secondary accent that reads as "ice" specifically, distinct from the more saturated brand teal.
- **Ice Shadow Teal** (`#186973`): the darker anchor of the ice family, used for a secondary eyebrow variant (`.cmp-eyebrow`) on internal product pages.
- **Vapor Pale** (`#eaf6f7`): the palest ice tint, parallel in role to Frost White-Blue but reserved for ice-family contexts.

### Tertiary
- **Chartreuse Mist** (`#f3f7de`) and **Lime Accent Line** (`#d8e58c`): a rare pale lime-green wash and its border/line partner. These are the only surviving trace of an earlier "lime green" palette ambition noted in the stylesheet's own header comment (`#A9C52F`) — that literal color was never actually implemented, but this softer mist/line pair is. Treat this family as a deliberately rare, low-saturation garnish, not a color to reach for by default.

### Neutral
- **Deep Charcoal Navy** (`#283739`): the dark anchor of the whole system — heading text color (`text-dark`), the base of dark hero/CTA backgrounds, and the ghost-button ink.
- **Void Navy** (`#1b2426`): the deepest dark, used for the darkest end of scroll-driven background transitions and dark floating panels.
- **Light Facility Gray** (`#f5f5f5`): the neutral page/section background alternative to white.
- **Steel Line Gray** (`#dfe3e3`): borders and hairline dividers, including the default card border and select-input borders.
- **Graphite Body** (`#46595b`): default body text color — never pure black.
- **Muted Slate** (`#6e8385`): secondary/caption text, de-emphasized copy.
- **Pure White** (`#ffffff`): card backgrounds, primary button text, page background.
- **Signal Red** (`#c81e2c`): the sole semantic/alert color, reserved for warnings or critical emphasis — never decorative.

### Named Rules
**The One Accent Rule.** Dry-Ice Teal is the only color that means "interactive" or "act now." Ice-Blue, Chartreuse Mist, and Signal Red each have one specific, narrow job (secondary emphasis, rare garnish, alert) and must not be reached for as general-purpose accents.

## Typography

**Display/Body Font:** "Malgun Gothic", "맑은 고딕", "Apple SD Gothic Neo" (with system-ui / -apple-system / "Segoe UI" / Roboto fallbacks) — one family for the whole system, differentiated by weight and size rather than a separate display face.

**Character:** Confident and slightly compressed at large sizes (tight `-0.02em` tracking on headlines gives them density and weight), open and readable at body size (1.6–1.75 line-height keeps long technical copy comfortable).

### Hierarchy
- **Display** (800, `clamp(34px, 4.6vw, 62px)`, line-height 1.16): hero `<h1>` only, set in white over a dark hero background, max-width constrained to ~780px so it never spans the full viewport.
- **Headline** (800, `clamp(28px, 3.6vw, 48px)`, line-height 1.25): section-level `<h2>` titles (`.section-head h2`), the system's primary rhythm-setter between page sections.
- **Title** (700): card and component-level `<h3>`/`<h4>` titles — a full step down in weight from headlines but still bold, never regular weight, so hierarchy reads even at small sizes.
- **Body** (400, 17px baseline, line-height 1.7; hero lead uses `clamp(16px, 1.3vw, 19px)` at 1.75): running copy and section descriptions (`.section-head p`), muted-slate colored for secondary body text.
- **Label** (800, 13.5px, letter-spacing 2px, uppercase): the `.eyebrow` pattern that precedes every section headline — teal-colored, always uppercase, always bold. A smaller sibling (11–12.5px, letter-spacing 1.5–3px) appears in nav/menu index labels and internal product-page eyebrows, following the same "small, bold, wide-tracked, teal-or-ice-colored" formula.

### Named Rules
**The Weight-Over-Size Rule.** Hierarchy is carried as much by font-weight (800 → 700 → 600 → 400) as by size. Nav links and lead-adjacent emphasis sit at 600; never drop a heading-level element to 400 just because its size is small — use the eyebrow/label pattern instead.

## Layout

The system is built on a 1160px max-width container (`--maxw`) with fluid, viewport-relative typography (`clamp()`) rather than distinct per-breakpoint type scales — headlines and body copy resize continuously as the viewport changes instead of jumping at fixed points. The primary structural breakpoint is 960px, where the header navigation collapses from an inline megamenu bar into a full-screen overlay behind a hamburger toggle (`.nav-toggle`, 40×40px, 8px radius). The header itself is fixed/sticky and hides on downward scroll (`.site-header.nav-hidden`) to reclaim vertical space on long pages, reappearing on scroll-up.

## Elevation & Depth

The system is **hybrid**: flat by default, but never zero — every card and table carries a whisper-quiet resting shadow (`--shadow-sm`, `0 2px 12px rgba(40,55,57,.07)`) rather than a hard flat edge, so surfaces always feel gently lifted off the page even at rest. Elevation then escalates in direct response to interaction: hovering a card or CTA steps up to the mid-tier `--shadow` (`0 10px 32px rgba(40,55,57,.10)`) or, for the most emphasized cards, the strongest `--shadow-lift` (`0 16px 40px rgba(40,55,57,.14)`), often paired with a small upward `translateY` — shadow depth is the site's primary tactile-feedback language. Separately, a handful of static elements (the hero photo, image galleries, dark floating CTA panels) use `--shadow` or `--shadow-lift` ambiently and permanently, signaling that they sit in their own visual layer above the page rather than reacting to the visitor.

### Shadow Vocabulary
- **Resting** (`box-shadow: 0 2px 12px rgba(40,55,57,.07)` — `--shadow-sm`): default state for nearly every card, table, and panel.
- **Responding** (`box-shadow: 0 10px 32px rgba(40,55,57,.10)` — `--shadow`): hover state for most cards; permanent ambient depth for hero photography and galleries.
- **Floating** (`box-shadow: 0 16px 40px rgba(40,55,57,.14)` — `--shadow-lift`): the strongest tier — hover state for the most emphasized cards (quote cards, feature sub-cards) and permanent depth for dark floating CTA panels.

### Named Rules
**The Always-Lifted Rule.** No card or table is ever perfectly flat — `--shadow-sm` is the floor, not an optional extra. Depth only ever increases from there; it never drops to zero on hover.

## Shapes

A single 14px radius (`--radius`) is the system's default corner language, applied to buttons, cards, and photos alike so the whole page reads as one consistent softness. Beyond that default, a small set of purpose-built radii exist: 8px for compact controls (the nav toggle, select inputs), 12px for a handful of secondary cards, 16px for a small set of larger product-solution cards, 20px for the biggest feature/detail panels (megamenu detail pane, gallery items, dark CTA-band sections), and 999px pill radius reserved for badges and small circular play/action buttons. Portrait imagery inside circular frames (`border-radius: 50%`) appears in a few icon-grid and avatar-style contexts. Borders, where present, are a consistent 1–1.5px hairline in Steel Line Gray or the relevant accent color — never heavier.

### Named Rules
**The One True Radius Rule.** 14px is the default answer for "what radius should this have." Reach for 8/12/16/20px or pill only when the component has a specific, established role that calls for it — don't introduce a new radius value for a one-off component.

## Components

Buttons and cards share the same "tactile and confident" character: solid, dependable shapes that give clear, immediate feedback the moment you interact with them, never fussy or over-decorated.

### Buttons
- **Shape:** 14px radius (`--radius`) on primary/secondary/ghost buttons; footer buttons use a slightly tighter 10px.
- **Primary** (`.cta-btn`): `background: linear-gradient(135deg, #228896 0%, #1b6d78 100%)`; white text; `padding: 12px 24px`; `font-weight: 700`; `font-size: 15px`; `letter-spacing: 0.1px`; resting shadow `0 6px 16px rgba(27,109,120,.22)`.
- **Hover/Focus:** `filter: brightness(1.06)`, `transform: translateY(-1px)`, shadow deepens to `0 10px 22px rgba(27,109,120,.28)` — a confident, immediate lift rather than a slow fade.
- **Secondary/Outline** (`.cta-btn.outline`): transparent background, 1.5px Dry-Ice Teal border, teal text, no shadow at rest; hover fills the background with Frost White-Blue.
- **Ghost** (`.cmp-btn-ghost`): 1.5px Charcoal Navy border, navy text, 16px font-size, 700 weight; hover inverts to a solid navy fill with white text.

### Cards / Containers
- **Corner Style:** 12–16px depending on role (see Shapes); 14px is the default.
- **Background:** Pure White.
- **Border:** 1px Steel Line Gray hairline.
- **Shadow Strategy:** resting `--shadow-sm`, escalating to `--shadow` or `--shadow-lift` on hover, frequently paired with a small `translateY` lift (see Elevation & Depth).
- **Internal Padding:** roughly `24px 22px 20px` for content cards (quote cards, feature cards).

### Inputs / Fields
- **Style:** `select` controls use a 1.5px Steel Line Gray border, 8px radius, bold 13.5px navy text; no plain text-input styling exists yet in the shared stylesheet (application forms are the only place selects currently appear).
- **Focus:** a checkbox/label focus-visible pattern uses a 2px Sublimation Ice-Blue outline with 2px offset — the ice-blue secondary color's clearest functional role in the system.
- **Disabled:** `opacity: .45`.

### Navigation
- **Style:** fixed/sticky header, hides on scroll-down and reappears on scroll-up. Top-level links use 15.5px/600-weight Charcoal Navy text with 27px/13px padding.
- **Active/Hover:** a 2px underline bar scales in from 0 to full width on hover (`::after`, `transform: scaleX()`); the active page instead shows a small 4px dot indicator when not being hovered.
- **Megamenu:** a rich dropdown panel (intro copy + indexed link list + live image preview + detail pane) opens beneath top-level items on hover, using the same eyebrow/label and card-radius language as the rest of the system.
- **Mobile:** below 960px, the nav becomes a full-screen fixed overlay (`inset: 76px 0 0 0`) triggered by a 40×40px, 8px-radius hamburger toggle.

## Do's and Don'ts

### Do:
- **Do** use Dry-Ice Teal as the only color that signals "interactive/primary action" — reserve Ice-Blue, Chartreuse Mist, and Signal Red for their one specific narrow role each.
- **Do** default every card, button, and photo to the 14px radius unless the component has an established reason (badge, compact control, feature panel) for a different value.
- **Do** give every card a resting `--shadow-sm` — never a perfectly flat, shadowless surface.
- **Do** carry hierarchy through font-weight (800/700/600/400) as much as through size, especially at small sizes where an eyebrow label substitutes for a heading.
- **Do** let the OS-native sans-serif render as-is; it was deliberately chosen over a hosted webfont after direct comparison.

### Don't:
- **Don't** introduce a second saturated accent color alongside Dry-Ice Teal — the system's confidence comes from having exactly one.
- **Don't** use the abandoned lime-green (`#A9C52F`) literal color; the only implemented trace of that palette direction is the softer Chartreuse Mist / Lime Accent Line pair.
- **Don't** fade shadows to zero on hover — depth only increases from the `--shadow-sm` floor.
- **Don't** fabricate certifications, facility details, or addresses on Company pages where the source content is explicitly marked as pending (`company/location.html`, `company/facility.html`) — see PRODUCT.md.
