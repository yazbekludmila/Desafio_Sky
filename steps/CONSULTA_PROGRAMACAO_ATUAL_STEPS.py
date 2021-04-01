#from selenium import webdriver
from pages.pages.Abrir_Site_Page import Abrir_Site
    
@when(u'clicar no menu programacao')
def step_impl(context):
   context.ConsultaValidaConteudo.selecionar_menu_programação()

@when(u'clicar na programacao atual')
def step_impl(context):
   context.ConsultaValidaConteudo.selecionar_programação_atual()
  
@then(u'aparecerá modal com informaçoes detalhadas da programaçao atual')
def step_impl(context):
   pass
   ##context.ConsultaValidaConteudo.validar_programa_atual()