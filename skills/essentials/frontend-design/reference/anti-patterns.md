# Anti-Patterns (The Unified Index of "Sins")

These patterns are NEVER acceptable. They are the fingerprints of generic "AI Slop" or poor engineering.

## 🛑 Aesthetic Bans (The "Slop" Detector)
- **Side-Stripe Borders**: `border-left` as an accent. Use full borders or icons instead.
- **Gradient Text**: `background-clip: text`. Use bold weight or size for emphasis.
- **AI Color Tropes**: Cyan-on-dark, purple-to-blue gradients, neon glows. Use OKLCH neutrals.
- **Card Nesting**: Cards inside cards. Flatten the hierarchy.
- **Bounce Easing**: Elastic easing in productivity apps. Use smooth exponential deceleration.
- **Default Fonts**: Inter, Roboto, Arial. (See Typography Reference for replacements).

## 🛑 Mobile & Touch Sins
- **Tiny Targets**: Any touchable element smaller than 44px.
- **Gesture-Only Actions**: Actions that *only* work with a swipe/pinch (always provide button fallbacks).
- **Infinite Scroll Memory**: Never use a simple `map()` or `ScrollView` for long lists; use Virtualized lists.
- **Inline Rendering**: Inline functions in React `renderItem` (causes unnecessary re-renders).

## 🛑 Interaction & Feedback Sins
- **Instant Snapping**: State changes without transitions.
- **Emoji Icons**: Using 🎨 🚀 ⚙️ instead of professional SVG icons.
- **Guessing Logos**: Using generic text for brand logos. Use verified SVGs from Simple Icons.
- **Layout Shifting Hovers**: Hover states that change `scale` or `width` and move neighboring elements.
- **Ghost Clickables**: Clickable elements without `cursor-pointer`.

## 🛑 Performance & Security Sins
- **JS-Thread Animations**: Heavy animations not using `useNativeDriver` or GPU acceleration (`transform`/`opacity`).
- **Hardcoded Secrets**: `.env` variables or API keys in the client bundle.
- **PII Logging**: Logging sensitive user data or tokens in production.
