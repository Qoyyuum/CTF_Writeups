The `hitemup` challenge was a bit obvious due to my experience with HTTP requests. This basically means hitting the page until you get what you're looking for (or when you have to pay exobitant amounts for AWS requests or Google Maps requests on the monthly bill).

Worried I might DOS the web server, decided to try anyways. Despite that the content page is mirrored, the numbers sort of remained the same, just counted backwards. Run `./getflag.py` to get the flag. Unfortunately, the if conditions I put in, no matter the format, doesn't seem to catch the `005` mark at all, so I had to `CTRL+C` my way when it hit near it. Scrolled up and expected the flag to show up in the empty `<h1></h1>` tags but it ended displaying under the visitor counter instead. 

Flag was `}sihTdetpircSuoYepoHi{FTCBC`. Reversed it: `CBCTF{iHopeYouScriptedThis}`
