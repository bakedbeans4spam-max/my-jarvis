from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import os
import time

def create_project():
    print("?? Jarvis: Starting Project Creation Protocol...")
    user_data = os.path.join("C:\\Jarvis", "user_data")
    
    with sync_playwright() as p:
        # Load the session Jarvis just saved
        browser = p.chromium.launch_persistent_context(user_data, headless=False)
        page = browser.new_page()
        stealth_sync(page)
        
        # Navigate to the Project Selector
        page.goto("https://console.cloud.google.com/projectselector2/home/dashboard")
        time.sleep(5) # Wait for session to load
        
        try:
            print("??? Jarvis: Attempting to create 'Jarvis-Core-Project'...")
            # Click the 'Create Project' button
            page.click("button[aria-label='Create Project'], button:has-text('NEW PROJECT')")
            
            # Fill in project details
            page.fill("input[name='name']", "Jarvis-Core-Project")
            
            # Click Create
            page.click("button:has-text('CREATE')")
            
            print("? Jarvis: Project creation initiated! I am waiting for Google to finish provisioning...")
            time.sleep(15) 
            print("?? Jarvis: Mission Accomplished. Your Google Cloud environment is ready.")
            
        except Exception as e:
            print(f"? Jarvis: Encountered an obstacle: {e}")
        
        browser.close()

if __name__ == '__main__':
    create_project()
