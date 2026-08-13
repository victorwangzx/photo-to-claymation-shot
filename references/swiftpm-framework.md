# S/W/I/F/T/P/M Framework

Use this framework to convert one source photo into a controlled claymation cinematic prompt.

## S - Subject

Extract visual recognition cues from the person:

- age impression without over-specifying identity
- hairstyle, hair length, hair volume, and hairline shape
- face shape, cheeks, jaw, nose, eyes, brows, mouth, expression
- posture, gesture, head angle, gaze direction
- clothing silhouette, dominant colors, fabric type, collar, sleeves, layers
- accessories such as glasses, earrings, watch, hat, bag, tools, books, cup
- visible hands and any prop interaction

When converting to claymation, preserve the cues above but translate them into rounded handmade clay forms, slight asymmetry, tactile fingerprints, and expressive stop-motion features.

## W - World

Extract or infer the environment:

- visible background: room, street, campus, studio, office, home, stage, nature
- role context: teacher, student, parent, artist, worker, speaker, traveler
- props that define the scene
- spatial depth, walls, windows, desk, chair, shelves, doorways, signage
- privacy-sensitive details that should be simplified or anonymized

For the claymation version, rebuild the world as a miniature set using cardboard, clay, painted paper, fabric, wire, handmade lamps, toy-scale furniture, and imperfect handmade props.

## I - Intent

Identify the narrative or emotional intention:

- warm portrait
- humorous everyday moment
- quiet reflection
- teaching or learning tension
- tired but sincere work state
- family memory
- awkward social comedy
- ceremonial or heroic framing
- gentle absurdity

Prefer one clear intent. Translate abstract ideas into visible action, expression, object placement, lighting, and camera distance.

## F - Form

Choose or preserve cinematic form:

- shot size: medium shot, close-up, extreme close-up, macro, full body, over-the-shoulder
- angle: eye-level, low angle, overhead, three-quarter view, profile
- lens feel: shallow depth of field, soft focus background, handcrafted miniature scale
- composition: centered, off-center, diagonal axis, layered foreground, symmetrical stage-like setup
- motion implication: paused gesture, mid-action, held expression

The final image should read as a film still, not a flat avatar or product render.

## T - Time

Extract or choose light and time:

- morning warm light
- afternoon golden light
- dusk orange light
- night blue-purple light
- indoor soft lamp light
- rainy window light
- classroom fluorescent warmth

If the source photo has weak lighting, choose a time that supports the intended story.

## P - Perception

Define the sensory and emotional atmosphere:

- warm, sincere, humorous
- slightly chaotic, gently absurd
- quiet, reflective, nostalgic
- handmade, tactile, miniature
- cinematic, theatrical, intimate

Keep the atmosphere specific and visual. Avoid abstract praise words without scene evidence.

## M - Medium

Always include the medium constraints:

```text
Aardman claymation style, handcrafted miniature set, visible fingerprints, stop-motion aesthetic, cinematic film still, clay character, handmade props, shallow depth of field, no text, no watermark.
```

Add task-specific constraints when needed:

- for portraits: expressive clay face, preserved hairstyle and outfit, respectful likeness
- for campus scenes: clay classroom, paper props, handmade school furniture
- for comedy: slightly exaggerated features, awkward pause, playful prop staging
- for emotional portraits: warm handmade lighting, soft clay texture, intimate close-up

## Final Prompt Template

```text
S（主体）：
一位根据上传照片改编的阿德曼黏土动画风人物，保留【发型/脸型/表情/服装/姿态/配饰】等核心识别特征，具有手工塑形的圆润五官、可见指纹、轻微不对称的黏土质感。

W（世界）：
位于【根据照片背景或人物气质重构的微缩电影场景】，包含【纸板/黏土/织物/手工灯具/小道具】等停止动画布景元素。

I（意图）：
呈现【由照片提炼出的情绪或叙事意图】，例如温暖、幽默、沉思、期待、疲惫、荒诞、纪念感或电影感。

F（形式）：
使用【镜头类型】呈现，例如中景、近景、特写、低角度、俯拍或浅景深电影镜头，构图参考原照片的【角度/姿态/空间关系】，带轻微手工畸变。

T（时间）：
发生在【根据照片光线重构的时间与光色】，例如清晨暖光、午后金黄、傍晚橙光、夜间蓝紫或室内柔光。

P（感知）：
整体氛围【从照片提炼出的触感与情绪】，兼具手作温度、电影感、轻微荒诞和停止动画的真实材料感。

M（媒介）：
Aardman claymation style, handcrafted miniature set, visible fingerprints, stop-motion aesthetic, cinematic film still, clay character, handmade props, shallow depth of field, no text, no watermark.
```
