# my_url_shortener_python_library
a python library for https://s.itayki.com

### Installation
 ```pip3 install git+https://github.com/iiiiii1wepfj/my_url_shortener_python_library.git```

### Example
get the links count:
   ```
from urlshortlib import UrlShort
import asyncio
urlshort = UrlShort(api_url="https://s.itayki.com")
async def main():
     print(await urlshort.get_links_count())

asyncio.run(main())
   ```

   ```
from urlshortlib import UrlShort
import asyncio
urlshort = UrlShort()
async def main():
    a = await urlshort.get_link_qr(slug="duckduckgo")
    with open("test.png", "wb") as img:
          img.write(a)
asyncio.run(main())
   ```
