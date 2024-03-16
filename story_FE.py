import streamlit as st
import openai
from gtts import gTTS

# Set OpenAI API key
openai.api_key = "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"

# Function to generate story and audio
def generate_story_and_audio(title):
    # Prompt for GPT-3 model
    prompt = (f"{title}\n\nOnce upon a time, there was")

    # Generate text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=60,
    )

    # Extract the generated story from the response
    generated_text = response.choices[0].text

    # Add story prefix
    story = "Once upon a time, there was" + generated_text

    # Split story into paragraphs
    paragraphs = story.split('\n\n')

    # Process each paragraph to generate image and print image URL
    image_urls = []
    for paragraph in paragraphs:
        st.write(paragraph)
        response = openai.Image.create(
            prompt=paragraph,
            n=1,
            size="512x512"
        )
        image_urls.append(response["data"][0]["url"])
        st.image(response["data"][0]["url"])

    # Generate audio from story
    language = 'en'
    myobj = gTTS(text=story, lang=language, slow=False)
    myobj.save("welcome.mp3")

    return story, image_urls

# Streamlit app
def app():
    st.title("Story Book Generator")
    st.write("Type a title and click the button to generate your story and audio!")

    # Get title from user input
    title = st.text_input("Enter story title:")

    # Generate story and audio when user clicks button
    if st.button("Generate"):
        story, image_urls = generate_story_and_audio(title)

        # Display audio
        st.audio("welcome.mp3")

if __name__ == '__main__':
    app()