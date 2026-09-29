from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import time

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
# ============================================================
USUARIO_EPC      = 'Julyson.santos'       # ← PREENCHER (equivalente ao goku.silva)
USUARIO_PRINCIPAL = 'Ericles.magno'
SENHA_PADRAO     = '12345'
# ============================================================


def TermoCiencia(driver):

    logger = setup_logger()

    # Logout do usuário principal e login com o usuário EPC
    try:
        logger.info("Deslogando")

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

        # ========= Etapa 4 - Aceite no Termo de Ciência =========

        logger.info('Logando com EPC')
        Campo_login2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login2usuario.click()
        Campo_login2usuario.clear()
        Campo_login2usuario.send_keys('Julyson.santos')

        campo_senha2usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha2usuario.click()
        campo_senha2usuario.send_keys(SENHA_PADRAO)

        botao_entrar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar2.click()

        botao_sim = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
            )
        botao_sim.click()
        time.sleep(1)
        
        logger.info("Autenticação Concluída")

    except Exception:
        logger.exception("❌ Falha na Autenticação")
        raise

    time.sleep(2)

    try:
        menu_DemandasTC = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-7"]/span'))
        )
        menu_DemandasTC.click()

        submenu_TermoCiencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[1]/div/a[5]'))
        )
        submenu_TermoCiencia.click()

        # --- Aceite do Primeiro Indicado EPC ---
        logger.info('Iniciando o Aceite Termo Ciência - 1º Indicado')

        coluna_acao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/a/i'))
        )
        coluna_acao.click()
        time.sleep(1)

        modal_flag1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[1]/p-checkbox/div/div[2]'))
        )
        modal_flag1.click()
        

        modal_flag2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[2]/p-checkbox/div/div[2]'))
        )
        modal_flag2.click()

        botao_aceitarindicacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[2]/button[1]/span'))
        )
        botao_aceitarindicacao.click()

        assinar_documento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        assinar_documento.click()
        assinar_documento.send_keys(SENHA_PADRAO)

        assinar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        assinar.click()
        time.sleep(2)

        mensagemtxt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
        )
        mensagemtxt.click()
        time.sleep(1)

        # --- Aceite do Segundo Indicado EPC ---
        logger.info('Aceite Segundo Indicado EPC')

        coluna_acao1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/a/i'))
        )
        coluna_acao1.click()
        time.sleep(2)

        modal_flag3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[1]/p-checkbox/div/div[2]'))
        )
        modal_flag3.click()

        modal_flag4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[2]/p-checkbox/div/div[2]'))
        )
        modal_flag4.click()

        botao_aceitarindicacao1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[2]/button[1]/span'))
        )
        botao_aceitarindicacao1.click()

        assinar_documento1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        assinar_documento1.click()
        assinar_documento1.send_keys(SENHA_PADRAO)

        assinar1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        assinar1.click()
        time.sleep(2)

        mensagemtxt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
        )
        mensagemtxt.click()
        time.sleep(1)

        # --- Aceite do Terceiro Indicado EPC ---
        logger.info('Aceite Terceiro Indicado EPC')

        coluna_acao2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/a/i'))
        )
        coluna_acao2.click()
        time.sleep(1)

        modal_flag5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[1]/p-checkbox/div/div[2]'))
        )
        modal_flag5.click()
        time.sleep(1)

        modal_flag6 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[1]/div/div[2]/p-checkbox/div/div[2]'))
        )
        modal_flag6.click()

        botao_aceitarindicacao2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-termo-ciencia-dialog/div/div[2]/div[2]/button[1]/span'))
        )
        botao_aceitarindicacao2.click()

        assinar_documento2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        assinar_documento2.click()
        assinar_documento2.send_keys(SENHA_PADRAO)

        assinar2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-termo-ciencia/app-assinar-documento-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        assinar2.click()
        time.sleep(2)

        mensagemtxt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
        )
        mensagemtxt.click()
        time.sleep(1)

        logger.info('Aceite Termo Ciência Concluído')

    except Exception:
        logger.exception('❌ Falha ao Aceitar Termos de Ciência')
        raise

    # Logout do usuário EPC e login com o usuário principal
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
