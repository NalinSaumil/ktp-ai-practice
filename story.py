import openai
from gtts import gTTS

# Enter your OpenAI API key here
openai.api_key = "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"

def generate_story(title):
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
    
    return generated_text

# Example usage
title = "Story of Ted Bundy"

def process(title):
  story = generate_story(title)

  print("Once upon a time, there was" + story)

  mytext = "Once upon a time, there was" + story

  Arr = mytext.split('\n\n')

  for i in range(0, len(Arr)):

    PROMPT = Arr[i]

    #create an image from the input of the dall E model
    response = openai.Image.create(
        prompt = PROMPT,
        n=1,
        size = "512x512"
    )

    #give a URL for the image that the dall E model creates
    print(response["data"][0]["url"])
    
  # Language in which you want to convert
  language = 'en'
    
  # Passing the text and language to the engine, 
  # here we have marked slow=False. Which tells 
  # the module that the converted audio should 
  # have a high speed

  myobj = gTTS(text=mytext, lang=language, slow=False)
    
  # Saving the converted audio in a mp3 file named
  # welcome 
  myobj.save("welcome.mp3")

while True :
    query = input("Enter your question: ")
    if query == "":
        break
    process(query)


