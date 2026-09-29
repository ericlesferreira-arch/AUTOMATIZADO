from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
from funcoes import gerar_nome_tr
import time

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
# ============================================================
USUARIO_PRINCIPAL = 'ericles.magno'
USUARIO_EPC       = 'julyson.santos'   
SENHA_PADRAO      = '12345'
# ============================================================# 


def TermoReferencia(driver):

    logger = setup_logger()


    #Logout do usuário GESTOR para logar com usuário EPC
    try:
        logger.info('Deslogando')

        Menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar.click()
        time.sleep(1)

        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        Sair.click()
        time.sleep(1)

        logger.info('Logando com usuário principal')
        Campo_login2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login2usuario.click()
        Campo_login2usuario.clear()
        Campo_login2usuario.send_keys(USUARIO_EPC)

        campo_senha2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha2usuario.click()
        campo_senha2usuario.send_keys(SENHA_PADRAO)

        botao_entrar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar2.click()
        time.sleep(2)

        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(1)

        logger.info('Autenticação Concluída')

    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise




    ## ETAPA: CRIAR TERMO DE REFERÊNCIA 

    try:
        menuTermoreferencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[3]/a/span'))
        )
        menuTermoreferencia.click()


        submenu_RegistroTermoReferencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[3]/div/a[1]'))
        )
        submenu_RegistroTermoReferencia.click()
        time.sleep(1)


        Botao_NovoTR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-list/p-table/div/div[1]/div/a/i'))
        )
        logger.info('Iniciando Termo Referencia')
        Botao_NovoTR.click()
        time.sleep(1)


        campo_demanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[1]/div[1]/select/option[3]'))
        )
        campo_demanda.click()


        ##============ AQUI, POR ENQUANTO SEMPRE O ULTIMO ETP SERÁ O PRIMEIRO TR, ENTÃO, SEMPRE INDICE 1
        
        Opcão_demanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[1]/div[1]/select/option[1]'))
        )
        Opcão_demanda.click()
        time.sleep(1)



        Descricao_TR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[3]/div[1]/input'))
        )
        Descricao_TR.click()
        nome_tr = gerar_nome_tr()
        Descricao_TR.send_keys(nome_tr)
        time.sleep(1)



        campo_regimeExecucao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[4]/div[2]/select'))
        )
        campo_regimeExecucao.click()
        time.sleep(1)


        opcao_regimeExecucao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[4]/div[2]/select/option[2]'))
        )
        opcao_regimeExecucao.click()


        campo_adjudicacaoObjeto = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[4]/div[3]/select'))
        )
        campo_adjudicacaoObjeto.click()
        time.sleep(1)

        opcao_adjudicacaoobjeto = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/div/div/div[4]/div[3]/select/option[2]'))
        )
        opcao_adjudicacaoobjeto.click()
        time.sleep(1)

        ## REALIZANDO O ENVIO DIRETO, POIS, APENAS A ABA DADOS BÁSICOS É DE PREENCHIMENTO OBRIGATÓRIO

        botao_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-dados-basicos/form/button[1]'))
        )
        botao_enviar.click()

        time.sleep(3)

        logger.info('Termo de Referencia enviado com sucesso')

    except Exception: 
        logger.exception('❌ Falha ao envair TR')
        raise



    ## DESLOGANDO COM EPC PARA LOGAR COM GESTOR (RESPONSÁVEL PELA VALIDAÇÃO)



    try:
        logger.info('Deslogando')
    
        Menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar.click()
        time.sleep(1)
    
        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        Sair.click()
        time.sleep(1)
    
        logger.info('Logando com usuário principal')
        Campo_login2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login2usuario.click()
        Campo_login2usuario.clear()
        Campo_login2usuario.send_keys(USUARIO_PRINCIPAL)
    
        campo_senha2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha2usuario.click()
        campo_senha2usuario.send_keys(SENHA_PADRAO)
    
        botao_entrar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar2.click()
        time.sleep(2)
    
        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(1)
    
        logger.info('Autenticação Concluída')
    
    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise




    # ETAPA - VALIDAR TERMO REFERENCIA 


    try:
        menu_TermoReferencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[3]/a/span'))
        )
        menuTermoreferencia.click()


        submenu_ValidarTR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[3]/div/a[2]'))
        )
        submenu_ValidarTR.click()
        time.sleep(1)


        campo_descricao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-validacao-list/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]'))
        )
        campo_descricao.click()
        campo_descricao.send_keys(nome_tr)
        time.sleep(1)


        Acessar_documento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By. XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-validacao-list/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]/a'))
        )
        Acessar_documento.click()
        time.sleep(1)


        campo_validacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-aprovacao-atual/form/div/div/div[3]/div[3]/select'))
        )
        campo_validacao.click()


        opcao_validacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-aprovacao-atual/form/div/div/div[3]/div[3]/select/option[1]'))
        )
        opcao_validacao.click()


        botao_registrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-termo-referencia-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-termo-referencia-aprovacao-atual/form/button[1]'))
        )
        botao_registrar.click()
        time.sleep(8)

        logger.info('Validação Termo Referencia Concluída')

    except Exception: 
        logger.exception('❌ Falha ao validar Termo Referencia')
        raise




    
    #Logout do usuário GESTOR para logar com usuário EPC
    
    try:
        logger.info('Deslogando')
    
        Menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar.click()
        time.sleep(1)
    
        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        Sair.click()
        time.sleep(1)
    
        logger.info('Logando com usuário principal')
        Campo_login2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login2usuario.click()
        Campo_login2usuario.clear()
        Campo_login2usuario.send_keys(USUARIO_EPC)
    
        campo_senha2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha2usuario.click()
        campo_senha2usuario.send_keys(SENHA_PADRAO)
    
        botao_entrar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar2.click()
        time.sleep(2)
    
        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(1)
    
        logger.info('Autenticação Concluída')
    
    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise





    ## ETAPA: Assinatura Termo Referencia (EPC)


    try:

        menu_Planejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/a/span'))
        )
        menu_Planejamento.click()


        submenu_Assinatura = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/div/a[3]'))
        )
        logger.info('Iniciando a Assinatura')
        submenu_Assinatura.click()


        campo_descricao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]'))
        )
        campo_descricao.click()
        campo_descricao.send_keys(nome_tr)
        time.sleep(1)


        botao_assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/button[1]/img'))
        )
        botao_assinar.click()


        campo_senha = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[2]/div/div[2]/input'))
        )
        campo_senha.click()
        campo_senha.send_keys('12345')


        botao_assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_assinar.click()
        time.sleep(2)


        logger.info('Assinatura EPC concluída')

    except Exception:
        logger.exception('❌ Falha na assinatura do TR (EPC)')
        raise

    
        ## Deslogando com EPC para logar com GESTOR 

    try:
        logger.info('Deslogando')
        
        menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar.click()
        time.sleep(1)
        
        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        Sair.click()
        time.sleep(1)
        
        logger.info('Logando com usuário principal')
        Campo_login2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login2usuario.click()
        Campo_login2usuario.clear()
        Campo_login2usuario.send_keys(USUARIO_PRINCIPAL)
        
        campo_senha2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha2usuario.click()
        campo_senha2usuario.send_keys(SENHA_PADRAO)
        
        botao_entrar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar2.click()
        time.sleep(2)
        
        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(1)
        
        logger.info('Autenticação Concluída')
        
    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise

    


    
    ## ETAPA: Assinatura Termo Referencia (EPC)


    try:

        menu_Planejamento1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/a/span'))
        )
        menu_Planejamento1.click()
        
        
        submenu_Assinatura1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/div/a[3]'))
        )
        logger.info('Iniciando a Assinatura')
        submenu_Assinatura1.click()
        
        
        campo_descricao1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]'))
        )
        campo_descricao1.click()
        campo_descricao1.send_keys(nome_tr)
        time.sleep(1)
        
        
        botao_assinar1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/button[1]/img'))
        )
        botao_assinar1.click()
        
        
        campo_senha1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[2]/div/div[2]/input'))
        )
        campo_senha1.click()
        campo_senha1.send_keys('12345')
        
        
        botao_assinar1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_assinar1.click()
        time.sleep(2)

        logger.info('Assinatura Concluída (Gestor)')

    except Exception:
        logger.exception('Falha ao Assinar Termo Referencia (gestor)')
        raise

