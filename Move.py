from Print import Print
import random

class Move:
    
    
    @staticmethod
    async def move(act, page,  x=0, y=0):
        
        try:
            
            Print.log("[+] Move rundom")
            count = random.randint(5, 15)
             
            Print.log(f'[+] Count move {count}')
            
            x = x
            y = y
            
            for _ in range(0, count):
                
                size = await page.get_window()
                
                xx = random.randint(0, int(size[1].width - 100))
                yy = random.randint(0, int(size[1].height - 100))
                
                Print.log("[+] Move")
                xs, ys = await act.mosemove(x, y, xx, yy)
                
                x = xs
                y = ys
            
            Print.ok("[+] Move rundom is done.")
            
            return x, y
        
        except Exception as e:
            Print.error("[+] Error in random_move class")
            Print.error(e)
        
        