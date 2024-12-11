

from Print import Print
from Scroll import Scroll
import random


class Scroll_RA:
    
    async def random(act, page, x, y):
        
        try:
            
            count_rand = random.randint(2, 6)
            
            for _ in range(0, count_rand):
                
                scrollHeight = await page.evaluate("document.body.scrollHeight")
                pageYOffset = await page.evaluate("window.pageYOffset")
                
                pageYOffset = 0 if pageYOffset is None else pageYOffset
                
                scrollHeight_sp = scrollHeight / 2
                
                rand = random.randint(0, int(scrollHeight_sp))
                
                if scrollHeight_sp > pageYOffset:
                    Print.log("scroool down")
                    x, y = await Scroll.scroll_down(act, page, rand, x, y)
                
                if scrollHeight_sp < pageYOffset:
                    Print.log("scroool up")
                    x, y = await Scroll.scroll_up(act, page, rand, x, y)
                
            return x, y
        
        except Exception as e:
            Print.error('[+] Error in method random_scroll')
            Print.error(e)
            
            return 0, 0