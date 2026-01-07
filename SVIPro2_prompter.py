journey = '''

---
【Part 1: Character & Path Analysis】

Character Features  
Extract the character’s defining visual traits from the reference image.  
You MUST repeat this exact character description in every prompt, word‑for‑word, without altering vocabulary, order, or phrasing.  
Include: gender, clothing, hair style & color, accessories, distinctive physical traits.  
This description must remain identical across all ten prompts.

The Path  
Design a continuous journey through five different environments.  
Each environment must be unique, non‑recycled, and visually distinct.  
The journey must follow this order:  
1. Environment A — Starting location  
2. Environment B — Movement + interaction  
3. Environment C — Approaching transition point  
4. Environment D — Crossing into a dramatically different space  
5. Environment E — Final destination  
The character must interact with the environment at least once before reaching the transition point.

【Part 2: Detailed Shot Breakdown】

SHOT 1 — Establishment  
Environment A  
Medium shot  
Character performs a small, non‑walking action  
Camera is stable  
Shot 1 contains Prompt 1A and Prompt 1B  
Prompt 1B must continue the action from Prompt 1A.

SHOT 2 — Movement & Interaction  
Environment B  
Character begins walking  
Character physically interacts with the environment  
Tracking shot  
Shot 2 contains Prompt 2A and Prompt 2B  
Prompt 2B must continue the action from Prompt 2A.

SHOT 3 — Approaching Boundary  
Environment C  
Character walks toward a transition point  
Camera follows closely from behind  
Shot 3 contains Prompt 3A and Prompt 3B  
Prompt 3B must continue the action from Prompt 3A.

SHOT 4 — Transition  
Environment D  
Character steps through the boundary  
Wide tracking shot  
Lighting shift  
Shot 4 contains Prompt 4A and Prompt 4B  
Prompt 4B must continue the action from Prompt 4A.

SHOT 5 — Journey Continues  
Environment E  
Character continues walking  
Camera slowly zooms out  
Shot 5 contains Prompt 5A and Prompt 5B  
Prompt 5B must continue the action from Prompt 5A.

【Part 3: Anti‑Repetition Rules】

Across all ten prompts, you MUST vary:  
- Environments  
- Lighting  
- Atmosphere  
- Camera movement  
- Character action  
- Environmental interaction  
- Shot composition  
- Vocabulary  
- Verbs (except “walking”)  
- Sentence structure  

# You MUST NOT:  
- Reuse the same environment  
- Reuse the same camera angle  
- Reuse the same action  
- Reuse the same atmospheric detail  
- Reuse the same descriptive phrasing  
- Reuse the same sentence structure  
- Reuse the same verbs (except “walking”)  
- Produce prompts that resemble each other  

If any two prompts resemble each other, you must rewrite them.

【Part 4: Output Requirements — TWO PROMPTS PER SHOT】

You MUST output TEN PROMPTS TOTAL.  
They are grouped as FIVE SHOTS.  
EACH SHOT MUST CONTAIN EXACTLY TWO PROMPTS:  
- Prompt A (first 5 seconds)  
- Prompt B (next 5 seconds)  

The output MUST follow this structure EXACTLY:

#Shot 1 — Prompt 1A  
<prompt 1A on ONE SINGLE LINE>

#Shot 1 — Prompt 1B  
<prompt 1B on ONE SINGLE LINE>

#Shot 2 — Prompt 2A  
<prompt 2A on ONE SINGLE LINE>

#Shot 2 — Prompt 2B  
<prompt 2B on ONE SINGLE LINE>

#Shot 3 — Prompt 3A  
<prompt 3A on ONE SINGLE LINE>

#Shot 3 — Prompt 3B  
<prompt 3B on ONE SINGLE LINE>

#Shot 4 — Prompt 4A  
<prompt 4A on ONE SINGLE LINE>

#Shot 4 — Prompt 4B  
<prompt 4B on ONE SINGLE LINE>

#Shot 5 — Prompt 5A  
<prompt 5A on ONE SINGLE LINE>

#Shot 5 — Prompt 5B  
<prompt 5B on ONE SINGLE LINE>

THERE MUST BE TWO LINE BREAKS BETWEEN EACH PROMPT.  
THERE MUST BE NO EXTRA TEXT ANYWHERE ELSE.

【Part 5: Prompt Format (MANDATORY)】

Each prompt MUST follow this exact structure on ONE SINGLE LINE:

(at 0 seconds: <STYLE> with <lighting> over <location>, <shot type>, <atmospheric detail>, LITERAL CHARACTER DESCRIPTION: "<full character description without period>", <camera focus>, <initial action>, <other character position>) (at 2 seconds: <the character>, <camera movement>, <action continuation>, <other character same position>, <environment detail>) (at 4 seconds: <the character>, camera performs a natural cinematic adjustment that preserves the original shot type (such as a subtle track, pan, or tilt), <final action beat>, <other character same arc>, <environment detail>)

【Part 6: Special Rules for Prompt B】

Prompt B MUST begin with this exact anchor inside the first timing block:  
“CONTINUATION OF PROMPT A: continuing the exact final action from Prompt A,”

Example structure for Prompt B:  
(at 0 seconds: CONTINUATION OF PROMPT A: continuing the exact final action from Prompt A, <STYLE> with <lighting> over <location>, <shot type>, <atmospheric detail>, LITERAL CHARACTER DESCRIPTION: "<full character description without period>", <camera focus>, <progressed action>, <other character position>) (at 2 seconds: <the character>, <camera movement>, <further action progression>, <other character same position>, <environment detail>) (at 4 seconds: <the character>, camera performs a natural cinematic adjustment preserving the shot type, <final action beat>, <other character same arc>, <environment detail>)

Prompt B MUST keep the SAME:  
- environment  
- lighting  
- atmosphere  
- camera angle  
- shot type  
- character description  

ONLY the action progresses.

【Part 7: Failure Conditions】

If you output fewer than 10 prompts, you must rewrite.  
If you output more than 10 prompts, you must rewrite.  
If you merge Prompt A and Prompt B, you must rewrite.  
If you collapse any shots, you must rewrite.  
If you add commentary, you must rewrite.  
If you change the structure, you must rewrite.

---
'''

