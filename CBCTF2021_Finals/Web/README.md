# Captcha the Flag

Tesseract sucks. It's not 100% accurate but I don't know how else I can extract text from images. This was particularly difficult as it kept getting the answer wrong part of the way. I'm sure I could try and enhance the image to make it more obvious of a number.

The images stored in this repo is the cleanest run for the tesseract to extract the text from. Challenges faced during this was mistaking different numbers (e.g. it tought a 7 was a 2). Another was thinking or believing that that there was space or commas in the numbers. I had to replace the strings to get rid of those. And a few times it saw intepreted 8 or 5 or 3 as a [Section Sign](https://en.wikipedia.org/wiki/Section_sign). It was fun hitting it for 4 hours over and over again.

Script is in the `flag.py`. 

Packages: `pip install -U pytesseract pillow`

And need tesseract installed on the machine and point the `path_to_tesseract` to the tesseract executable.