import asyncio
import os
from playwright.async_api import async_playwright

async def create_vm():
    print("?? Jarvis: Initiating Direct Cloud Connection...")
    user_data = os.path.join("C:\\Jarvis", "user_data")
    
    async with async_playwright() as p:
        # Launching a standard browser with your session
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=user_data, 
            headless=False,
            viewport={'width': 1280, 'height': 720}
        )
        page = await browser.new_page()
        
        print("??? Jarvis: Navigating to Google Cloud...")
        # Direct link to Instance Creation
        await page.goto("https://console.cloud.google.com/compute/instancesAdd", wait_until="domcontentloaded")
        
        print("?? ACTION REQUIRED:")
        print("1. If prompted, select your project 'Jarvis-Core-Project'.")
        print("2. Jarvis is keeping the window open for 10 minutes.")
        print("3. Please verify the 'e2-micro' selection and click 'CREATE' at the bottom.")
        
        # Keep window open for you to finish the 'Human' verification
        await asyncio.sleep(600) 
        await browser.close()

if __name__ == '__main__':
    asyncio.run(create_vm())
