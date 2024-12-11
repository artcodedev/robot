

from Print import Print
from Executor import Executor
import sys
import random

class Some_DO:
    
    @staticmethod
    async def some_do(act, page, s, x, y):
        
        for i in s:
            
            try:
                
                Print.log("[+] Start Some Do")
                
                inner_html = await Executor.innerHTML(page)
                
                if "Проверьте настройки прокси-сервера и брандмауэра." in inner_html:sys.exit(0)
                
                if "ERR_TUNNEL_CONNECTION_FAILED" in inner_html: sys.exit(0)
                
                if "ERR_TIMED_OUT" in inner_html: sys.exit(0)
                 
                else:
                    
                    Print.warning(i['el'])
                    
                    el = await Executor.locator(page, i['el'])
                    
                    if el is not None:
                        
                        coords = await Executor.coords(page, i['el1'], 0)
                        
                        if coords != None:
                            if len(coords) > 0:
                                Print.log(f'[+] Link {coords}')
                                
                                q = random.randint(int(coords['left']),  int(coords['left'] + coords['width']))
                                w = random.randint(int(coords['top']),  int(coords['top'] + coords['height']))
                                
                                xx, yy = await act.click( x, y, q, w)
                                
                                return xx, yy
                        
                        
                Print.log('[+] Next step Some_DO')
                
                return x, y
                
            except Exception as e:
                Print.error('[+] Error in Some DO')
                Print.error(e)
                
                return 0, 0
