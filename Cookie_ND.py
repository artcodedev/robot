

from Print import Print
import time
import os
from pathlib import Path
from nodriver import cdp
# from nodriver.cdp import network
import pathlib
import pickle
# from nodriver.core.browser import CookieJar 

class Cookie_ND:
    
    dir = 'cookies'
    
    @staticmethod
    async def ch_path():
        
        try:
        
            Print.log("[+] Check cookie file")
            
            path_cookies = Path(Cookie_ND.dir)
            
            if not path_cookies.exists(): os.mkdir(path_cookies)
            
            return True if path_cookies.exists() else False
        
        except Exception as e:
            Print.error('[+] Error in ch_path method')
            Print.error(e)
            return False
    
    
    @staticmethod
    async def saveCookie(br, ch, host, t = None):
        
        try:
            
            Print.log('[+] Get cookie ')
            
            if await Cookie_ND.ch_path():
            
                Print.log("[+] Save cookies ++") 
                
                file = f"{Cookie_ND.dir}/{ch}.{host}.{str(int(time.time()))}.dat"
                
                save_path = pathlib.Path(file).resolve()
                
                connection = br.connection
                cookies = await connection.send(cdp.storage.get_cookies())
                Print.log(cookies)
                pickle.dump(cookies, save_path.open("w+b"))
                
        except Exception as e:
            Print.error('[+] Error in setCookie method')
            Print.error(e)
            return False
    
    
    @staticmethod
    async def setCookie(br, ch, host, index):
        try:
            
            if await Cookie_ND.ch_path():
                
                list_cookies = os.listdir(Cookie_ND.dir)
               
                if len(list_cookies) > 0:
                   
                    m_co = []
                            
                    for i in list_cookies:
                        if i.find(ch) != -1 and i.find(host) != -1: m_co.append(i)
                    
                    if len(m_co) != 0:
                        
                        Print.log('[+] Сookie file found')
                        
                        if len(m_co) != 0:
                            file = m_co[index]
                    
                            save_path = pathlib.Path(f"{Cookie_ND.dir}/{file}").resolve()
                            cookies = pickle.load(save_path.open("r+b"))
                            await br.connection.send(cdp.storage.set_cookies(cookies))
                            return file

                            
                    else: Print.warning("[+] Cookie not found")
                        
                else: Print.warning("[+] Cookie dir is Null")
                
                return False
        
                
        except Exception as e:
            Print.error('[+] Error in getCookie method')
            Print.error(e)
    
    
    @staticmethod
    async def clear_cookie():
        
        try: 
            if await Cookie_ND.ch_path():

                list_cookies = os.listdir(Cookie_ND.dir)
                
                Print.log(list_cookies)
        
        except Exception as e:
            Print.error("[+] Error in method clear_cookie")
            Print.error(e)
    