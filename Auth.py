

from Print import Print
from Executor import Executor
import random


class Auth:
    
    async def auth(act, page, x, y, auth_data):
        
        try:
            Print.log("[+] Auth")
            
            logged_user = await page.query_selector_all("a[href='/popup-messagebox']")
            
            if len(logged_user) == 0:
                
                popup_login = await page.query_selector_all("a[href='/popup-login']")
                
                if len(popup_login):
                    
                    login = await Executor.coords(page, "a[href='/popup-login']", 0)
                    
                    q = random.randint(int(login['left']),  int(login['left'] + login['width']))
                    w = random.randint(int(login['top']),  int(login['top'] + login['height']))
                    
                    x, y = await act.click(x, y, q, w)
                    
                    await page.sleep(2)
                    
                    type_login = await Executor.coords(page, f"div[data-popup-tabs-name='{auth_data['type']}']", 0)

                    await page.sleep(2)
                    
                    if type_login == None:
                        Print.error(f"[+] Eleme {type_login} not found")
                        return x, y
                    
                    if len(type_login) == 0:
                        Print.error(f"[+] Eleme {type_login} not found")
                        return x, y
                    
                    q1 = random.randint(int(type_login['left']),  int(type_login['left'] + type_login['width']))
                    w1 = random.randint(int(type_login['top']),  int(type_login['top'] + type_login['height']))
                    
                    await page.sleep(2)
                    
                    x, y = await act.click(x, y, q1, w1)
                    
                    await page.sleep(2)
                
                    sign_in = await Executor.coords(page, f"input[id='sign-in-{auth_data['type']}']", 0)
            
                    if sign_in == None:
                        Print.error(f"[+] Eleme {type_login} not found")
                        return x, y
            
                    if len(sign_in) == 0:
                        Print.error(f"[+] Eleme {type_login} not found")
                        return  x, y
                    
                    q = random.randint(int(sign_in['left']),  int(sign_in['left'] + sign_in['width']))
                    w = random.randint(int(sign_in['top']),  int(sign_in['top'] + sign_in['height']))
                    
                    x, y = await act.click(x, y, q, w)
                    
                    await page.sleep(2)
                    
                    sign_in_text = await page.select(f"input[id=sign-in-{auth_data['type']}]")
                    
                    await sign_in_text.send_keys(auth_data['login'])
                    
                    await page.sleep(2)

                    pass_s = 'sign-in-password' if auth_data['type'] == 'email' else f'sign-in-{auth_data['type']}-password'
                    
                    pass_str = f"input[id='{pass_s}']"
                    
                    pass_input = await Executor.coords(page, pass_str, 0)
                    
                    if pass_input == None:
                        Print.error(f"[+] Eleme {pass_s} not found")
                        return 
                    
                    if len(pass_input) == 0:
                        Print.error(f"[+] Eleme {pass_s} not found")
                        return
                    
                    q = random.randint(int(pass_input['left']),  int(pass_input['left'] + pass_input['width']))
                    w = random.randint(int(pass_input['top']),  int(pass_input['top'] + pass_input['height']))
                    
                    x, y = await act.click(x, y, q, w)
                    
                    await page.sleep(2)
                    
                    pass_in_text = await page.select(pass_str)
                    
                    await pass_in_text.send_keys(auth_data['pass'])
                    
                    await page.sleep(2)
                    
                    submit = await Executor.coords(page, f"button[data-test='submit_button']", 0)
            
                    if submit == None:
                        Print.error(f"[+] Eleme {submit} not found")
                        return x, y
            
                    if len(submit) == 0:
                        Print.error(f"[+] Eleme {submit} not found")
                        return x, y
            
                    q = random.randint(int(submit['left']),  int(submit['left'] + submit['width']))
                    w = random.randint(int(submit['top']),  int(submit['top'] + submit['height']))
                    
                    x, y = await act.click(x, y, q, w)
                    
                    await page.sleep(4)
                
                else: Print.error("[+] Eleme /popup-login not found")
            
            else: Print.log("[+] User is not logged")
            
            Print.ok('[+] Auth done')
            
            return x, y
        
        except Exception as e:
            Print.error("[+] Error in method auth")
            Print.error(e)
            
            return 0, 0