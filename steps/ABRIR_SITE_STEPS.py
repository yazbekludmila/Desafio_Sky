#from selenium import webdriver
from pages.pages.Abrir_Site_Page import Abrir_Site

###################################################################
     
@given(u'eu esteja na Home Page do site da SKY {url}')
def step_impl(context, url):
   #context.app.navigate(url)
   context.abresite.abrir_home()   