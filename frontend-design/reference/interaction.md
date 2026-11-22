# Interaction Design Reference

This reference defines the interaction standards for the Universal Frontend & Design Brain.

## 1. Speed & Perception
- **Optimistic UI**: Update the UI immediately, sync in the background.
- **Instant Feedack**: Hover and active states must be fast (under 100ms).
- **Wait States**: Use skeleton screens or progressive loading for anything over 500ms.

## 2. Forms & Controls
- **Validation**: Validate on `blur`, not on every keystroke.
- **Touch Targets**: Minimum 44x44px.
- **Labels**: Always use semantic `<label>` elements. Never use placeholders as labels.

## 3. Hierarchy of Action
- **Specific CTAs**: Avoid "Submit" or "Click here". Use **Verb + Object** (e.g., "Create Project").
- **Button Hierarchy**: Use primary, secondary, and ghost buttons. Not every button is primary.
- **Progressive Disclosure**: Reveal advanced options only when needed.

## 4. Focus & Accessibility
- **Focus Outlines**: Never use `outline: none` without a custom replacement.
- **Empty States**: Use empty states to teach the user how to use the feature.
