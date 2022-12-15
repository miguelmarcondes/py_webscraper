from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def autenthication():
    page.goto('thewebsite')
    page.fill('input#textUser', 'yourlogin')
    page.fill('input#textSenha', 'yourpassword')
    page.click('button[type=button]')
    page.get_by_text("some element behind the captcha").wait_for()
    page.goto('anotherpage')
    page.fill('input[type=input]', 'another auth')
    page.fill('input[type=password]', 'another auth')
    page.locator('text=Entra').click()
    page.goto('specific page')

def adjust_link(var):
    link = 'link&that&uses&&to&divide&variables&unfriendly&'
    array_var_value = link.split('&')
    for i in array_var_value:
        var.append(i.split('=', 1)[0])
    
    return var

feature_name = 'input_needed'
char_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
char_list = ['%26', '%22', '%27', '%3C', '%\3E', '<', '>', '\'', '\"']
variables_list = []
variable = 0
i = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    autenthication()
    page.fill('input#textFerramentas', feature_name)
    adjust_link(variables_list)
    while variable < len(variables_list):
        for char in char_index:
            page.fill('input#textVariavel', variables_list[variable])
            page.select_option("select#CHARS", char)
            page.locator('text=Carregar').click()   
            page.get_by_text('Número').wait_for()
            html = page.inner_html('#tabela_resultado_sql')
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.find('caption', text = "Número de registros encontrados: 0")
            if not text == None:
                print(feature_name + ": o caractere " + char_list[i] + " da variável " + variables_list[variable] + " passou!")
            else:
                print(feature_name + ": o caractere " + char_list[i] + " da variável " + variables_list[variable] + " não passou!")
            i += 1
        i = 0
        variable += 1