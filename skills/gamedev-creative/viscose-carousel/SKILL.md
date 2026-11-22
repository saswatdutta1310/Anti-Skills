---
name: viscose-carousel
description: Implement the Viscose Carousel technique using WebGL Signed Distance Fields (SDFs) to create fluid, melting, and threading card interactions. Use when designing non-standard, organic, fluid, or "gooey" portfolio carousels and interactive 3D UI components.
---

# Viscose Carousel Technique

The Viscose Carousel technique is a design approach for creating fluid, organic web interfaces—specifically portfolio carousels—where elements do not just separate or fade, but "melt" and pull apart like honey or a viscous fluid. This is achieved by rendering the entire carousel as a single WebGL fragment shader using Signed Distance Fields (SDFs) rather than independent DOM elements or 3D meshes.

## When to Use
Use this skill when tackling tasks that require:
- Fluid, organic, or "gooey" UI interactions.
- Complex element merging/separation effects that CSS filters (like blur + contrast) cannot achieve with high fidelity.
- Advanced WebGL/Three.js shader architecture for full-screen UI components.
- Portfolio sites aiming for highly unique, physics-inspired visual interactions.

## Core Concepts

### 1. The Single Fragment Shader Architecture
Elements (cards) are **not** independent img tags or Three.js Mesh objects.
- The entire scene is one full-screen rectangle running a single fragment shader.
- Every pixel calculates its distance to the nearest card using SDFs.
- **Texture Atlas:** All artwork lives in a single texture atlas. The fragment shader cannot index an array of samplers with a varying index (in ESSL 1.00), so coordinates are mapped to the correct cell in the atlas based on the card's position.

### 2. Smooth Minimum (smin) for Melting
To make shapes merge, you take the minimum of their distance functions. To make them melt or fuse, use a **smooth minimum**.
`glsl
// GLSL snippet for smooth minimum
float smin(float a, float b, float k) {
    float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}
`
- The k value sets the "gooeyness" (blend strength).
- Neighboring elements automatically swell into a fillet and fuse into a continuous surface when close.

### 3. Modelling the "Honey" Thread
Two cards drifting apart under smin alone will eventually just stop touching. To create a "snap" effect, the connecting thread is modeled as its own discrete swept shape between neighbors with four driven properties based on separation distance v (0 = touching, 1 = separated):
- **Width:** Falls off on a curve, thinning fast then lingering.
- **Pinch:** The middle narrows faster than the ends, creating the "neck".
- **Sag:** Droop grows with distance, making long threads hang.
- **Dissolve (Negative Radius):** Pushes the radius past zero near the end. This carries it out of antialiasing range so the thread breaks and snaps, rather than fading out like a hairline.

### 4. Cursor as a "Force", Not a Pointer
Nothing is drawn exactly at the cursor. The cursor is a disturbance in the SDF.
- **Hovering:** Raises k locally. The surface goes soft at the cursor, while staying stiff further out.
- **Reactions:** Nearest cards lean toward the cursor and swell. Neighbors back off and dim, making the hovered card read as "picked up". Threads stretch between the cards *around* the cursor, not *on* the cursor.
- **Asymmetric Rates:** Cards take up a lean quickly but let go slowly. This avoids feeling like a mechanical follow, and instead feels like dragging through a thick medium.

### 5. DOM Text Melting (The Same Trick, Twice)
For textual elements (like project years or disciplines) that need to melt but live in the DOM, the technique is replicated using CSS:
- Stack two copies of the text.
- Blur one out while blurring the other in.
- Apply a heavy alpha threshold (e.g., using SVG filters or high contrast) to the parent container.
- Two soft, blurred edges drifting past each other will cross the threshold and fuse into one sharp shape.
- *Note:* A word that isn't changing shouldn't melt. A static layer must be kept outside the filter to avoid unexpected thickening during the transition.

### 6. Refraction Lip (Glass Effect)
Create a glass refraction lip (like the rounded edge of a thick glass sheet) along screen boundaries by warping the ray coordinates (p) in the fragment shader before calculating the SDF. This bends both the planes and the honey threads together without requiring a second render pass or a render target.

## Implementation Architecture
- **Frameworks:** React (App Router), Three.js, GSAP (for momentum/spring animations), Tailwind CSS.
- **State Management:** JS drives the uniform arrays (positions, rotations, link distances) and sends them to the fragment shader.
