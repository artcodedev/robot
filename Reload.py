

from Print import Print
import random

class Reload:
    
    async def reload(act, page,  x, y):
        
        try:
            
            size = await page.get_window()
            
            wi = random.randint(0, int(size[1].width))
            
            await page.evaluate("window.location.reload()")
            
            x, y = await act.mosemove(x, y, wi, 0)
            
            return x, y
        
        except Exception as e:
            Print.log(e)
            
            return 0, 0