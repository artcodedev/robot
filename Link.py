
from Print import Print
import random
from Executor import Executor
from Scroll import Scroll

class Link:
    
    
    @staticmethod
    async def delete_d(m, close_urls):
        try:
            ms = []
            n_ms = []
            
            if len(m) != 0:
                
                for i in m: ms.append(i.href)
                
                for i1 in ms:
                    
                    if i1 not in close_urls and i1 is not None and i1 not in n_ms: n_ms.append(i1)
            
            return n_ms
        
        except Exception as e:
            Print.error(e)
            return []
    
    
    @staticmethod
    async def link(act, page, xx, yy, close_urls):
        
        try:
        
            hrefs = await page.query_selector_all("a[href]")
            
            m = await Link.delete_d(hrefs, close_urls)
            
            link = m[random.randint(0, len(m) - 1)]
            
            Print.log(f'[+] Link {link}')
            
            link_m = await page.query_selector_all(f"a[href='{link}']")
            
            if len(link_m) != 0:
                
                el_pos = random.randint(0, len(link_m) - 1)
                
                link = f'''a[href='{link}']'''
                
                coords = await Executor.coords(page, link, el_pos )
                
                Print.log(f"[+] Coords link {coords}")
                
                
                padding_top = await page.evaluate("document.documentElement.clientHeight")
                
                ck = True
                counter = 0
                
                view = await page.get_window()
                view_h = view[1].height
                
                while ck:
                    if counter > 10:
                        Print.warning('[+] Counter link scroll > 10')
                        break
                    
                    counter += 1
                    
                    y = int(coords['top'])
                    
                    if y > (view_h - 200):
                        Print.log('[+] y > height view')
                        i = int(y - (view_h / 2))
                        xx, yy = await Scroll.scroll_down(act, page, i, xx, yy)
                    
                    if y < 100:
                        Print.log('[+] y < height view')
                        i = int((y * -1) + padding_top + (padding_top - view_h))
                        xx, yy = await Scroll.scroll_up(act, page, i, xx, yy)
                    
                    if y > 100 and y < (view_h - 200):
                        Print.ok("[+] Scroll completed on element")
                        ck == False
                        break
                    
                    Print.log('[+] Next step while scroll')
                    coords = await Executor.coords(page, link, el_pos)
                    Print.log(f'[+] While coords {coords}')
                    
                coords = await Executor.coords(page, link, el_pos)
                
                if coords['left'] > 0 and coords['top'] > 0:
                    
                    Print.warning(f"[+] Click {coords}")
                    
                    q = random.randint(int(coords['left']),  int(coords['left'] + coords['width']))
                    w = random.randint(int(coords['top']),  int(coords['top'] + coords['height']))
                    
                    if "/games/" in str(link): w = w + 12
                    
                    xx, yy = await act.click( xx, yy, q, w)
                    
            else: Print.warning(f'[+] Can not fiund link {link}')
            
            return xx, yy
        
        except Exception as e:
            Print.error("[+] Error in link method")
            Print.error(e)
            
            return 0, 0