---
name: photo-to-claymation-shot
description: Transform an uploaded portrait or character photo into an Aardman-style claymation cinematic still by first analyzing the photo through the S/W/I/F/T/P/M framework, then generating a handcrafted miniature stop-motion movie shot and, for image delivery, composing before/after comparison and optional cinematic-matte frame deliverables. Use when the user provides a person photo and asks for clay animation, Aardman style, stop-motion film still, claymation character, SWIFTPM-based image prompt/design, original-plus-result comparison delivery, or movie-spec 16:9/4:3 black-bar framing.
---

# Photo To Claymation Shot

Turn one person photo into a claymation-style cinematic image prompt or generated image. Do not merely apply a surface filter; extract the person's recognizable visual facts, then rebuild them as a handmade clay character inside a miniature stop-motion film world. When delivering an image result, compose the original photo and the generated claymation still into one finished comparison image, and create a cinematic matte frame when requested or useful for presentation.

## When To Use

Use this skill when the user provides or references a person photo and asks to:

- make an Aardman-style, claymation, stop-motion, or clay character version
- create a cinematic still, animated film shot, miniature set image, or character portrait
- analyze the photo with S/W/I/F/T/P/M or SWIFTPM before producing an image prompt
- batch-generate claymation prompts from portraits or character references
- deliver an original-photo-plus-claymation-result comparison image
- deliver a movie-spec cinematic frame with a 16:9 image area inside a 4:3 black-bar canvas

## Workflow

1. Inspect the photo and identify the person's core recognition cues: hairstyle, face shape, expression, posture, clothing, accessories, age impression, and any important props.
2. Analyze the photo with S/W/I/F/T/P/M. Use [references/swiftpm-framework.md](references/swiftpm-framework.md) when the task asks for explicit breakdown, prompt writing, or batch production.
3. Decide what must be preserved so the result remains traceable to the source person while becoming a clay character.
4. Rebuild the subject as a handcrafted clay figure: rounded forms, expressive but respectful features, visible fingerprints, slight asymmetry, and softened clay clothing details.
5. Rebuild or infer the world as a miniature set using the source photo's background, role, mood, or story. If the source background is private, messy, or irrelevant, simplify it into an emotionally consistent handcrafted set.
6. Before image generation, remove useless border information from the source photo, such as black bars, blank scan margins, solid app-preview padding, or obvious non-photo edges. Do not crop meaningful subjects, hands, faces, clothing, props, or scene context.
7. Inspect the cleaned source image pixel dimensions and use the same width, height, and aspect ratio as the target dimensions for the generated claymation still.
8. Produce the requested output:
   - If the user asks for a prompt, output the photo breakdown and the final S/W/I/F/T/P/M prompt.
   - If the user asks for an image, internally perform the breakdown, generate the claymation still, then compose the original photo and generated still into one finished comparison image unless the user explicitly asks for the effect image only.
   - If the user asks for a cinematic, movie-spec, poster-like, film-frame, or presentation-ready image, generate a separate 16:9 cinematic shot first, then create a cinematic matte frame from that shot.

## Output Formats

For prompt-only tasks, use:

```text
照片拆解：
S：
W：
I：
F：
T：
P：
M：

最终文生图提示词：
S（主体）：
W（世界）：
I（意图）：
F（形式）：
T（时间）：
P（感知）：
M（媒介）：
```

For direct image generation, include all relevant visual constraints from the final S/W/I/F/T/P/M prompt in the image-generation prompt. Do not include visible text, logos, watermarks, or fake lettering unless the user explicitly requests them.

For direct image generation, explicitly set or request the generated claymation still at the cleaned source photo's exact pixel dimensions whenever the image tool supports size control. If exact pixel control is unavailable, preserve the same aspect ratio and closest available resolution, then resize the generated still to the cleaned source photo's exact pixel dimensions before comparison composition.

## Image Delivery Composition

When the user asks for an image result, deliver one combined comparison image by default. Use this decision order:

1. Clean the source: crop useless border information from the original photo first, including black bars, blank scan margins, app-preview padding, or solid non-photo edges.
2. Choose one comparison mode:
   - **Mode A - same-framing comparison**: use when the generated claymation still preserves the source photo's framing family: similar shot distance, subject scale, body crop, and main subject position. This is the default mode for ordinary photo-to-claymation delivery.
   - **Mode B - cinematic comparison**: use when comparing the source photo against a separately directed 16:9 cinematic shot, or when the result intentionally expands the environment, changes focal length, changes shot distance, or creates a film-still composition.
