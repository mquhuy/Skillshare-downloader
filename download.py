from selenium import webdriver
import requests
from selenium.webdriver.firefox.options import Options
import os
import time
from sys import argv
import concurrent.futures
from account import USR, PW

def downloadvideo(url, filename, file_number):
    global driver
    global foldername
    saved_file = '{}/{}. {}.mp4'.format(foldername, file_number, filename)
    if not os.path.isfile(saved_file):
        video_file = requests.get(url, stream=True)
        open(saved_file, 'wb').write(video_file.content)
        print('"{}" downloaded.'.format(filename))
    else:
        print("Passed existing file {}".format(filename))

def get_video_list(list_url):
    global driver
    global foldername
    driver.get(list_url)
    foldername = driver.find_element_by_class_name('class-details-header-name').text
    if not os.path.isdir(foldername):
        os.makedirs(foldername)
    session_items = driver.find_elements_by_class_name('session-item')
    numbers = []
    links = []
    titles = []
    for item in session_items:
        video_number = item.find_element_by_class_name('completion-button').get_attribute('data-rank')
        video = item.find_element_by_class_name('session-item-title')
        title = video.text
        video.click()
        url = driver.find_element_by_class_name('vjs-tech').get_attribute('src')
        links.append(url); titles.append(title); numbers.append(video_number)
    return links, titles, numbers

def download_video_list(links, titles, numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(downloadvideo, links, titles, numbers)
    
def get_driver():
    options = Options()
    options.set_headless(True)
    options.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_options=options)
    driver.get('https://www.skillshare.com/login?via=homepage')
    username = driver.find_element_by_class_name('login-form-email-input')
    username.send_keys(USR)
    password = driver.find_element_by_class_name('login-form-password-input')
    password.send_keys(PW)
    login = driver.find_element_by_class_name('btn-login-submit')
    time.sleep(10)
    login.click()
    time.sleep(10)
    return driver


if __name__ == '__main__':
    driver = get_driver()
    list_url = argv[1]
    links, titles, numbers = get_video_list(list_url)
    download_video_list(links, titles, numbers)
    print('All done')
    driver.close()