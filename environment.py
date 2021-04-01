
"""		Pyautomator Framework de teste 

			saraivatestes"""

from selenium import webdriver
from Pyautomators import fixture
from webautomators import WebChromeDriver
from webautomators.extended_options import WebChromeOptions
##from pages.pages.HomeSaraivaPage import Procura_Compra_Produto
##from pages.pages.LoginSaraivaPage import Fazer_Login_Saraiva
##from pages.pages.FreteSaraivaPage import Escolher_Frete
##from pages.pages.PagamentoPage import Fazer_Pagamento

from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Consultar_Programacao_Atual_Page import Consultar_Validar_Programacao_Atual

def before_all(context):
	options = WebChromeOptions()
	options.maximized()
	context.app = WebChromeDriver(executable_path='C:\drivers\chromedriver.exe', options=options)
	#context.app = WebChromeDriver(executable_path='C:\Users\Ludmila\Documents\A4_YOU_SEE\DESAFIO_4_YOU_SEE\saraivatestes\driver\chromedriver.exe', options=options)
	
	context.ConsultaValidaConteudo = Consultar_Validar_Programacao_Atual(context.app)

	context.abresite  = Abrir_Site(context.app)
	
	context.pages = {
	#    "login": "http://www.sky.com.br"
	#	"login": "https://www.saraiva.com.br/checkout/onepage/"
	#	"login": "https://www.saraiva.com.br/checkout/onepage/",
	#	"frete": "https://www.saraiva.com.br/checkout/onepage/",
	#	"pagamento": "https://www.saraiva.com.br/checkout/onepage/"
	}

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

#def after_all(context):
#	context.driver.quit()

#def before_all(context):
#	context.app=webdriver.Chrome('driver/chromedriver.exe')
#	context.page=HomeSaraiva(context.app)