3. Choose the join direction from the cleaned source image:
   - landscape: stack original and result vertically
   - portrait: place original and result side by side horizontally
   - square: stack original and result vertically
4. Make both sections identical in width and height before joining.

Mode A sizing:

- Keep the original photo faithful in one section. Permit only proportional scaling or a slight crop needed to match the comparison layout.
- Resize/crop the generated result to the cleaned source dimensions, then compose.

Mode B sizing:

- Do not blindly center-crop either side. Align the two images like Photoshop layers: mark the visible person/core-subject bounding box in each image, temporarily think of them as overlaid at partial opacity, scale one side proportionally until the core subject height matches, align the important body anchors, then crop both sections to the same cleaned source dimensions.
- Decide which side is the visual scale target:
  - If the user wants to show faithful conversion, scale/crop the cinematic image to match the source subject.
  - If the user wants to show the cinematic shot as the target, enlarge/crop the source photo to match the cinematic subject scale and position. This is the default when a standalone cinematic frame has already been approved or requested.
- Preserve body evidence when choosing anchors. Use face center, head top, chin, shoulders, waist, hands, bag, strap, and ground contact. If lower body, waist, bag, strap, hands, or ground contact are important, keep the lower-body or lower-left anchor stable and remove extra area from the top/right as needed. Do not crop away the waist, hands, bag, or other body cues needed for comparison.
- Never include the 4:3 black-bar cinematic frame in a comparison image. Use the 16:9 active cinematic picture if Mode B is chosen.

- Join the two sections directly with no labels, frame, drop shadow, collage tape, watermark, logo, or explanatory text unless the user requests labels.
- Return the combined comparison image as the final deliverable. Keep the standalone generated result as a source artifact when useful for future edits.

Use [scripts/compose_comparison.py](scripts/compose_comparison.py) for deterministic composition when local image paths are available.

## Cinematic Matte Frame

Use this as an additional deliverable when the user asks for a more cinematic, shareable, film-still, poster-like, or animation-movie-spec image.

- Do not create this by cropping the comparison result or a portrait-format generated still.
- First generate a separate 16:9 cinematic shot that preserves the source person's recognition cues while extending or redesigning the environment as a movie scene.
- Read [references/cinematic-shot-design.md](references/cinematic-shot-design.md) before writing or generating a cinematic-frame prompt.
- Place the 16:9 active picture inside a 4:3 final canvas with black bars above and below.
- Default final canvas: `1440 x 1080`; default active picture: `1440 x 810`; top and bottom bars: `135 px` each.
- For higher-resolution delivery, use another 4:3 canvas while preserving the same math, for example `1920 x 1440` with a `1920 x 1080` active picture.
- Keep the active picture free of text, logos, watermarks, and fake lettering.
- The cinematic matte frame is a display deliverable, not the source image for before/after comparison. Keep comparison composition based on the cleaned source photo dimensions.
- If the 16:9 active cinematic picture is used in a before/after comparison, crop/scale it to the cleaned source dimensions while preserving the person's size and position as closely as possible. Use visual anchors such as face center, head height, torso position, hands, and crossbody straps rather than simple center-crop.

Use [scripts/create_cinematic_frame.py](scripts/create_cinematic_frame.py) only for deterministic matte framing after a true 16:9 cinematic shot is available.

## Guardrails

- Preserve the person's recognizable traits; do not turn them into a generic clay character.
- Do not beautify, age-change, race-change, gender-change, or caricature the person in a cruel way unless explicitly requested.
- Rebuild the photo as a new stop-motion film still, not as a literal filter over the original image.
- Keep the result warm, handmade, cinematic, and slightly imperfect.
- For children's photos, keep the depiction wholesome, school-safe, and non-exploitative.
- If the photo includes private background details, simplify or anonymize the world while preserving the emotional tone.
- Avoid generated text inside the image. Prefer blank paper props, symbolic marks, or unreadable handmade shapes.

## Style Reference

Read [references/claymation-style-rules.md](references/claymation-style-rules.md) when the task needs a final image-generation prompt, style refinement, or troubleshooting of results that look too plastic, too generic, too realistic, or not handmade enough.
