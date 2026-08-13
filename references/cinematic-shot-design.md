# Cinematic Shot Design

Use this reference when creating the optional movie-spec deliverable. The cinematic frame must be designed as a new 16:9 film shot, not cropped from the portrait comparison image.

## Core Rule

The comparison image preserves the source photo's framing. The cinematic shot re-directs the scene for film.

Keep the person's identity cues, relationships, pose logic, and emotional truth, but expand the world, camera, lens, light, and composition so the result feels like a still from a stop-motion animated movie.

## Design Steps

1. Preserve the source facts:
   - number of people
   - relative positions and relationship
   - hairstyle, face shape, expression, posture, clothing, accessories
   - important props and scene identifiers
   - emotional tone
2. Choose a cinematic shot type:
   - full-body wide shot for environmental memory
   - medium wide shot for character relationship
   - medium shot for warm portrait drama
   - close-up only when the source photo is already face-focused
3. Choose lens language:
   - `35mm` for environmental storytelling and wider space
   - `50mm` for natural portrait distance and memory scenes
   - `85mm` for intimate portraits with stronger background compression
4. Choose camera height:
   - eye-level for faithful memory and documentary warmth
   - child-height for childhood photos or school scenes
   - slight low angle for heroic, ceremonial, or animated-film presence
5. Extend the environment:
   - expand left and right around the original scene
   - add foreground, midground, and background layers
   - preserve original location cues while adding handmade set depth
   - add props only when they support the story
6. Generate the active image as a complete `16:9` horizontal composition.
7. Put the finished 16:9 shot into a 4:3 black-bar frame with `scripts/create_cinematic_frame.py`.

## Prompt Requirements

Include these ideas in the image-generation prompt:

```text
Generate as a true 16:9 horizontal cinematic shot, not a crop from the source portrait. Preserve the source subjects and their relationship, but expand the environment left and right into a complete stop-motion movie set. Use a [35mm/50mm/85mm] lens feel, [eye-level/child-height/slight low angle] camera height, [full-body wide/medium wide/medium/close-up] framing, layered foreground and background, shallow or medium depth of field, practical miniature lighting.
```

## Composition Guardrails

- Do not crop off heads, hands, essential clothing, or relationship cues.
- Do not move people so far from the source relationship that the story changes.
- Do not invent a new identity, age, role, or costume.
- Do not fill the expanded sides with generic decoration; extend the actual source world.
- Avoid empty widescreen padding. Every added side area should clarify place, depth, weather, light, or story.
- Keep the generated active picture text-free.

## Default Choices

Use these defaults when the source does not suggest a stronger choice:

- Lens: `50mm`
- Camera height: eye-level
- Framing: medium wide shot
- Depth of field: medium-shallow
- Light: warm practical film light based on the source photo
- Canvas: `16:9` active picture, then `4:3` black-bar final

## Examples

For an old vertical family photo:

```text
Preserve the family members' positions, clothing, posture, and expressions. Generate a true 16:9 horizontal claymation film still by expanding the original setting left and right: more winter trees, handmade ground texture, distant small props, warm faded memory light. Use a 50mm eye-level medium wide shot, full-body readable characters, layered miniature forest depth, no text.
```

For a campus portrait:

```text
Preserve the person's hairstyle, glasses, smile, outfit, and posture. Generate a true 16:9 horizontal claymation film still by expanding the campus courtyard around them: handmade flowers, red columns, lattice windows, stone base, foreground branches, warm afternoon light. Use a 50mm eye-level medium shot with shallow depth of field, no text.
```
