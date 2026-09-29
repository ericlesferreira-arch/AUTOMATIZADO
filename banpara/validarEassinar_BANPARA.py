from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import setup_logger
import time

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
# ============================================================
USUARIO_PRINCIPAL   = 'Ericles.magno'
USUARIO_RESPONSAVEL = 'Claudio.magno'   
USUARIO_AUTORIDADE  = 'Teste.qa'   
USUARIO_EPC         = 'Julyson.santos'    
SENHA_PADRAO        = '12345'
# ============================================================ #


## Nessa tela tem 3 alterações, Se atentar aos Send_Keys dos campos de Busca 

def validarEassinar(driver, nome_demanda):

    logger = setup_logger()

    try:
        menu_DemandasTC = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-7"]/span'))
        )
        menu_DemandasTC.click()
        time.sleep(1)

        submenu_validarDemanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[1]/div/a[2]'))
        )
        submenu_validarDemanda.click()
        time.sleep(1)

        # =========== ETAPA 5: Validação do DOD =============

        ##ALTERAR A CADA EXECUÇÃO

        Fcampo_Demanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-demanda-validar-list/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        Fcampo_Demanda.click()
        Fcampo_Demanda.send_keys(nome_demanda)
        time.sleep(1)

        selecionar_Demanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-demanda-validar-list/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]'))
        )
        logger.info('Início Validação')
        selecionar_Demanda.click()

        validacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="inAprovado"]'))
        )
        validacao.click()

        aprovado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="inAprovado"]/option[1]'))
        )
        aprovado.click()
        time.sleep(1)
        
        parecer_Aprovado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-validar-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-aprovacao-atual/form/div/div/div[4]/div/app-quill-editor/div/div[2]/div/div[1]'))
        )
        parecer_Aprovado.click()
        parecer_Aprovado.send_keys('Automatizado')
        time.sleep(1)


        body1 = driver.find_element(By.TAG_NAME, "body")
        body1.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        Registrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-validar-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-aprovacao-atual/form/button[1]'))
        )
        Registrar.click()
        time.sleep(2)

        logger.info('Validação Concluída')

    except Exception:
        logger.exception('❌ Falha na validação do DOD')
        raise

    fechar_mensagemaprovado = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
    )
    fechar_mensagemaprovado.click()
    time.sleep(3)

    # =========== ETAPA 6: Assinatura do Fluxo do DOD - Gestor ===========


    try:
        menu_Planejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-14"]/span'))
        )
        menu_Planejamento.click()
        time.sleep(1)

        submenu_AssinarDocumento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/div/a[3]'))
        )
        submenu_AssinarDocumento.click()
        time.sleep(1)

        ##INSERIR AQUI A DESCRIÇÃO DA DEMANDA ( INFORMAÇÃO INCLUIDA NO CAMPO "NOME DEMANDA")

        Campo_Descricaoassinatura = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        Campo_Descricaoassinatura.click()
        Campo_Descricaoassinatura.send_keys(nome_demanda)
        time.sleep(1)

        Botao_AssinarDoc = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]/button[1]'))
        )
        logger.info('Início Assinatura Gestor')
        Botao_AssinarDoc.click()
        time.sleep(1)

        campo_senha = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha.click()
        campo_senha.send_keys(SENHA_PADRAO)

        Botao_assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        Botao_assinar.click()
        time.sleep(2)

        logger.info('Assinatura Gestor Concluída')

    except Exception:
        logger.info('❌ Falha na Assinatura')

    mensagemSucesso = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
    )
    mensagemSucesso.click()
    time.sleep(2)

    # Logout do Gestor e login com o usuário autoridade
    try:
        Menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]/i'))
        )
        Menu_Deslogar.click()
        time.sleep(1)

        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        logger.info('Deslogando')
        Sair.click()
        time.sleep(1)

        logger.info('Logando com usuário Autoridade Competente')
        Campo_login4usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login4usuario.click()
        Campo_login4usuario.clear()
        Campo_login4usuario.send_keys(USUARIO_AUTORIDADE)

        campo_senha4usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha4usuario.click()
        campo_senha4usuario.send_keys(SENHA_PADRAO)

        botao_entrar4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar4.click()
        time.sleep(1)

        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(3)

        logger.info('Autenticação Concluída')

    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise
            
    
    try:

        menu_Planejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-14"]/span'))
        )
        menu_Planejamento.click()
        time.sleep(1)
        
        submenu_AssinarDocumento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[5]/div/a[3]'))
        )
        submenu_AssinarDocumento.click()
        time.sleep(1)


        ## Alterar Send.Keys de acordo com a descrição da DEMANDA

        Campo_Descricaoassinatura1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        Campo_Descricaoassinatura1.click()
        Campo_Descricaoassinatura1.send_keys(nome_demanda)
        time.sleep(1)



        Botao_AssinarDoc2 = WebDriverWait(driver, 10). until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/button[1]'))
        )
        Botao_AssinarDoc2.click()
        

        assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[2]/div/div[2]/input'))
        )
        assinar.click()
        assinar.send_keys('12345')

        assinarsim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        assinarsim.click()
        time.sleep(3)
        
        logger.info('Assinatura Autoridade Concluída')

    except Exception:
        logger.exception('❌ Falha na Assinatura Autoridade')
        raise

    mensagemSucesso = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
    )
    mensagemSucesso.click()
    time.sleep(1)


    # Logout da Autoridade e login com o usuário EPC
    try:
        Menu_Deslogar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]/i'))
        )
        Menu_Deslogar.click()
        time.sleep(1)
    
        Sair = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        logger.info('Deslogando')
        Sair.click()
        time.sleep(1)
    
        logger.info('Logando com usuário EPC (Equipe de Planejamento)')
        Campo_login4usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login4usuario.click()
        Campo_login4usuario.clear()
        Campo_login4usuario.send_keys(USUARIO_EPC)
    
        campo_senha4usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha4usuario.click()
        campo_senha4usuario.send_keys(SENHA_PADRAO)
    
        botao_entrar5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar5.click()
        time.sleep(1)
    
        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(1)
    
        logger.info('Autenticação Concluída')
    
    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise