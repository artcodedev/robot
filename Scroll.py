

from Print import Print
import nodriver as uc
import random


class Scroll:
    
    page = None
    x = None
    y = None
    atc = None
    
    
    @staticmethod
    async def divide(value: int, parts: int) -> int:
        res = [random.random() for _ in range(int(parts))]
        coef = value / sum(res)
        return [int(x * coef) for x in res]
    
    
    @staticmethod
    async def __scroll(i, page):
        
        try:
            
            size = await Scroll.page.get_window()
            
            xx = random.randint(0, int(size[1].width / 2))
            yy = random.randint(0, int(size[1].height / 2))
            
            xs, ys = await Scroll.act.mosemove(Scroll.x, Scroll.y, float(xx), float(yy))
        
            dv_i = await Scroll.divide(i, 8 * abs(i / 1000)) if i > 2000 or i < -2000 else await Scroll.divide(i, 8)
            
            for h in dv_i:
                
                await page.sleep(random.randint(1, 3) / 100)
                
                await page.send(
                    uc.cdp.input_.synthesize_scroll_gesture(
                        x=0,
                        y=0,
                        y_distance=h,
                        y_overscroll=0,
                        x_overscroll=0,
                        prevent_fling=True,
                        repeat_delay_ms=0,
                        speed=random.randint(200, 400),
                    )
                )
                
            xs, ys = await Scroll.act.mosemove(Scroll.x, Scroll.y, xs, ys)
            
            return xs, ys
        
        except Exception as e:
            Print.error(e)
    
    
    @staticmethod
    async def scroll_up(act, page, i, x, y):
        try:
           
            Print.log("[+] Scroll up")
            
            Scroll.page = page
            Scroll.x = x
            Scroll.y = y
            Scroll.act = act
            
            return await Scroll.__scroll(i * 1, page) 
            
        except Exception as e:
            Print.error("[+] Error in method scroll_up")
            Print.error(e)
            
    
    @staticmethod
    async def scroll_down(act, page, i, x, y):
        try:
            
            Print.log("[+] Scroll down")
            
            Scroll.page = page
            Scroll.x = x
            Scroll.y = y
            Scroll.act = act
            
            return await Scroll.__scroll(i * -1, page) 
            
        except Exception as e:
            Print.error("[+] Error in method scroll_down")
            Print.error(e)
            return 0, 0