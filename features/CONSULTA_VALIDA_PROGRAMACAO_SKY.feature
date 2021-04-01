@Consulta_Programação_SKY

Feature: Consulta Programação atual SKY 

    Eu como usuario da internet quero acessar site SKY e ver programaçao atual
    
    """Feature Description"""

   Background: Estar no site da SKY
   Given eu esteja na Home Page do site da SKY http://www.sky.com.br
   
   @ConsultaProgramacaoAtual
        Scenario: Consultar programacao atual 
        When clicar no menu programacao
        When clicar na programacao atual
        Then aparecerá modal com informaçoes detalhadas da programaçao atual

   