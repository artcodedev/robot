

import sys
import asyncio
import nodriver as uc
import nodriver
import json
import random
import os
import nodriver.core.element
import time
import datetime
from Print import Print
from Cookie_ND import Cookie_ND
from Sleep import Sleep
from Actions import Actions
from Move import Move
from Scroll import Scroll
from Some_DO import Some_DO
from Link import Link
from Scroll_RA import Scroll_RA
from Reload import Reload
from Auth import Auth




class User_ND:
    
    def __init__(self, url, move, experience, auth, movement, proxy, auth_data, conf, base_url, utm=False, cookie=False, save_cookie=False, index_cookie=None) -> None:
        self.url = url
        self.move = move
        self.experience = experience
        self.auth = auth
        self.movement = movement
        self.proxy = proxy
        self.error = 0
        self.conf = conf
        self.auth_data = auth_data
        self.base_url = base_url
        self.utm = utm
        self.cookie = cookie
        self.extention = f'--load-extension={os.getcwd()}\\0.3.2_0'
        self.save_cookie = save_cookie
        self.index_cookie = index_cookie
        self.cursor_x = 0
        self.cursor_y = 0
    
    
    async def launch_browser(self):
        try:
            self.browser = await uc.start(
                headless=True,
                 browser_args=[
                    
                    self.extention,
                    # "--window-size=1300,1000"
                    # '--start-maximized'
                    ]
            )
        except Exception as e:
            Print.error(f"[+] Failed to launch browser: {e}")
            raise
        
        
        return self.browser


    async def launch_proxy_browser(self, ipPort, username, password):
        try:
            self.browser = await uc.start(
                headless=True,
                browser_args=[
                    f"--proxy-server={ipPort}",
                    self.extention,
                    # "--window-size=1300,1000"
                    # '--start-maximized'
                    ]
            )

            self.username = username
            self.password = password

            self.main_tab = await self.browser.get("draft:,")
            
            self.main_tab.add_handler(uc.cdp.fetch.RequestPaused, self.req_paused)
            
            self.main_tab.add_handler(uc.cdp.fetch.AuthRequired, self.auth_challenge_handler)
            
            await self.main_tab.send(uc.cdp.fetch.enable(handle_auth_requests=True))
            
            return self.browser
        
        except Exception as e:
            Print.error(f"[+] Failed to launch proxy browser: {e}")
            raise


    async def auth_challenge_handler(self, event: uc.cdp.fetch.AuthRequired):
        try:
            asyncio.create_task(
                self.main_tab.send(
                    uc.cdp.fetch.continue_with_auth(
                        request_id=event.request_id,
                        auth_challenge_response=uc.cdp.fetch.AuthChallengeResponse(
                            response="ProvideCredentials",
                            username=self.username,
                            password=self.password,
                        ),
                    )
                )
            )
        except Exception as e:
            Print.error(f"[+] Error handling authentication challenge: {e}")


    async def req_paused(self, event: uc.cdp.fetch.RequestPaused):
        try:
            asyncio.create_task(
                self.main_tab.send(
                    uc.cdp.fetch.continue_request(request_id=event.request_id)
                )
            )
        except Exception as e:
            Print.error(f"[+] Error while continuing paused request: {e}")
    
    
    async def walk(self) -> bool:
        
        try:
        
            Print.ok('[+] Next step')
            
            range_walk = random.randint(1, 2)
            
            Print.log(f'[+] Range walk {range_walk}')
        
            self.cursor_x, self.cursor_y = await Some_DO.some_do(self.actions, self.page, self.conf['some_do']['check_el'], self.cursor_x, self.cursor_y)
            
            for _ in range(0, range_walk):
                event = ["scroll", "move", "auth"]
        
                Print.log('[+] Get random behavior')
                event_el = event[random.randint(0, len(event) - 1)]
                
                if event_el == 'scroll':
                    self.cursor_x, self.cursor_y = await Scroll_RA.random(self.actions, self.page, self.cursor_x, self.cursor_y)
                
                if event_el == 'move':
                    self.cursor_x, self.cursor_y = await Move.move(self.actions, self.page, self.cursor_x, self.cursor_y)
                
                if event_el == 'auth':
                    self.cursor_x, self.cursor_y = await Auth.auth(self.actions, self.page, self.cursor_x, self.cursor_y, self.auth_data)
            
            try:
                
                self.cursor_x, self.cursor_y = await Link.link(self.actions, self.page, self.cursor_x, self.cursor_y, self.conf['close_urls'])
            
            except Exception as e:
                Print.error("[+] Error in Click link")
                Print.error(e)
            
            Print.log('\n')
            Sleep.zZz(random.randint(7, 10))
            Print.log('\n')
            
            try:
                 
                self.cursor_x, self.cursor_y = await Reload.reload(self.actions, self.page, self.cursor_x, self.cursor_y)
                
            except Exception as e:
                Print.error("[+] Can not reload page")
                Print.log(e)
            
            Print.log('\n')
            Sleep.zZz(random.randint(7, 10))
            Print.log('\n')
            
            return True
        
        except Exception as e:
            Print.error(e)
            return False
    
     
    async def run(self):
        
        try:
            
            Print.log('[+] Start User')
            
            Print.log(f"[+] Date: {datetime.datetime.now()}")
            
            # without proxy
            # self.driver = await self.launch_browser()

            # use proxy
            self.driver = await self.launch_proxy_browser(f'{self.proxy['ip']}:{self.proxy['port']}', self.proxy['login'], self.proxy['pass']) 
            
            self.page = self.driver
            
            url = self.url['url']
        
            url__s = self.conf['start_urls']

            url_start = url__s[random.randint(0, len(url__s) - 1)] if len(url__s) > 1 else url__s[0]

            move = self.movement['move']

            _s_url = f"{url}{url_start}"
                
            _s_url = _s_url if 'http' in _s_url else f'https://{_s_url}'
            
            Print.log(f"[+] Set cookie type {self.cookie}")
            if self.save_cookie is False:
                
                if self.cookie:
                    
                    Print.log("[+] Set cookies")
                        
                    self.cookie = await Cookie_ND.setCookie(self.driver, "chrome", self.url['url'], self.index_cookie)
            
            
            self.page = await self.driver.get(_s_url)
            
            Sleep.zZz(random.randint(3,4))
            self.actions = Actions(move['mousemove'], move['scroll'], self.page)
            
            if self.save_cookie:
            
                Print.warning("[+] Save cookie")
                Sleep.zZz(random.randint(7,9))  
                
                await Cookie_ND.saveCookie(self.browser, "chrome", self.url['url'], None)
                
                await self.page.close()
                self.browser.stop()
                
                return False
                
            time_s = self.url['time']
                
            time_s = random.randint(int(time_s[0]), int(time_s[1]))
                
            Print.log(f"[+] Time walk {time_s}")
                
            time_s = int(time.time()) + time_s
                
            Print.log(f'[+] Full time in sec {time_s}')

            
            while time_s > int(time.time()):
                    
                if self.error > 5:
                    Print.error('[+] Error limit exceeded')
                    return False
                    
                res = await self.walk()
                    
                if res: Print.ok('[+] Walk without mistakes')
                    
                else:
                    Print.error("[+] Walk with mistakes")
                    self.error += 1
                    
                res = None
                
                Print.ok("[+] Time walk is done.")
                
            await self.page.close()
                
            return True
        
        except Exception as e:
            Print.error("[+] Error in method start User_ND")
            Print.error(e)
            
            if self.page != None: await self.page.close()
            
            return False
    
          
    def start(self):
        
        try:
            
            uc.loop().run_until_complete(self.run())
            
        except Exception as e:
            Print.error(e)
    

if __name__ == "__main__":
    
    name_file = None

    try:
        args = sys.argv
        
        name_file = f'{args[1]}.json'
        
        def readfile(file):
            try: 
                
                with open(file, 'r') as f: return json.loads(f.read())
                
            except Exception as e:
                Print.log(e)
                return None
        
        data = readfile(name_file)
        
        if data != None:
            
            os.remove(name_file)
            
            user = User_ND(
                data['url'],
                data['move'],
                data['experience'],
                data['auth'],
                data['movement'],
                data['proxy'],
                data['auth_data'],
                data['conf'],
                data['base_url'],
                data['utm'],
                data['cookie'],
                data['save_cookie'],
                data['index_cookie']                   
            )
            
            user.start()
        
        else:
            Print.warning("[+] Can not get data file")
            os.remove(name_file)
        
    except Exception as e:
        Print.error("[+] Error in main User_ND")
        Print.error(e)
        
        try:
            
            if name_file != None: os.remove(name_file)
        
        except Exception as ee:
            Print.error(f"[+] Can not delete file {name_file}")
            Print.error(ee)
