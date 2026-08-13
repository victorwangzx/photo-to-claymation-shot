# Photo To Claymation Shot

Turn a portrait photo into an Aardman-style claymation cinematic still, then deliver both a clean before/after comparison image and a movie-spec cinematic matte frame.

This Codex skill is designed for photo-to-image workflows where the output should feel like a handcrafted stop-motion film frame instead of a simple style filter.

## What It Does

- Analyzes a source portrait with the S/W/I/F/T/P/M framework.
- Preserves recognizable subject cues such as hairstyle, expression, posture, clothing, and accessories.
- Rebuilds the person as a handmade clay character in a miniature stop-motion set.
- Removes useless source-image borders such as black bars or blank scan margins.
- Generates the claymation result at the cleaned source image's dimensions when possible.
- Delivers two final image artifacts by default:
- A combined comparison image:
  - portrait source images: original and result side by side
  - landscape source images: original above result
  - square source images: original above result
  - same-framing results are resized/cropped directly to the cleaned source dimensions
  - cinematic results use a Photoshop-like layer alignment step so the core subject height and body anchors match before cropping
- A cinematic matte frame:
  - final canvas: 4:3
  - active movie picture: 16:9
  - default: `1440 x 1080` canvas with a `1440 x 810` active picture and black bars above/below
  - the 16:9 movie picture is generated as a separate cinematic shot, not cropped from the portrait comparison image

## Install

Copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R photo-to-claymation-shot ~/.codex/skills/
```

Then invoke it in Codex:

```text
$photo-to-claymation-shot
Turn this portrait into a claymation cinematic still.
```

## Example Use

```text
$photo-to-claymation-shot
Use this old family photo as the source. Preserve the two children, the winter woodland, and the faded memory feeling. Deliver the original-plus-result comparison image.
```

## Included Files

- `SKILL.md`: main skill workflow and guardrails
- `references/swiftpm-framework.md`: S/W/I/F/T/P/M breakdown system
- `references/claymation-style-rules.md`: claymation image style rules
- `references/cinematic-shot-design.md`: 16:9 movie-shot direction rules
- `scripts/compose_comparison.py`: deterministic before/after image composition helper
- `scripts/create_cinematic_frame.py`: deterministic 4:3 film-frame helper with 16:9 active image area
- `agents/openai.yaml`: Codex UI metadata

## Notes

This skill does not include sample photos or generated outputs. Keep user images and generated artifacts outside the skill folder.
