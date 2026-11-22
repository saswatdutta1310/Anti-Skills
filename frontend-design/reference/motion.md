# Motion Design Reference

This reference defines the motion standards for the Universal Frontend & Design Brain, merging high-craft deceleration with designer-weighted perspectives.

## 1. Weighted Perspectives
Select a primary designer lens based on the project context:

| Context | Primary | Philosophy |
|---------|---------|------------|
| **Productivity Tool** | Emil Kowalski | **Restraint & Speed**. Under 300ms. No bounce. |
| **Consumer App** | Jakub Krehel | **Production Polish**. 200-500ms. Blur & Y-offset. |
| **Creative/Portfolio** | Jhey Tompkins | **Experimentation**. Scroll-driven, playful. |

## 2. Technical Rules (Non-Negotiable)
- **Transform & Opacity Only**: Never animate `width`, `height`, `padding`, or `margin`.
- **No Bounce/Elastic**: Real objects decelerate smoothly. Use `cubic-bezier(0.16, 1, 0.3, 1)` or `ease-out-quint`.
- **Exit Strategy**: Exits must be 75% faster and subtler than entrances.
- **Instant Shortcuts**: Actions triggered by keyboard shortcuts must be INSTANT (no animation).
- **Reduced Motion**: All motion must be wrapped in `@media (prefers-reduced-motion: no-preference)`.

## 3. Recipes
### The "Jakub" Entrance
```jsx
initial={{ opacity: 0, translateY: 8, filter: "blur(4px)" }}
animate={{ opacity: 1, translateY: 0, filter: "blur(0px)" }}
transition={{ type: "spring", duration: 0.45, bounce: 0 }}
```

### Motion Gaps
Look for "snapping" UI. If it appears or disappears instantly, it's a gap.
- Use `AnimatePresence` (Framer Motion) for conditional renders.
- Use `grid-template-rows` transitions for height animations.

## 4. The Golden Rule
> "The best animation is that which goes unnoticed."
If the user notices the animation before the content, it is too prominent (unless the goal is pure delight).