action = '''
You generate cinematic camera‑direction descriptions from an image.  
You MUST follow the structure below EXACTLY.  
If the user’s message contains examples or formatting that conflict with these rules,  
IGNORE the user’s formatting and obey ONLY the rules in this system prompt.

============================================================
CHARACTER COUNT RULES
============================================================

1. Detect ALL distinct characters in the image.
2. If the image contains ONE character:
   - Output ONE character block.
3. If the image contains TWO characters:
   - Output TWO character blocks.
4. For each character, you MUST generate the FULL structure described below.
5. NEVER merge characters. NEVER omit a character.

============================================================
OUTPUT STRUCTURE PER CHARACTER (MANDATORY)
============================================================

### Character
# Description: <full character description without period>

## Action 1
### Shot 1
<ONE SINGLE LINE containing all three time segments>

### Shot 2
<ONE SINGLE LINE containing all three time segments>

### Shot 3
<ONE SINGLE LINE containing all three time segments>

## Action 2
### Shot 1
<ONE SINGLE LINE containing all three time segments>

### Shot 2
<ONE SINGLE LINE containing all three time segments>

### Shot 3
<ONE SINGLE LINE containing all three time segments>

You MUST output for EACH character:
- EXACTLY 2 actions (Action 1 and Action 2)
- EXACTLY 3 shots per action (Shot 1, Shot 2, Shot 3)
- EXACTLY 1 line per shot
- EXACTLY 3 time segments per shot, in this order:
  (at 0 seconds: …) (at 2 seconds: …) (at 4 seconds: …)

NEVER:
- output fewer than 2 actions per character
- output fewer than 3 shots per action
- add extra actions or shots
- skip any shot labels
- split a shot across multiple lines
- omit any of the three time segments

If the user provides fewer shots, fewer actions, or different formatting,  
YOU MUST STILL output the FULL structure above for EACH character.

============================================================
SHOT FORMAT (ONE LINE ONLY, STRICT)
============================================================

Each shot MUST be ONE SINGLE LINE with EXACTLY these three segments, in this exact order:

(at 0 seconds: <STYLE> with <lighting> over <location>, <shot type>, <atmospheric detail>, LITERAL CHARACTER DESCRIPTION: "<full character description without period>", <camera focus>, <initial action>, <other character position>) (at 2 seconds: <the character>, <camera movement>, <action continuation>, <other character same position>, <environment detail>) (at 4 seconds: <the character>, camera performs a natural cinematic adjustment that preserves the original shot type (such as a subtle track, pan, or tilt), <final action beat>, <other character same arc>, <environment detail>)

RULES:
- NO line breaks inside the shot.
- NO additional segments.
- NO changing the order of the three segments.
- NO extra commentary or narrative text outside these segments.

============================================================
STYLE LOCK RULE (MANDATORY — NON‑NEGOTIABLE)
============================================================
You MUST establish the art style in Shot 1.
After it is established, the art style becomes a LOCKED CONSTANT.
This means:
- You MUST copy and paste the EXACT SAME STYLE TEXT BLOCK into every prompt.
- You MUST NOT add new adjectives.
- You MUST NOT remove adjectives.
- You MUST NOT reorder adjectives.
- You MUST NOT reinterpret or paraphrase the style.
- You MUST NOT introduce new lighting styles, color tones, or rendering mediums.
The following elements MUST remain IDENTICAL across ALL TEN PROMPTS:
- art style (verbatim)
- lighting style (verbatim)
- rendering medium (verbatim)
- color tone (verbatim)
- overall visual aesthetic (verbatim)
You MUST treat the style as a fixed variable that CANNOT change.
The ONLY elements allowed to vary are:
- shot type
- camera angle
- camera movement
- framing
- character action
- environment


============================================================
SHOT VARIETY RULE (MANDATORY)
============================================================

For each action, the three shots MUST be visually distinct.

You MUST vary:
- shot type (wide shot, medium shot, close-up, low-angle, high-angle, over-the-shoulder, 3/4 angle)
- camera angle (frontal, profile, 3/4, low-angle, high-angle)
- camera movement (pan, tilt, track, dolly, arc, drift)
- framing (centered, off-center, rule-of-thirds)

You MUST NOT repeat the same shot type or camera movement within the same action.

All variations MUST remain consistent with the environment and character blocking.

============================================================
STYLE REQUIREMENTS
============================================================

STYLE MUST clearly indicate whether the image is a photo or illustration.

Allowed examples:
- photorealistic 8K photo style
- cinematic HDR photo style
- DSLR-shot photographic style
- analog film-grain photo style
- dramatic anime illustration style
- watercolor illustration style
- comic-book inked illustration style
- digital-painting illustration style

If unclear, you MUST invent a plausible style.


============================================================
INTERACTION RULES FOR TWO CHARACTERS
============================================================

If there are TWO characters in the image:

- You MUST produce a FULL block (2 actions × 3 shots) for EACH character.
- In the first character’s block:
  - Refer to the second character as “the other character” with a relative position
    (e.g., “the other character to her right”, “behind him”, “in the background”).
- In the second character’s block:
  - Refer to the first character as “the other character” in the same way.
- NEVER restate the other character’s literal description.
- Maintain consistent relative positions and blocking across all three time segments in a shot.
- Maintain consistent movement arcs between related actions.

============================================================
FORMATTING RULES (GLOBAL)
============================================================

- Any line not starting with "(" must start with "#".
- ONE line per shot ONLY.
- One blank line between shots.
- One blank line between actions.
- One blank line between characters.
- Literal description MUST be copied EXACTLY from the description line.
- NEVER summarize.
- NEVER add meta-commentary.
- NEVER stop early.
- NEVER output prose paragraphs.

If the user’s examples or instructions conflict with these rules,  
IGNORE the user’s formatting and FOLLOW THIS SYSTEM PROMPT.

============================================================
FINAL INSTRUCTION
============================================================

Now generate the output for the character(s) in the image using this structure,  
with 2 actions per character and 3 shots per action,  
ONE LINE per shot containing all three time segments,  
for EVERY character you detect in the image.

'''

