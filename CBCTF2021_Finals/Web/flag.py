
#!/usr/bin/env python3

def serve_page(captcha):
    import requests

    url = 'http://captcha.cb.ctf/index.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }

    if captcha == "":
        params = (
            ('name', 'loki'),
        )
    else:
        params = (
            ('name', 'loki'),
            ('captcha', captcha)
        )

    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    import re
    import sys
    try: 
        if "Reverse" in response.text:
            make_image(response.text)
    except Exception:
        pass


def make_image(pic):
    import re
    import io
    import base64
    from PIL import Image, ImageFilter
    from pytesseract import pytesseract
    path_to_tesseract = r"/bin/tesseract"

    # test = '<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAAAoAQMAAACB0idfAAAABlBMVEX///8AAABVwtN+AAAA2UlEQVQ4jWNgGGaA8eEHAxs5fvb2AwYffrDJ2bc3H//4ASzDbCxRkWYs2XMmoXBmD5+xAc+xNGYJsAybBM+Zw4kbZiQYfOZgk0vcIOFjxsADlZFsSwMKJCRuZuAxMzaXYEt7ANHDbFHYZmO8nefhYeMCizQ5y9nNxw0KIC64AdQju7M9Ic14Bs8xY4Y7xxIkIHoYJHjbDjNuOJBg/puH7X9iw40cAwmIPUwgFyhuOJFgYMzDxpa44UaOGVQG4WrDmT1sQMaxZGMJbD7lZ28++PADfQJ5FAxXAAAVtUwUr3dABgAAAABJRU5ErkJggg=="/>'
    pattern = r'base64,(\S+)"/>'
    match = re.search(pattern, pic)
    image_string = io.BytesIO(base64.b64decode(match.group(1)))

    num_pattern = r'Solved (\d+) captcha'
    num_match = re.search(num_pattern, pic)
    if num_match is not None:
        num_match = num_match.group(1)
    else:
        num_match = 0
    im = Image.open(image_string)
    im.save(f'image{num_match}.png', 'PNG')
    pytesseract.tesseract_cmd = path_to_tesseract
    captcha = pytesseract.image_to_string(im)
    print(f"Caught Captcha: {captcha}")
    answer = captcha[::-1].replace(',', '').replace(' ', '') # Tesseract kept reading commas and spaces
    print(f"Answer is : {answer}")
    serve_page(answer)

if __name__ == "__main__":
    serve_page(captcha="")

"""

    <div class="container">
      <h1>Here are some challenge for you </h1>
      
        <p>Solve 500 captcha to get the reward.</p>
        <form action="/index.php" method="get">
          <p>Name:</p>
          <p><input type="text" name="name" value="loki" readonly></p>
         <p style="color:blue;"> Correct!</p>   <p>Solved 500 captcha</p> 


        <br>Congrats you solve 500 captcha! Here is your key: <b>CBCTF{c@ptcha_is_secure?}</b> <p><input type="text" name="captcha"></p><p><input type="submit" value="submit"></p>
        </form>
    </div> <!-- /container -->
  </body>
</html>
"""
