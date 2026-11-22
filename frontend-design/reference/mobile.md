# Mobile & Touch-First Design Module

Ported from `mobile-design`. Focuses on the reality of mobile usage: distracted, one-handed, and low-battery.

## 📱 The Mobile Feasibility & Risk Index (MFRI)
Score every mobile feature from -10 to +10.
- **Complexity (-)**: Deep gestures, heavy media, complex state.
- **Clarity (+)**: Platform defined, accessibility ready.
- **Score < 0**: Redesign required before code.

## 🖐️ Touch Psychology
- **Fitts’ Law**: Targets must be large enough for fingers, not just cursors.
- **The Thumb Zone**: Primary CTAs must be in the bottom/reachable area.
- **Minimum Target**: 44x44px (iOS) / 48x48px (Android).
- **No Hover**: Interactive states must be clear without hover (use press/active states).

## 🏛 Platform Specifics
| Element | iOS (SF Pro) | Android (Roboto) |
| :--- | :--- | :--- |
| **Back** | Edge Swipe | System Back Button |
| **Icons** | SF Symbols | Material Icons |
| **Sheets** | Bottom Sheet | Dialog / Full-page |

## 🚀 Performance Doctrine (Hard Bans)
- **Lists**: NEVER use `ScrollView` for long lists. Use `FlatList`, `FlashList`, or `ListView.builder`.
- **Renders**: Avoid inline `renderItem` functions (use `useCallback` + `memo`).
- **Animations**: Use Native Driver for 60fps. Avoid JS-thread animations.
- **Battery**: Use `const` widgets/components to avoid unnecessary rebuilds.

## 🔒 Security
- **Sensitive Data**: Never store tokens in `AsyncStorage` / `localStorage`. Use Keychain/SecureStore.
- **PII**: Strip logs in production.
