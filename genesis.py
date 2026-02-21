import asyncio
import os
from playwright.async_api import async_playwright

async def deploy_jarvis():
    print("?? Jarvis: Initiating Project Genesis...")
    auth_file = "C:\\Jarvis\\auth.json"
    
    async with async_playwright() as p:
        # Launching with your saved 'Key'
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state=auth_file)
        page = await context.new_page()
        
        print("??? Jarvis: Accessing the Cloud Command Center...")
        await page.goto("https://console.cloud.google.com/compute/instancesAdd")
        
        print("?? TASK: Jarvis is setting up the hardware.")
        print("?? If Google asks you to 'Select a Project', please click 'Jarvis-Core-Project' on the screen.")
        
        # We stay open for 10 minutes so you can watch or help if a popup appears
        await asyncio.sleep(600) 
        await browser.close()

if __name__ == '__main__':
    asyncio.run(deploy_jarvis())
