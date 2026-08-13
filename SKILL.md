---
name: photo-to-claymation-shot
description: Transform an uploaded portrait or character photo into an Aardman-style claymation cinematic still by first analyzing the photo through the S/W/I/F/T/P/M framework, then generating a handcrafted miniature stop-motion movie shot and delivering both an original-plus-result comparison image and a movie-spec cinematic matte frame. Use when the user provides a person photo and asks for clay animation, Aardman style, stop-motion film still, claymation character, SWIFTPM-based image prompt/design, original-plus-result comparison delivery, or movie-spec 16:9/4:3 black-bar framing.
version: 1.0.1
---

# Photo To Claymation Shot

Turn one person photo into a claymation-style cinematic image prompt or generated image. Do not merely apply a surface filter; extract the person's recognizable visual facts, then rebuild them as a handmade clay character inside a miniature stop-motion film world. When delivering an image result, generate one primary 16:9 cinematic claymation shot, then derive both finished files from that same shot: an original-photo-plus-result comparison image and a cinematic matte frame.

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
7. For image delivery, generate one true 16:9 horizontal cinematic claymation shot as the primary effect source. Do not generate a separate same-framing portrait effect image unless the user explicitly asks for one.
8. Produce the requested output:
   - If the user asks for a prompt, output the photo breakdown and the final S/W/I/F/T/P/M prompt.
   - If the user asks for an image, internally perform the breakdown, generate the primary 16:9 cinematic claymation shot, then deliver both required image artifacts from that same shot: the comparison image and the cinematic matte frame.
   - If the user explicitly asks for only one artifact, honor that narrower request.

## Required Image Deliverables

For image-generation tasks, deliver these two files unless the user explicitly narrows the request:

1. **Comparison image**: original photo plus claymation result in one clean before/after composition.
2. **Cinematic matte frame**: a movie-spec claymation still with a 16:9 active picture placed inside a 4:3 black-bar canvas.

The comparison image and cinematic matte frame must use the same primary 16:9 cinematic claymation shot. The comparison's result side is a scale/crop derivative of the 16:9 shot, matched to the original photo's subject size and position. Keep the standalone 16:9 active cinematic picture as a source artifact when useful for future edits, but do not treat it as a primary delivery unless requested.

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

For direct image generation, explicitly request a true 16:9 horizontal cinematic shot. The result side of the comparison is produced later by scaling and cropping this 16:9 shot to the cleaned source photo's dimensions.

## Image Delivery Composition

When producing the required comparison image, use this decision order:

1. Clean the source: crop useless border information from the original photo first, including black bars, blank scan margins, app-preview padding, or solid non-photo edges.
2. Choose one comparison mode:
   - **Mode B - cinematic comparison**: default for this skill. Use the primary 16:9 cinematic claymation shot, then scale/crop it for comparison.
   - **Mode A - same-framing comparison**: use only when the user explicitly asks for a faithful same-framing conversion instead of the default cinematic-shot workflow.
3. Choose the join direction from the cleaned source image:
   - landscape: stack original and result vertically
   - portrait: place original and result side by side horizontally
   - square: stack original and result vertically
4. Make both sections identical in width and height before joining.

Mode A sizing:

- Use only when the user explicitly asks for a same-framing conversion.
- Keep the original photo faithful in one section. Permit only proportional scaling or a slight crop needed to match the comparison layout.
- Resize/crop the generated result to the cleaned source dimensions, then compose.

Mode B sizing:

- Do not blindly center-crop either side. Align the two images like Photoshop layers: mark the visible person/core-subject bounding box in each image, temporarily think of them as overlaid at partial opacity, scale one side proportionally until the core subject height matches, align the important body anchors, then crop both sections to the same cleaned source dimensions.
- Decide which side is the visual scale target:
  - If the user wants to show faithful conversion, scale/crop the cinematic image to match the source subject.
  - If the user wants to show the cinematic shot as the target, enlarge/crop the source photo to match the cinematic subject scale and position. This is the default when a standalone cinematic frame has already been approved or requested.
- Preserve body evidence when choosing anchors. Use face center, head top, chin, shoulders, waist, hands, bag, strap, and ground contact. If lower body, waist, bag, strap, hands, or ground contact are important, keep the lower-body or lower-left anchor stable and remove extra area from the top/right as needed. Do not crop away the waist, hands, bag, or other body cues needed for comparison.
- Never include the 4:3 black-bar cinematic frame in a comparison image. Use the 16:9 active cinematic picture, and crop/scale from that active picture only.

- Join the two sections directly with no labels, frame, drop shadow, collage tape, watermark, logo, or explanatory text unless the user requests labels.
- Return the combined comparison image as one of the two required final deliverables. Keep the standalone generated result as a source artifact when useful for future edits.

Use [scripts/compose_comparison.py](scripts/compose_comparison.py) for deterministic composition when local image paths are available.

## Cinematic Matte Frame

Produce this as the second required image deliverable for image-generation tasks.

- Do not create this by cropping the comparison result or a portrait-format generated still.
- First generate the primary 16:9 cinematic shot that preserves the source person's recognition cues while extending or redesigning the environment as a movie scene.
- Read [references/cinematic-shot-design.md](references/cinematic-shot-design.md) before writing or generating a cinematic-frame prompt.
- Place the 16:9 active picture inside a 4:3 final canvas with black bars above and below.
- Default final canvas: `1440 x 1080`; default active picture: `1440 x 810`; top and bottom bars: `135 px` each.
- For higher-resolution delivery, use another 4:3 canvas while preserving the same math, for example `1920 x 1440` with a `1920 x 1080` active picture.
- Keep the active picture free of text, logos, watermarks, and fake lettering.
- The cinematic matte frame is a display deliverable, not the source image for before/after comparison. The comparison must use the same 16:9 active cinematic picture before black bars are added.
- Crop/scale the 16:9 active cinematic picture to the cleaned source dimensions while preserving the person's size and position as closely as possible. Use visual anchors such as face center, head height, torso position, hands, and crossbody straps rather than simple center-crop.

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
