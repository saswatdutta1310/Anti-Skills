# Unified Design Verification Checklists

Ported from `ui-ux-pro-max` and `web-design-guidelines`.

## 🎨 Visual Quality Audit
- [ ] **No Emoji Icons**: Use Lucide/Heroicons SVGs only.
- [ ] **Consistent Iconography**: All icons from the same set and stroke weight.
- [ ] **Real Assets**: Verified brand logos (Simple Icons), no placeholders.
- [ ] **Layout Stability**: Hover states do not shift elements or cause layout jumps.
- [ ] **Contrast**: Minimum 4.5:1 for accessibility.
- [ ] **Safe Colors**: Use OKLCH or curated palettes; avoid `rgb(255, 0, 0)`.

## 🖱 Interaction & Feedback
- [ ] **Active Cursors**: All clickable elements have `cursor-pointer`.
- [ ] **Hover States**: Clear visual feedback (subtle lift, glow, or color shift).
- [ ] **Loading States**: Skeleton screens or animated spinners for async actions.
- [ ] **Zero-Latency Feel**: Animations between 150ms and 300ms.

## 📱 Responsive & Mobile
- [ ] **Thumb-Ready**: Navigation and primary CTAs in reachable zones.
- [ ] **Viewport Meta**: Proper scaling enabled.
- [ ] **Horizontal Scroll**: Eliminated on all device widths (375px to 1440px).
- [ ] **Readable Text**: Minimum 16px for body text on mobile.

## 🏗 Vercel/Modern Web Standards
- [ ] **Semantic HTML**: Proper `<header>`, `<main>`, `<footer>` tags.
- [ ] **Focus Rings**: Accessible keyboard navigation rings.
- [ ] **Performance**: 60fps animations via GPU-heavy properties (transform/opacity).
