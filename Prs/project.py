from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchShadowRootException

google = webdriver.Chrome()
google.get('https://www.google.com');

def search_for_somthing():
    path = google.find_element(By.XPATH , "//textarea[@id='APjFqb']");
    string = "youtube"
    for this in string:
        path.send_keys(this)
    path.send_keys(Keys.ENTER)
    sleep(1)

def for_select(var : any):
    this = google.find_element(By.PARTIAL_LINK_TEXT, var)
    this.click()

def search_for_what_you_want(search: any):
    this = google.find_element(By.XPATH, "//input[@id='search']")
    for se in search:
        this.send_keys(se);
    this.send_keys(Keys.ENTER)

def to_delete():
    this = google.find_element(By.XPATH, "//input[@id='search']")
    this.send_keys(Keys.BACKSPACE * 100)

def home_page():
    this = google.find_element(By.XPATH, "//ytd-topbar-logo-renderer[@id='logo']//div[@class='style-scope ytd-topbar-logo-renderer']//div")
    this.click()

search_for_somthing()
for_select("YouTube: Accueil")
serch_flag = 0
while (1):
    if serch_flag == 0:
        what = input("Please what Do you want.. ? ")
        search_for_what_you_want(what)
        sleep(1)
        elements = google.find_elements(By.XPATH, "(//yt-formatted-string[@class='style-scope ytd-video-renderer'])")
        index = 0
        store_in_array = []
        for element in elements:
            store_in_array.append(element.text)
            index += 1;
        flag = 0
        while flag < index:
            if (len(store_in_array[flag]) != 0):
                print([flag] ,store_in_array[flag], "\n")
            flag += 1
        for_you = input(" Enter the number of the title u wanna install ... ")
        takeit = 0
        while (not for_you.isdigit()):
            for_you = input(" Enter the number of the title u wanna install ... ")
            takeit = int(for_you)
        this = google.find_element(By.PARTIAL_LINK_TEXT, store_in_array[takeit])
        print("\nYou choose ->"+ store_in_array[takeit])
        this.send_keys(Keys.ENTER)
    wanna_res = input("Wnnna Search again ...? y | n\n")
    if (wanna_res == 'y'):
        serch_flag = 0
        home_page()
        store_in_array = []
        what = ''
        for_you = ''
    else:
        serch_flag = 1
    input()
check = input("wanna delet")
if check == '1':
    to_delete()
    check = ""
check = input(" Enter here ")
if check == ' ':
    home_page()