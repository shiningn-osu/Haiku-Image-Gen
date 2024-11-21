from openai import OpenAI
from pathlib import Path
import time

client = OpenAI(api_key="")

def ParseLines(Lines):          #place array of file lines into 1 string
  output = ""
  for x in range(len(Lines)):
    output += Lines[x] + " "
  return output

def main():
  prompt = ""

  while(True):

    p = Path(__file__).with_name('signal.txt') #test if signal is active
    with p.open('r') as file:
      Lines = file.readlines()
      if(Lines == ["run"]):
        print("signal found, running")

        p = Path(__file__).with_name('input.txt') #take haiku
        with p.open('r') as file:
          Lines = file.readlines()
          prompt = ParseLines(Lines)

        p = Path(__file__).with_name('signal.txt') #clear signal
        with p.open('w') as file:
          Lines = file.writelines("")
          print("SIGNAL CLEARED, PROMPT IS "  + prompt)
          print("OPENAI API PROMPTED, WAITING FOR RESPONSE...")
          response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,                      #input haiku
            size="1024x1024",
            quality="standard",
            n=1,
          )
          print("RESPONSE RECIEVED, PRINTING URL:")
          image_url = response.data[0].url
          print(image_url)

          p = Path(__file__).with_name('output.txt')
          with p.open('w') as file:
            Lines = file.writelines(image_url)
          print("Output URL written to output.txt")
          print("Testing for new signal...")
      else:                                     #no signal found, waiting...

        print("no signal found")
        time.sleep(3) #wait 3 seconds before testing again


main()

