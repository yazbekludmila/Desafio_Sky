from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Abrir_Site():

    def __init__(self, app):
        self.app = app
        #self.pagina('http://www.sky.com.br')

    def abrir_home(self):
        self.app.get('http://www.sky.com.br')
        
    def fechar_janela_aviso(self):
       #X_janela_aviso_inicial = self.app.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_YQcCxObpxg0J"]/div/div[2]/div/div[2]/div/div/div/div[1]/button').click()
     # self.app.execute_script('window.scrollTo( 0, 190000 );')
       sleep(16)
       #janela_aviso_inicial = self.app.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_YQcCxObpxg0J"]/div/div[2]/div/div[2]/div/div/div/div[1]/button/span').click()
       sleep(6)
         
        

    