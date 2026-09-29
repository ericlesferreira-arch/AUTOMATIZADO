from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import time

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
# ============================================================
USUARIO_PRINCIPAL = 'ericles.magno'
USUARIO_EPC       = 'julyson.santos'   
SENHA_PADRAO      = '12345'
# ============================================================


def ValidarAssinarETP(driver, nome_etp):

    logger = setup_logger()

    
    # Acessando menu ETP > Validar ETP
    menu_EstudoTecnicoV = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-10"]'))
    )
    menu_EstudoTecnicoV.click()
    time.sleep(1)

    Submenu_ValidarETP = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[2]/div/a[2]'))
    )
    Submenu_ValidarETP.click()

    # ===== ETAPA DE VALIDAÇÃO DO ETP =======
    try:
        # ⚠️ ALTERAR o send_keys conforme o nome dO ETP a ser buscada
        Filtro_BuscarPorETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-validacao-list/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        Filtro_BuscarPorETP.click()
        logger.info('Iniciando Validação ETP')
        Filtro_BuscarPorETP.send_keys(nome_etp)
        time.sleep(1)

        Acao_Validaretp = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-validacao-list/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]/a'))
        )
        Acao_Validaretp.click()

        Campo_ValidacaoETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-aprovacao-atual/form/div/div/div[3]/div[3]/select'))
        )
        Campo_ValidacaoETP.click()

        Opcao_validacaoAprovado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-aprovacao-atual/form/div/div/div[3]/div[3]/select/option[1]'))
        )
        Opcao_validacaoAprovado.click()

        Botao_Registrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-validacao-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-aprovacao-atual/form/button[1]'))
        )
        Botao_Registrar.click()
        time.sleep(7)

        mensagemSucesso = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
        )
        mensagemSucesso.click()
        time.sleep(2)

        logger.info('Validação ETP Concluída')

    except Exception:
        logger.exception('❌ Falha ao Validar ETP')
        raise

    # Logout do Gestor e login com o usuário EPC para assinar o ETP
    try:
        Menu_Deslogar5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar5.click()
        time.sleep(1)

        Sair5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        logger.info('Deslogando')
        Sair5.click()
        time.sleep(1)

        logger.info('Logando com usuário EPC')
        Campo_login3usuario5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login3usuario5.click()
        Campo_login3usuario5.clear()
        Campo_login3usuario5.send_keys(USUARIO_EPC)
        time.sleep(1)

        campo_senha3usuario5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha3usuario5.click()
        campo_senha3usuario5.send_keys(SENHA_PADRAO)
        time.sleep(1)

        botao_entrar5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar5.click()
        time.sleep(1)

        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(2)

        logger.info('Autenticação Concluída')

    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise

            ## FAZENDO DAQUI PARA BAIXO


    # ===== ETAPA: Assinatura EPC no FLUXO do ETP =====
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

    try:
            #------- AQUI VAI A DESCRIÇÃO DO DOD (ACHAR O DOC E ASSINAR) --------#

        descricao_ETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        descricao_ETP.click()
        descricao_ETP.send_keys(nome_etp)
        time.sleep(2)

        acao_assinarEPCETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/button[1]'))
        )
        acao_assinarEPCETP.click()

        Campo_AssinarETPEPC = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[2]/div/div[2]/input'))
        )
        Campo_AssinarETPEPC.click()
        Campo_AssinarETPEPC.send_keys(SENHA_PADRAO)
        time.sleep(1)

        botao_assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_assinar.click()
        time.sleep(1)

        logger.info('Assinatura EPC no ETP Concluída')

    except Exception:
        logger.exception('❌ Falha ao Assinar com EPC')
        raise

    mensagemSucesso = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
    )
    mensagemSucesso.click()
    time.sleep(2)



# Logout do usuário EPC e login com o usuário Gestor
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

    # ------ SEMPRE ALTERAR SEND KEYS DA DESCRIÇÃO DA BUSCA PELO ETP PENDENTE DE ASSINATURA ------ # 

    try:
        logger.info('Iniciando Assinatura Gestor')

        descricao_ETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[1]/div/table/thead/tr[2]/th[2]/input'))
        )
        descricao_ETP.click()
        descricao_ETP.send_keys(nome_etp)
        time.sleep(2)

        acao_assinarGestor = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]/button[1]'))
        )
        acao_assinarGestor.click()


        campo_assinardocumentoGestor = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[2]/div/div[2]/input'))
        )
        campo_assinardocumentoGestor.click()
        campo_assinardocumentoGestor.send_keys('12345')


        btn_salvarAssinaturaGestor = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-planejamento-assinatura-documentos/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        btn_salvarAssinaturaGestor.click()
        time.sleep(2)

        mensagemSucesso = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
        )
        mensagemSucesso.click()
        time.sleep(2)

        logger.info('Assinatura Concluída')

    except Exception:
        logger.exception('❌ Falha na assinatura Gestor')
        raise


    
    