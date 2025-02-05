def capture_screenshot(page, name):
    page.screenshot(path=f'reports/{name}.png')