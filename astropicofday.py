#Ben Jennings

#1. Save image from astropix.

import urllib
from bs4 import BeautifulSoup
import ctypes

base_url = 'https://apod.nasa.gov/apod/astropix.html'

def url_resp(url):
    
    '''
    Returns HTML response of url request.
    '''
    
    resp = urllib.request.urlopen(url).read().decode('utf8')
    
    return resp

def parser(resp):
    
    '''
    Parses the HTML response string.
    '''
    
    parsed_resp = BeautifulSoup(resp, "html.parser")
    
    return parsed_resp

def url_img(parsed_resp):
    
    '''
    Retrieves url extension of current image.
    '''
    
    links = parsed_resp.find_all('a')
    
    image_link = links[1].get('href')

    return image_link

#saving image

x = url_resp(base_url) 
y = parser(x)
z = url_img(y)

#removing / from z and taking last element for file name.

file_name = z.split('/')[-1]

base_img_url = 'https://apod.nasa.gov/apod/'

#file path to save img
PATH = 'C:/Users/bench/Documents/personal_projects/astropicofday' + '/' + file_name

resource = urllib.request.urlopen(base_img_url+z)
output = open(PATH,'wb')
output.write(resource.read())
output.close()

#setting wallpaper as such!

SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)