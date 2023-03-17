from tashkeel import tashkeel
from audio import generate_audio

SYSTEM_NAME = "مُعِينْ"
SYSTEM_PROMPT = f"مرحبابك معك {SYSTEM_NAME} كيف ممكن اساعدك"

text = tashkeel(SYSTEM_PROMPT)
generate_audio(text, "entry_audio")