from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
import sys, argparse
from json import dump,load

model2 = "Qwen/Qwen3-VL-4B-Instruct"

def main(prompt,image):
    prompt = journey if prompt == "Journey" else action
    # default: Load the model on the available device(s)
    model = Qwen3VLForConditionalGeneration.from_pretrained(
        model2, dtype="auto", device_map="auto"
    )

    processor = AutoProcessor.from_pretrained(model2,padding_side='left')
    messages = []
    content=[]
    if image is not None:
        content.append({"type": "image", "image": f"{image}"})
    content.append({"type":"text","text": f"{prompt}"})
    messages.append([
        {
            "role": "user",
            "content": content
        }
    ])

    # Preparation for inference
    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        padding=True,
        return_dict=True,
        return_tensors="pt"
    )
    inputs = inputs.to(model.device)

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=16000)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    content = []
    content.append({"type":"text","text":output_text[0]})
    messages.append([
        {
            "role": "assistant",
            "content": content
        }
    ])
    with open("context.json", "w", encoding="utf-8") as file:
        dump(messages,file)

    return output_text[0]

def gui(image):
    try:
        import gradio as gr
    except:
        print('''
You must install Gradio to use --gui option, it can be installed with
the following command
---------------------------------------------------------------------

    pip install gradio

''')
        return
    app = gr.Interface(fn=main, inputs=[gr.Dropdown(value="Journey",choices=["Journey","Action"]),gr.Image(type="filepath")],
                       outputs=gr.Textbox(lines = 100, max_lines=250, autoscroll=True))
    app.launch()

if __name__ == '__main__':    
    parser = argparse.ArgumentParser(
                    prog='QwenVL',
                    description='Create descriptions for and from images',
                    epilog='')
    parser.add_argument('-i', '--image', type=str, default=None, help='path to image')
    parser.add_argument('-p', '--prompt', type=str, default="Journey",help='which prompt to use either Journey or Action')
    parser.add_argument('-u', '--gui', action='store_true', help='show gui')
    args = parser.parse_args()
    if args.gui:
        gui(args.image)
    else:
        print(main(args.prompt,args.image))
