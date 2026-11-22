# Color & Contrast Reference

This reference defines the color standards for the Universal Frontend & Design Brain, prioritizing perceptual uniformity and brand cohesion.

## 1. OKLCH over HSL
Always use **OKLCH** for color definitions. It is perceptually uniform, meaning equal steps in lightness *look* equal.

```css
/* Pattern: oklch(L C H) */
--brand-primary: oklch(0.6 0.18 250);
```

- **Saturation Control**: As you move toward white or black, REDUCE chroma. Light colors at high chroma look garish.

## 2. Tinted Neutrals
**Pure Gray is Dead.** Never use #000, #888, or #FFF.
- Tint neutrals toward the brand's primary hue.
- Chroma range: 0.005–0.015.
- This creates subconscious cohesion between brand colors and UI surfaces.

## 3. The 60-30-10 Rule
Distribute color by visual weight, not pixel count:
- **60%**: Neutral / Surface
- **30%**: Secondary text, borders, and UI elements
- **10%**: Sharp accents (use sparingly for maximum power)

## 4. Accessibility & Contrast
- **Gray on Color**: Never use gray text on colored backgrounds. Use a darkened/lightened shade of the background hue instead.
- **Dark Mode**: Do not default to "cool" glowing accents. Theme selection must be derived from audience context (e.g., DEX = dark, Hospital = light).
- **Text Contrast**: Use a high-contrast dark gray instead of pure #000 for body text to reduce eye strain.
