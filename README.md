# Photo To Claymation Shot

Turn a portrait photo into an Aardman-style claymation cinematic still, then deliver a clean before/after comparison image.

This Codex skill is designed for photo-to-image workflows where the output should feel like a handcrafted stop-motion film frame instead of a simple style filter.

## What It Does

- Analyzes a source portrait with the S/W/I/F/T/P/M framework.
- Preserves recognizable subject cues such as hairstyle, expression, posture, clothing, and accessories.
- Rebuilds the person as a handmade clay character in a miniature stop-motion set.
- Removes useless source-image borders such as black bars or blank scan margins.
- Generates the claymation result at the cleaned source image's dimensions when possible.
- Delivers one combined comparison image by default:
  - portrait source images: original and result side by side
  - landscape source images: original above result
  - square source images: original above result

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
- `scripts/compose_comparison.py`: deterministic before/after image composition helper
- `agents/openai.yaml`: Codex UI metadata

## Notes

This skill does not include sample photos or generated outputs. Keep user images and generated artifacts outside the skill folder.
