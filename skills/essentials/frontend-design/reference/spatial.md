# Spatial & Layout Reference

This reference defines the spatial standards for the Universal Frontend & Design Brain.

## 1. The 4pt System
Use a **4pt base** for all spacing, layout, and rhythm.
- **Scale**: 4, 8, 12, 16, 24, 32, 48, 64, 96px.
- Use semantic tokens (`--space-sm`, `--space-md`) rather than pixel values.

## 2. Layout Principles
- **The Squint Test**: If you squint, the hierarchy should remain clear.
- **Grid Breaking**: Break the grid intentionally for emphasis. Use asymmetry and overlap.
- **Gap over Margin**: Use CSS `gap` for sibling spacing to eliminate margin collapse issues.
- **Container Queries**: Use `@container` for component-level responsiveness. Viewport queries are for page layout only.

## 3. Density & Rhythm
- **Varied Spacing**: Don't use the same padding everywhere. Tight groupings vs. generous separations create rhythm.
- **Negative Space**: Treat white space as a structural element, not an absence.
- **Character Limit**: Body text max-width: 65–75ch.

## 4. Anti-Patterns
- **Nested Cards**: Avoid wrapping everything in cards. Flatten the hierarchy.
- **Hero Metric Slop**: Avoid the "Big Number + Small Label + Gradient" template unless specifically required.
- **Centered Everything**: Left-aligned text often feels more "designed" and professional.
