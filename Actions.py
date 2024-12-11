
import sys
sys.path.insert(1, '../')

import time
import os
import random
import numpy as np
from Print import Print
import nodriver as uc
import asyncio


class Actions:
    
    
    def __init__(self, mouse=None, scroll=None, page=None) -> None:
        self.mouse = mouse
        self.scroll = scroll
        self.page = page
    
    async def ran(self):
        return random.randint(20, 50)

    async def mosemove(self, x: int, y: int, q, w):

        v = await self.ran()
        v1 = await self.ran()
        v2 = await self.ran()
        v3 = await self.ran()
        
        G_0 = random.randint(v, random.randint(v, v + 20))
        W_0 = random.randint(v1, random.randint(v1, v1 + 20))
        M_0 = random.randint(v2, random.randint(v2, v2 + 20))
        D_0 = random.randint(v3, random.randint(v3, v3 + 20))
        
        return await self.wind_mouse(x, y, q, w, G_0, W_0, M_0, D_0)
    
    async def wind_mouse(self, start_x, start_y, dest_x, dest_y, G_0, W_0, M_0, D_0):
        
        sqrt3 = np.sqrt(2)
        sqrt5 = np.sqrt(10)

        current_x, current_y = start_x, start_y
        v_x = v_y = W_x = W_y = 0
        
        
        while (dist := np.hypot(dest_x - start_x, dest_y - start_y)) >= 1:
            W_mag = min(W_0, dist)
            if dist >= D_0:
                W_x = W_x / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
                W_y = W_y / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
            else:
                W_x /= sqrt3
                W_y /= sqrt3
                
                if M_0 < 3:
                    M_0 = np.random.random() * 3 + 3
                else:
                    M_0 /= sqrt5
                    
                    
            v_x += W_x + G_0 * (dest_x - start_x) / dist
            v_y += W_y + G_0 * (dest_y - start_y) / dist
            
            v_mag = np.hypot(v_x, v_y)
            if v_mag > M_0:
                v_clip = M_0 / 2 + np.random.random() * M_0 / 2
                v_x = (v_x / v_mag) * v_clip
                v_y = (v_y / v_mag) * v_clip
            start_x += v_x
            start_y += v_y
            move_x = int(np.round(start_x))
            move_y = int(np.round(start_y))
            
            if current_x != move_x or current_y != move_y:
                await self.page.send(uc.cdp.input_.dispatch_mouse_event("mouseMoved", x=float(move_x), y=float(move_y)))
                await self.page.sleep(random.randint(0, 9) / 100)
            
            current_x = move_x
            current_y = move_y
            
        
        return current_x, current_y
    
    async def click(self, x, y, q, w):
        
        try:
            
            x, y = await self.mosemove(x, y, q, w)
            
            # time.sleep(.1)
            
            await asyncio.gather(
                self.page.send(
                    uc.cdp.input_.dispatch_mouse_event(
                        "mousePressed",
                        x=x,
                        y=y,
                        button=uc.cdp.input_.MouseButton("left"),
                        click_count=1,
                    )
                ),
                self.page.send(
                    uc.cdp.input_.dispatch_mouse_event(
                        "mouseReleased",
                        x=x,
                        y=y,
                        button=uc.cdp.input_.MouseButton("left"),
                        click_count=1,
                    )
                ),
            )
            
            return x, y
        
        except Exception as e:
            Print.error(e)
            return 0, 0
    
    
    
