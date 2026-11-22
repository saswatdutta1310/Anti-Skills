# Antigravity Design Module

Ported from `antigravity-design-expert`. Focuses on weightless, spatial, and highly interactive interfaces.

## 📐 Core Principles
- **Weightlessness**: Elements should appear to float. Use layered, soft, diffused drop-shadows.
    - Example: `box-shadow: 0 20px 40px rgba(0,0,0,0.05);`
- **Spatial Depth**: Utilize Z-axis layering. Use CSS `perspective` and `translateZ` to pop foreground elements.
- **Glassmorphism**: 
    - Subtle translucency.
    - Background blur: `backdrop-filter: blur(12px);`
    - Semi-transparent borders for a glassy edge.
- **Isometric Perspectives**: Use 3D transforms for dashboards/grids (e.g., `rotateX(60deg) rotateZ(-45deg)`).

## 🎬 Motion & Animation (The Butter Flow)
- **Zero-Latency Feel, Non-Instant**: Minimum `0.3s ease-out` for all state changes.
- **GSAP & ScrollTrigger**:
    - Elements should "float" into view on scroll.
    - Parallax: Move background slower than foreground.
- **Staggered Entrances**: Entrances should ripple (stagger by `0.1s`) rather than appearing at once.
- **Performance**: Use `will-change: transform` for GPU acceleration. Avoid animating `box-shadow` or `filter` continuously.

## 🛠 Implementation Snippets (Tailwind + CSS)
```css
/* Glassmorphism Utility */
.glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
}

/* Antigravity Hover */
.float-hover {
  transition: transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}
.float-hover:hover {
  transform: translateY(-10px) scale(1.02) rotateX(5deg);
}
```
