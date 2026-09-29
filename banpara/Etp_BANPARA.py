from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import setup_logger
from selenium.webdriver.common.action_chains import ActionChains
from funcoes import gerar_nome_etp
import time

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
# ============================================================
USUARIO_PRINCIPAL = 'ericles.magno'
USUARIO_EPC       = 'julyson.santos'   
SENHA_PADRAO      = '12345'
# ============================================================


def Etp(driver):

    logger = setup_logger()

    # ========= ETAPA 7: CRIAÇÃO DO ESTUDO TÉCNICO =========
    logger.info('Iniciando Criação do ETP')

    menu_EstudoTécnico = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-10"]'))
    )
    menu_EstudoTécnico.click()
    time.sleep(1)

    submenu_RegistroETP = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[2]/div/a[1]'))
    )
    submenu_RegistroETP.click()
    time.sleep(1)

    try:
        novo_ETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-list/p-table/div/div[1]/div/a/i'))
        )
        novo_ETP.click()
        logger.info('Iniciando a Elaboração do ETP')
        time.sleep(1)


        Tipoetp_Simplificado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-tipo-estudo-tecnico-dialog/div/div[1]/label[2]/input'))
        )
        Tipoetp_Simplificado.click()
        time.sleep(1)


        Botao_Iniciar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-tipo-estudo-tecnico-dialog/div/div[2]/button[2]'))
        )
        Botao_Iniciar.click()

        # Preenchimento da Aba Descrição da Necessidade
        campo_Demanda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="demanda"]'))
        )
        campo_Demanda.click()
        time.sleep(1)

        # ⚠️ Alterar de acordo com o Indice da Demanda ( A posição na qual ela está, nesta execução está na 38)
        opção_demandaETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos-simplificado/form/div/div/div[1]/div[1]/select/option[38]'))
        )
        opção_demandaETP.click()
        time.sleep(1)

        ## ALTERAR A CADA EXECUÇÃO, POIS, NA ASSINATURA DO FLUXO DO ETP, A DESCRIÇÃO QUE APARECE É A DO ETP E NAO A DA DEMANDA
    
        campo_NomeProjetoContratacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nmSolucao"]'))
        )
        campo_NomeProjetoContratacao.click()
        nome_etp = gerar_nome_etp()
        campo_NomeProjetoContratacao.send_keys(nome_etp)
        time.sleep(1)


        Campo_DescricaoETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos-simplificado/form/div/div/div[5]/div/app-quill-editor/div/div[1]/span[5]/button[3]'))
        )
        Campo_DescricaoETP.click()
        Campo_DescricaoETP.send_keys('AUTOMATIZADO')
        time.sleep(2)


        campo_NomeProjetoContratacaoR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nmSolucao"]'))
        )
        campo_NomeProjetoContratacaoR.click()
        time.sleep(1)


        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        time.sleep(1)


        
        Botao_SalvarETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos-simplificado/form/button[2]/i'))
        )
        Botao_SalvarETP.click()
        time.sleep(3)

        logger.info('Dados Básicos Salvo com sucesso')

    except Exception:
        logger.exception('❌ Falha ao salvar dados básicos')
        raise

    

    # Aba: Justificativa/Alinhamento
    try:
        logger.info('Iniciando Preenchimento da Aba Justificativa/Alinhamento')

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_UP)

        Campo_JustificativaNecessidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-justificativa-alinhamento-simplificado/form/div/div/div/div[1]/app-quill-editor/div/div[2]/div/div[1]'))
        )
        Campo_JustificativaNecessidade.click()
        Campo_JustificativaNecessidade.send_keys('AUTOMATIZADO')
        time.sleep(1)

        Campo_AlinhamentoPlanejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-justificativa-alinhamento-simplificado/form/div/div/div/div[2]/app-quill-editor/div/div[2]/div/div[1]'))
        )
        Campo_AlinhamentoPlanejamento.click()
        Campo_AlinhamentoPlanejamento.send_keys('TESTE AUTOMATIZADO')


        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        salvar_JustificativaAlinhamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-justificativa-alinhamento-simplificado/form/button/i'))
        )
        salvar_JustificativaAlinhamento.click()
        time.sleep(1)

        logger.info('Justificativa/Alinhamento Registrados com sucesso')

    except Exception:
        logger.exception('❌ Falha ao Salvar informações da aba Justificativa/Alinhamento')
        raise

    #========= Aba: Descrição da Solução ========#

    #========= Sub Aba Bens e Serviços ========#
    try:
        logger.info('Iniciando Bens e Serviços')

        descricao_BemServico = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[2]/div/div/div[1]/textarea'))
        )
        descricao_BemServico.click()
        descricao_BemServico.send_keys('Teste Automatizado')
        time.sleep(2)

        Campo_QuantidadeBem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[1]/input'))
        )
        Campo_QuantidadeBem.click()
        Campo_QuantidadeBem.send_keys('150,50')
        time.sleep(1)


        Campo_UnidadeBem = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[2]/select'))
        )
        Campo_UnidadeBem.click()


        opcao_UnidadeBem = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[2]/select/option[3]'))
        ) 
        opcao_UnidadeBem.click()
        time.sleep(1)



        Campo_ValorUnitario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[3]/input'))
        )
        Campo_ValorUnitario.click()
        Campo_ValorUnitario.send_keys('1000')
        

        Campo_ValorTotal = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[4]/div[1]/input'))
        )
        Campo_ValorTotal.click()
        time.sleep(1)



        botao_salvarBem = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-quantidades-simplificado/form/div/div/div[3]/div[4]/div[2]/button/i'))
        )
        botao_salvarBem.click()
        time.sleep(1)

        logger.info('Padrão Mínimo de Qualidade concluído')

    except Exception:
        logger.exception('❌ Falha ao Salvar Padrão Mínimo de Qualidade')

    #========  Sub aba: Estimativas das Quantidades =========#
    try:
        logger.info('Iniciando Estimativa das Quantidades')

        aba_EstimativaQuantidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/ul/li[2]'))
        )
        aba_EstimativaQuantidade.click()
        time.sleep(1)

        Descricao_EstimativaQuantidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-estimativas-quantidades-simplificado/form/div/div/div/div[1]/app-quill-editor/div/div[2]/div/div[1]'))
        )
        Descricao_EstimativaQuantidade.click()
        Descricao_EstimativaQuantidade.send_keys('TESTE AUTOMATIZADO')
        time.sleep(1)

        Descricao_CotacaoPrecos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-estimativas-quantidades-simplificado/form/div/div/div/div[2]/app-quill-editor/div/div[2]/div/div[1]'))
        )
        Descricao_CotacaoPrecos.click()
        Descricao_CotacaoPrecos.send_keys('AUTOMATIZADO')
        time.sleep(1)

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        time.sleep(1)

        salvar_EstimativaQuantidades = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-estimativas-quantidades-simplificado/form/button/i'))
        )
        salvar_EstimativaQuantidades.click()
        time.sleep(1)

        logger.info('Estimativa das Quantidades Concluída')

    except Exception:
        logger.exception('❌ Falha ao Concluir Estimativa das Quantidades')
        raise

    # Sub Aba: Parcelamentos
    try:
        logger.info('Iniciando Preenchimento sub aba Parcelamentos')

        Subaba_Parcelamentos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/ul/li[4]'))
        )
        Subaba_Parcelamentos.click()

        dESCRICAO_ParcelamentoSolucao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[4]/div/app-estudo-tecnico-parcelamentos-simplificado/form/div/div/div/div/app-quill-editor/div/div[2]/div/div[1]'))
        )
        dESCRICAO_ParcelamentoSolucao.click()
        dESCRICAO_ParcelamentoSolucao.send_keys('AUTOMATIZADO')
        time.sleep(1)


        botaosalvar_DescricaoSolucao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[3]/div/app-estudo-tecnico-bens-servico-simplificado/p-tabview/div/div/p-tabpanel[4]/div/app-estudo-tecnico-parcelamentos-simplificado/form/button'))
        )
        botaosalvar_DescricaoSolucao.click()
        time.sleep(3)

        logger.info('Parcelamentos concluído')

    except Exception:
        logger.exception('❌ Falha ao concluir Parcelamentos')
        raise

    # Aba: Declaração Viabilidade
    try:
        logger.info('Iniciando Declaração Viabilidade')

        aba_DeclaracaoViabilidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/ul/li[5]/a'))
        )
        aba_DeclaracaoViabilidade.click()

        salvar_declaracaoviabilidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[5]/div/app-estudo-tecnico-declaracao-viabilidade-simplificado/form/button/i'))
        )
        salvar_declaracaoviabilidade.click()
        time.sleep(3)

        logger.info('Declaração Viabilidade Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Declaração Viabilidade')
        raise

    # RETORNANDO PARA A ABA "DADOS BÁSICOS" PARA ENVIAR O ETP PARA APROVAÇÕES
    try:
        aba_dadosbasicos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/ul/li[1]/a'))
        )
        aba_dadosbasicos.click()

        botao_EnviarETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos-simplificado/form/button[1]/i'))
        )
        botao_EnviarETP.click()
        time.sleep(1)

        opcao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-simplificado-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos-simplificado/app-confirm-dialog[1]/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        opcao_sim.click()
        time.sleep(5)



        logger.info('Especificação Concluída')

    except Exception:
        logger.exception('❌ Falha ao Concluir Especificação')
        raise


    mensagemSucesso = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]'))
    )
    mensagemSucesso.click()
    time.sleep(1)
    

    
    mensagemSucesso2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]'))
    )
    mensagemSucesso2.click()
    time.sleep(2)
    



    # Login com o Gestor (usuário principal) para aprovar o ETP
    try:
        logger.info('Deslogando')
    
        Menu_Deslogar3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="userDropdown"]'))
        )
        Menu_Deslogar3.click()
        time.sleep(1)
    
        Sair3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/app-navbar/nav/div/div[2]/div/button[2]'))
        )
        Sair3.click()
        time.sleep(1)
    
        logger.info('Logando com usuário Principal (Gestor)')
        Campo_login3usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
        )
        Campo_login3usuario.click()
        Campo_login3usuario.clear()
        Campo_login3usuario.send_keys(USUARIO_PRINCIPAL)
    
        campo_senha3usuario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
        )
        campo_senha3usuario.click()
        campo_senha3usuario.send_keys(SENHA_PADRAO)
    
        botao_entrar3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
        )
        botao_entrar3.click()
        time.sleep(2)

        botao_sim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        botao_sim.click()
        time.sleep(2)
    
        logger.info('Autenticação Concluída')

    except Exception:
        logger.exception('❌ Falha na Autenticação')
        raise

    return nome_etp
    