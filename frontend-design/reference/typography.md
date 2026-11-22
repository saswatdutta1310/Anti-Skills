# Typography Reference

This reference defines the typography standards for the Universal Frontend & Design Brain, merging principles from Impeccable and modern design systems.

## 1. Reflex Font Rejection List
Do NOT use these fonts. They are training-data defaults and create monoculture across projects.

- **Serif**: Fraunces, Newsreader, Lora, Crimson, Crimson Pro, Crimson Text, Playfair Display, Cormorant, Cormorant Garamond, Syne, Instrument Serif
- **Sans/Mono**: Inter, Roboto, Arial, Open Sans, IBM Plex Mono, IBM Plex Sans, Space Mono, Space Grotesk, DM Sans, Outfit, Plus Jakarta Sans, Instrument Sans

## 2. Font Selection Procedure
1. **Define Brand Voice**: Write down 3 concrete words (e.g., "warm and mechanical", "calm and clinical"). Avoid "modern" or "elegant".
2. **Reject Reflexes**: List the first 3 fonts you think of, then BAN them.
3. **Explore**: Search Google Fonts, ABC Dinamo, Velvetyne, etc., for a font that fits the brand as a *physical object*.
4. **Pairing**: Pair a distinctive **Display** font with a restrained **Body** font.

## 3. Technical Rules
- **Modular Scale**: Use at least a 1.25 ratio between steps.
- **Fluid Sizing**: Use `clamp()` for headings on marketing pages.
- **Line Length**: Cap at 65-75ch for readability.
- **Line Height**: Scales inversely with line length. Add 0.05-0.1 for light text on dark backgrounds.
- **Justification**: `text-align: justify` is strictly BANNED.

## 4. Hierarchy Patterns
- **Contrast over Size**: Use font-weight and letter-spacing to create hierarchy before increasing size.
- **Structural Type**: Use typography to define layout rhythm, not just as labels.
