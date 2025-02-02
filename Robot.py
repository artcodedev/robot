
import sys
sys.path.insert(1, '../')

import time
from Print import Print
import requests
import json
from Sleep import Sleep
import subprocess
import os
from Cookie_ND import Cookie_ND



class Robot:
    
    def __init__(self, id, base_url, url=None) -> None:
        self.id = id
        self.base_url = base_url
        self.url = url
    
    
    def request_m(self, url):
        try:
            
            res = requests.get(f'http://{self.base_url}{url}')
            
            return json.loads(res.text) if res.status_code == 200 else False
        
        except Exception as e:
            Print.error("[+] Error in method request")
            Print.error(e)
            return False
    
    
    def clear_cookie(self):
        
        try:
            
            dir = 'cookies'
            
            list_cookies = os.listdir(dir)
            
            for i in list_cookies:
                
                file = f'{dir}/{i}'
                
                if os.path.getsize(file) < 2300:
                    try: os.remove(file)
                    except: continue
                
            
            Print.log(list_cookies)
        
        except Exception as e:
            Print.error("[+] Error in method clear cookie")
            Print.error(e)
    
    
    def run(self, name_file, data):
        try:
            with open(f'{name_file}.json', 'w+') as f: f.write(json.dumps(data))
            res = subprocess.call(f'python User_ND.py {name_file}', shell=True)
            Print.log('[+] Done.') if res == 0 else  Print.log('[+] Done with error')
        
        except Exception as e:
            Print.error('[+] Error in method RUN')
            Print.error(e)
    
    
    def start(self):
        
        try:
            
            while True:
                
                try:
                    
                    Print.log("[+] Get proxy")
                    proxy = self.request_m("/api/v1/getproxy")
                    
                    if proxy == False: Print.error("[+] Error in get proxy")
                    
                    Print.log(f'[+] Proxy status {proxy['status']}')
                    
                    if proxy and proxy['status']:
                        
                        Print.ok("[+] The request to receive the proxy is successful")
                        
                        behavior = self.request_m(f"/api/v1/behavior/{self.id}")
                        
                        if behavior and behavior['status']:
                            
                            Print.ok("[+] The request to receive the behavior is successful")
                            
                            if behavior['data']['in_work']:
                                
                                Print.log(f"[+] Robot id: {self.id} start walk")
                                
                                data = behavior['data']
                                
                                Print.log("[+] Start visits")
                                
                                for i in data['visits']:
                                    
                                    Print.log(f'[+] Visits url {i['url']}')
                                    
                                    Print.log("[+] Request getconfvisitorurl in visits")
                                    
                                    conf = self.request_m(f"/api/v1/getconfvisitorurl/{i['url']}")
                                    
                                    if conf['status']:
                                        
                                        Print.warning('[+] Status getconfvisitorurl is [ true ]')
                                        
                                        data['proxy'] = proxy['data']['proxy']
                                        data['conf'] = conf['data']
                                        data['base_url'] = self.base_url
                                        
                                        name_file = int(time.time())
                                        
                                        list_cookies = os.listdir("cookies")
                                        
                                        if len(list_cookies) != 0:
                                            
                                            Print.log("[+] Walk in mass cookie")
                                            
                                            for i in range(0, len(list_cookies)):
                                            
                                                data['index_cookie'] = i
                                                data['save_cookie'] = False
                                                
                                                self.run(name_file, data)
                                        
                                        else:
                                            
                                            Print.log("[+] Save new cookies")
                                            
                                            data['index_cookie'] = None
                                            data['save_cookie'] = True
                                            
                                            self.run(name_file, data)
                                        
                                        Print.log("[+] Save new cookies")    
                                        data['index_cookie'] = None
                                        data['save_cookie'] = True
                                        
                                        self.run(name_file, data)
                                        
                                        self.clear_cookie()
   
                                                
                                    else: Print.warning('[+] Status getconfvisitorurl was [ false ]')
                                
                            else:
                                
                                sl = behavior['data']['sleep']
                                
                                Print.log(f"[+] 'in_work' is false ")
                                
                                Sleep.zZz(sl)
                                        
                                Print.log('\n')
                        
                        else: Print.error("[+] The request to receive the behavior is not successful")
                    
                    else: Print.error("[+] The request to receive the proxy is not successful")   
                        
                except Exception as e: Print.error(e)
                
                Sleep.zZz(2)
                # break
            
        except Exception as e:
            Print.error("[+] Error in start method")
            Print.error(e)
        
        

if __name__ == '__main__':
    
    try:
        
        args = sys.argv
        
        if len(args) >= 2:
            
            Print.ok("[+] Start app ROBOT")
            
            Robot(args[1], args[2], None if len(args) <= 3 else args[3]).start()
        
        else:
            Print.error("[+] The program is running without arguments ")
    
    except Exception as e:
        Print.error("[+] Error in main")
        Print.error(e)
    
    