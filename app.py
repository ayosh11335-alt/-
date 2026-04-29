import streamlit as st
from gtts import gTTS

# عنوان التطبيق
st.title("🔊 تحويل النص إلى صوت")

st.write("اكتب النص اللي عايزه يتحول لصوت 👇")

# إدخال النص
text = st.text_area("اكتب هنا:")

# اختيار اللغة
lang = st.selectbox("اختار اللغة:", ["ar", "en"])

# زر التحويل
if st.button("تحويل"):
    if text.strip() != "":
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)

        st.success("تم التحويل بنجاح ✅")

        # تشغيل الصوت
        with open(filename, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
    else:
        st.error("اكتب نص الأول!")
