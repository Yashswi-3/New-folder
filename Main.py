import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(
    page_title='Story Visualizer - Yashswi Shukla',
    layout='centered'
)

# Title and Introduction
st.title("✨ Misty Hill School Story Visualizer")
st.subheader("AI Internship by Yashswi Shukla")

st.sidebar.title("About the Characters")
st.sidebar.write("""
- **Pema** — a thoughtful red panda
- **Temba** — a black Himalayan bear with a mischievous side
- **Kima** — a grey langur, energetic and impulsive
- **Pihu** — a Himalayan bulbul, musical and graceful
- **Kunu** — a nimble goral, quietly wise
""")

st.sidebar.success("Select a scene to view from the pagination controls below!")

# Story scenes
scenes = [
    {
        "header": "1️⃣ Pema's Dawn Walk",
        "image": "ChatGPT Image Jun 15, 2025, 01_18_36 AM.png",
        "text": """
**Brief Description:**  
A solitary moment of quiet anticipation as Pema the red panda makes her pre‑dawn trek to school, savoring the stillness and magic of the misty hills.

**Story Excerpt:**  
> “Pema, a red panda with soft russet fur and thoughtful eyes, liked to walk to school before the village was fully awake. The hills were quiet then, and the clouds hung low like sleepy scarves across the trees. She took the winding path slowly, her paws making soft prints in the morning dew.”

**Sensory Details:**  
- Tactile: Pema’s paws make soft prints in the morning dew.  
- Visual: Low mist, clouds hang low.  
- Auditory: The hills are silent.  

**Why this scene?**  
- Establishes Pema as the protagonist
- Sets atmospheric context
- Highlights solitude before friendships form
        """
    },
    {
        "header": "2️⃣ Turning Toward School with Kunu",
        "image": "ChatGPT Image Jun 15, 2025, 01_14_00 AM.png",
        "text": """
**Brief Description:**  
At Pema’s gentle reminder, the friends pivot toward the school’s hidden roof—a moment of shared purpose before Kunu’s arrival.

**Story Excerpt:**  
> “‘Not now,’ Pema said gently. ‘We’ll be late.’  
> The four of them turned toward the last bend in the trail, where the school roof peeked out from behind the pines.  
> And there, as always, came Kunu.”

**Sensory Details:**  
- Visual: The school roof peeks from pines
- Kinesthetic: A gentle breeze with the flags
- Emotional: Anticipation and togetherness
        """
    },
    {
        "header": "3️⃣ Kunu Points - Group's Shared Awe",
        "image": "ChatGPT Image Jun 15, 2025, 01_14_14 AM.png",
        "text": """
**Brief Description:**  
Kunu guides his friends toward a moment of awe as the clouds lift and the first rays illuminate the peak.

**Story Excerpt:**  
> “He didn’t speak right away. Kunu was a young goral—a nimble creature with grey fur and steady steps. He nodded toward the clouds.  
> A ray of sunlight fell upon the snow-capped peak.  
> ‘Clear day,’ Kunu said softly.  
> They stood together, enraptured by nature’s magic.”

**Sensory Details:**  
- Auditory: A woodpecker taps, a birdsong resonates
- Olfactory: The air smells of pine and slate
- Visual: The clouds lifting, the sunlight touching the peak
        """
    },
    {
        "header": "4️⃣ Final Dash to the Gate",
        "image": "ChatGPT Image Jun 15, 2025, 02_18_44 AM.png",
        "text": """
**Brief Description:**  
The friends break into a sprint toward the school gate, their youthful energy fueling their forward rush.

**Story Excerpt:**  
> “Then—ding ding ding!—the school bell rang, faint but bright.  
> ‘Last one to the gate is a sleepy snail!’ Kima shouted, already halfway there.  
> Pema walked behind the others, smiling to herself.  
> She liked the first day of school. It always felt a little bit like the first page of a book.”

**Sensory Details:**  
- Auditory: The school bell ringing
- Visual/Emotional: The children’s happiness and renewal
        """
    },
    {
        "header": "Full Story",
        "image": None,
        "text": """
**First Bell at Misty Hill School**  

Pema, a red panda with soft russet fur and thoughtful eyes, liked to walk to school before the village was fully awake. The hills were quiet then, and the clouds hung low like sleepy scarves across the trees. She took the winding path slowly, her paws making soft prints in the morning dew.
At the bend near the prayer flag tree, someone was waiting. Temba, a woolly Himalayan black bear, waved with both paws. “I thought I’d be the first today,” he grinned, a little out of breath. His ears twitched in the breeze.
“You’re early,” Pema said with a smile. “Did you take the steep trail again?”
“I ran most of the way,” Temba said proudly, then sat down on a flat stone. “Only tripped twice.”
They sat quietly for a moment, listening. Far off, a woodpecker tapped on a pine. Somewhere below, a goat bleated. Mist still curled along the ridgeline, soft and slow.
Then came a rustle from the hillside above.
Kima slid down a patch of dry grass, landing in a happy tumble near their feet. He was a grey langur, lanky and full of energy. “Guess who found a secret shortcut!” he announced, brushing twigs from his fur.
“You say that every week,” said Pema.
“This time it’s actually secret,” Kima insisted, holding up a shiny acorn as proof. “Also, there’s a rock shaped like a mango. I licked it just to check.”
Temba giggled. “Was it sweet?”
“Mostly just dusty,” Kima said, making a face.
Just then, a flutter of wings passed overhead. Pihu swooped down in a lazy spiral and landed beside them. She was a Himalayan bulbul with bright eyes and a musical voice. “The wind’s perfect today,” she said, fluffing her feathers. “You could float all the way to the lake if you wanted.”
Kima’s eyes lit up. “Let’s try it!”
“Not now,” Pema said gently. “We’ll be late.”
The four of them turned toward the last bend in the trail, where the school roof peeked out from behind the pines.
And there, as always, came Kunu.
He didn’t speak right away. Kunu was a young goral—a nimble mountain goat with soft grey fur and steady steps. He simply nodded at the others, then pointed toward the mountain ridge.
A line of sunlight had just touched the snowcap above. The clouds were lifting.
“Clear day,” Kunu said softly. “You can see the whole peak.”
They stood for a moment, all five, watching the morning open up before them. The forest shimmered with birdsong. The air smelled of pine and slate.
Then—ding ding ding!—the school bell rang, faint but bright.
“Last one to the gate is a sleepy snail!” Kima shouted, already halfway there.
Pema walked behind the others, smiling to herself. New notebooks, clean chalkboards, stories waiting to begin. She liked the first day of school. It always felt a little bit like the first page of a book.

        """
    },
]

# Pagination
page = st.number_input("Select scene number", min_value=1, max_value=len(scenes), value=1)

current_scene = scenes[page - 1]

st.header(current_scene['header'])

if current_scene['image']:
    st.image(current_scene['image'], use_container_width=True)

st.markdown(current_scene['text'])

# Footer
st.markdown('---')
st.caption("Created with Streamlit for AI Internship | Images generated with ChatGPT")
