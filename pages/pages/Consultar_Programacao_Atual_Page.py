from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Consultar_Validar_Programacao_Atual():

    def __init__(self, app):
        self.app = app
        
    def selecionar_menu_programação(self):

        # seleciona fechar janela aviso 
        janela_aviso  = self.app.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_YQcCxObpxg0J"]/div/div[2]/div/div[2]/div/div/div/div[1]/button/span').click()
        ##sleep(6)
        
        # seleciona menu programacao 
        menu_programacao = self.app.find_element_by_xpath('//*[@id="main-menu"]/div[2]/div[2]/ul[1]/li[3]/a/strong').click()
        sleep(2)
       ##################
       
    def selecionar_programação_atual(self):
        
        sleep(5)
        self.app.execute_script('window.scrollTo( 0,1100 );')
        sleep(5)
        
        #campo "agora"
        campo_agora = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[1]/span').click()
        sleep(5)

        # TITULO TELA PRINCIPAL  
        TITULO_TELA_PRINCIPAL = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/h2')
        content_titulo_principal = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/h2').text
           
        # HORA TELA PRINCIPAL  
        HORA_TELA_PRINCIPAL = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]')
        content_hora__principal = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]').text

        #CLICAR NO TITULO TELA PRINCIPAL = ABRE MODAL COM DETALHES DA PROGRAMACAO
        TITULO_TELA_PRINCIPAL = self.app.find_element_by_xpath('//*[@id="schedules-container"]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/h2').click()
        sleep(5)

        ## CAPTURAR INFORMAÇÕES JANELA DETALHES DA PROGRAMACAO ATUAL

        # TITULO JANELA  DETALHES DA PROGRAMACAO ATUAL
        TITULO_JANELA_DETALHE = self.app.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/h2')
        content_titulo_janela = self.app.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/h2').text              
        
        # HORA  JANELA  DETALHES DA PROGRAMACAO ATUAL# HORA TELA PRINCIPAL  
        HORA_JANELA_DETALHE = self.app.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]')
        content_hora_janela = self.app.find_element_by_xpath('//*[@id="modal"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]').text
        sleep(5)

##def validar_programa_atual(self):   

        ### VALIDAR TITULO PROGRAMAÇAO TELA PRINCIPAL = TITULO DA JANELA DETALHE 
        assert content_titulo_principal  == content_titulo_janela
        
        ### VALIDAR HORA PROGRAMAÇAO TELA PRINCIPAL = HORA  DA JANELA DETALHE 
        assert content_hora__principal == content_hora_janela
        #sleep(6)

        ### FECHAR MODAL DETALHES DA PROGRAMAÇAO

        FECHA_MODAL = self.app.find_element_by_xpath('//*[@id="modal"]/div/div[1]/button/span[2]').click()
        sleep(1)