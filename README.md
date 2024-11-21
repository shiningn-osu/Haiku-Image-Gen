
# SUMMARY:

    -This microservice uses text files to input a haiku, request an image from OPENAI's DALL E 3
    ai image generator, and outputs the url to said generated image into output.txt

    -To be able to run this program, you will need to install the openai library
    in your console, type:

    "pip install openai"

        -python will need to be written to your PATH environment variable, which can be done when installing
        python, or manually in windows settings.
        - if python reads that openai is not found, try reinstalling python from scratch, as python can have
        frequent issues with recognizing versions that exist on your machine, and can be referencing the wrong
        one
        - If openai is still not recognized, try uninstalling all recognized versions of python on your computer,
        and check C:\msys64\ucrt64\bin and delete all executables with python logos 
        after all of this, then reinstall python by checking the option that the PATH environment is written, and 
        pip is installed. (this is what finally worked for me after many hours)
    
    - all other libraries should be native to python.

# CONTRACT FOR HAIKU IMAGE GENERATOR (MICROSERVICE A)
 
## REQUESTING DATA:

    To request an image generation, write the haiku in question into "input.txt", and write the 
    "run" into signal.txt while the microservice is running. Every 3 seconds, the service tests for
    the contents of signal.txt, and if they are "run", it will automatically take the contents of 
    input.txt and call for an image using them, before clearing signal.txt, to wait for another prompt

    for example, in input.txt:

        with p.open('w') as file:
            Lines = file.writelines("Bleak good afternoon \n A domestic, blue pig flies \n in spite of the cube")

    (The above string can be replaced with a variable containing a generated haiku)
    then, in signal.txt:

        with p.open('w') as file:
            Lines = file.writelines("run")

    this would signal chatgpt to create an image based on the above haiku.


## RECEIVING DATA:

    The output url containing the image will be pasted to output.txt, and can be read, downloaded, or
    used in any other way that the user desires.

    The following url can be used however the user pleases, the best overall example would be to
    take the url and be able to use it as a variable within a python program, for example:

        with p.open('r') as file:
          Lines = file.readlines()

        for x in range(len(Lines)):
            url += Lines[x] + " "
        
    this would save the url within the file into a single string object.






    CLIENT                          Microservice                                               OPENAI API
    |                               | (constantly testing for "run" in signal.txt)             |
    | -- write haiku to input.txt ->|                                                          |
    | -- write "run" to signal.txt->|                                                          |
    |                               | -- recognizes "run"                                      |
    | <-erases "run" from signal.txt|                                                          |
    |                               | -- Takes haiku, inputs it as prompt into OPENAI API  ->  |
    |                               | <- Returns URL containing generated image  ------------- | 
    | <- Writes url to output.txt   |                                                          |
    |                               |RETURNS TO TESTING FOR RUN                                |
    |                               |                                                          |




## OTHER NOTES:

    Please note:
    OpenAI charges $0.04 per image generated. The api key included within main.py currently is tied to a balance, and so
    please refrain from generating many many images in testing, if you need to generate many images, (like over 30) please register your own 
    api key at https://platform.openai.com/settings/organization/api-keys
    Obviously its only 4 cents per image, I just want to warn you as at some point it would stop functioning as the balance (around 4 dollars left) 
    would eventually run out and it would give you a limitation error.


