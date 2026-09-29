from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import setup_logger
import time


def AbasETP(driver):

    logger = setup_logger()

    # ========= Aba: Estimativa do Valor da Contratação =========
    try:
        Aba_EstimativaValorContratacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[6]/a'))
        )
        Aba_EstimativaValorContratacao.click()

        MeioUsado_pesquisa = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-meio-pesquisa/form/div[2]/div/div/div/div/div[1]/input'))
        )
        logger.info('Iniciando Meio de Pesquisa')
        MeioUsado_pesquisa.click()

        btn_Salvar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-meio-pesquisa/form/div[3]/button'))
        )
        btn_Salvar.click()
        time.sleep(1)

        logger.info('Meio de Pesquisa Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Meios de Pesquisa')
        raise

    # ========= Subaba: Estimativa de Preço =========
    try:
        subaba_EstimativaPreco = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/ul/li[2]/a'))
        )
        subaba_EstimativaPreco.click()

        excluir_estimativaPreco = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/p-table/div/div[1]/div/div[2]/table/tbody/tr/td[1]/button[2]/i'))
        )
        excluir_estimativaPreco.click()

        confirmar_exclusaoSIM = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/p-table/div/div[1]/div/div[2]/table/tbody/div/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        confirmar_exclusaoSIM.click()

        campodescricao_Estimativa = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/div/div/div[2]/div[1]/textarea'))
        )
        logger.info('Iniciando Estimativa de Preço')
        campodescricao_Estimativa.click()
        campodescricao_Estimativa.send_keys('AUTOMATIZADO')
        time.sleep(1)

        Campo_Quantidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/div/div/div[3]/div[1]/input'))
        )
        Campo_Quantidade.click()
        Campo_Quantidade.send_keys('10')

        Campo_ValorUnitario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/div/div/div[3]/div[2]/input'))
        )
        Campo_ValorUnitario.click()
        Campo_ValorUnitario.send_keys('250,00')

        campodescricaoR_Estimativa = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/div/div/div[2]/div[1]/textarea'))
        )
        campodescricaoR_Estimativa.click()
        time.sleep(1)

        btnSalvar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[6]/div/app-estudo-tecnico-estimativa-valor-contratacao/p-tabview/div/div/p-tabpanel[2]/div/app-estudo-tecnico-quantidades/form/div/div/div[3]/div[4]/button/i'))
        )
        btnSalvar.click()
        time.sleep(1)

        logger.info('Estimativa de Preço Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Estimativa de Preço')
        raise

    # ======== Aba: Justificativa Para o Parcelamento da Solução ========
    try:
        aba_JustificativaParcelamentoSolucao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[7]/a'))
        )
        logger.info('Iniciando Justificativa Parcelamento Solução')
        aba_JustificativaParcelamentoSolucao.click()
        time.sleep(1)

        tooltip_dividaEmItens = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[7]/div/app-estudo-tecnico-parcelamentos/form/div[2]/div/div/div[1]/input'))
        )
        tooltip_dividaEmItens.click()

        botao_Salvaritens = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[7]/div/app-estudo-tecnico-parcelamentos/form/div[3]/button'))
        )
        botao_Salvaritens.click()

        logger.info('Justificativa Parcelamento Solução concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Justificativa Parcelamento Solução')
        raise

    # ========= Aba: Contratações Correlatas ou Independentes =========
    try:
        aba_ContratacaoCorrelatasIndependentes = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[8]/a/span'))
        )
        logger.info('Iniciando Contratação Correlatas Independentes')
        aba_ContratacaoCorrelatasIndependentes.click()

        Toltip_CorrelatasIndependentes = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[8]/div/app-estudo-tecnico-licitacoes/form/div[2]/div/div/div/div[2]/input'))
        )
        Toltip_CorrelatasIndependentes.click()

        botaoSalvar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[8]/div/app-estudo-tecnico-licitacoes/form/div[3]/button'))
        )
        botaoSalvar.click()
        time.sleep(1)

        logger.info('Contratações Correlatas Independentes Concluída')

    except Exception:
        logger.exception('❌ Falha ao Concluir Contratações Correlatas Independentes')
        raise

    # ======= Aba: Alinhamento da Contratação Com o Planejamento ========
    try:
        aba_AlinhamentoContratacaoPlanejamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[9]'))
        )
        logger.info('Iniciando Alinhamento Contratação Planejamento')
        aba_AlinhamentoContratacaoPlanejamento.click()

        tooltipNao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[9]/div/app-estudo-tecnico-alinhamento-contratacao/form/div[2]/div/div[1]/div/div[2]/input'))
        )
        tooltipNao.click()

        Descricao_Providencias = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[9]/div/app-estudo-tecnico-alinhamento-contratacao/form/div[2]/div/div[2]/div/div/app-quill-editor/div/div[2]/div/div[1]'))
        )
        Descricao_Providencias.click()
        Descricao_Providencias.send_keys('AUTOMATIZADO')

        BOTAOSALVARAlinhamento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[9]/div/app-estudo-tecnico-alinhamento-contratacao/form/div[3]/button'))
        )
        BOTAOSALVARAlinhamento.click()
        time.sleep(1)

        logger.info('Alinhamento Contratação Planejamento Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Alinhamento Contratação Planejamento')
        raise

    # ======= Aba: Resultados Pretendidos =======
    try:
        aba_ResultadoPretendido = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[10]'))
        )
        logger.info('Iniciando Resultado Pretendido')
        aba_ResultadoPretendido.click()

        opcao_ReducaoCusto = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[10]/div/app-estudo-tecnico-beneficios/form/div[2]/div/div/div/div/div[1]/div[1]/input'))
        )
        opcao_ReducaoCusto.click()

        botaosalvar_ResultadoPretendido = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[10]/div/app-estudo-tecnico-beneficios/form/div[3]/button'))
        )
        botaosalvar_ResultadoPretendido.click()
        time.sleep(3)

        logger.info('Resultado Pretendido Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Resultado Pretendido')
        raise

    # ========== Aba: Providências Pendentes ========
    try:
        aba_ProvidenciasPendentes = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[11]/a/span'))
        )
        aba_ProvidenciasPendentes.click()
        logger.info('Iniciando Providências Pendentes')

        opcaoNAO = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[11]/div/app-estudo-tecnico-adequacoes/form/div[2]/div/div/div/div[2]/input'))
        )
        opcaoNAO.click()

        btnn_SalvarProvidencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[11]/div/app-estudo-tecnico-adequacoes/form/div[3]/button'))
        )
        btnn_SalvarProvidencia.click()
        time.sleep(3)

        logger.info('Providências Pendentes Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Providências Pendentes')
        raise

    # ============ Aba: Impactos Ambientais e Medidas de Mitigação ===========
    try:
        aba_ImpactosAmbientaisMitigacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[12]/a/span'))
        )
        logger.info('Iniciando Impactos Ambientais e Medidas de Mitigação')
        aba_ImpactosAmbientaisMitigacao.click()

        Toltipp_ImpactoAmbientalContratacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[12]/div/app-estudo-tecnico-impacto-ambientais/form/div[2]/div/div/div/div[2]/input'))
        )
        Toltipp_ImpactoAmbientalContratacao.click()

        btn_SalvarImpactos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[12]/div/app-estudo-tecnico-impacto-ambientais/form/div[3]/button'))
        )
        btn_SalvarImpactos.click()
        time.sleep(3)

        logger.info('Impactos Ambientais e Medidas de Mitigação Concluído')

    except Exception:
        logger.exception('❌ Falha ao Concluir Impactos Ambientais e Medidas de Mitigação')
        raise

    # ========= Aba: Conclusão =========
    try:
        aba_Conclusao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[13]/a/span'))
        )
        logger.info('Iniciando Conclusão')
        aba_Conclusao.click()

        opcao_NAO = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[13]/div/app-estudo-tecnico-conclusao/form/div[2]/div/div/div/div[2]/input'))
        )
        opcao_NAO.click()

        btn_SalvarConclusao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[13]/div/app-estudo-tecnico-conclusao/form/div[3]/button'))
        )
        btn_SalvarConclusao.click()
        time.sleep(1)

        logger.info('Conclusão Concluída')

    except Exception:
        logger.exception('❌ Falha ao Concluir Conclusão')
        raise

    # ========= Voltando para Aba Descrição da Necessidade para Enviar o ETP =========
    try:
        aba_DescricaoNecessidade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/ul/li[1]/a'))
        )
        aba_DescricaoNecessidade.click()
        logger.info('Iniciando envio do ETP para aprovações')

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        botao_enviarETP = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos/form/button[1]/i'))
        )
        botao_enviarETP.click()

        confirmar_envio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-estudo-tecnico-registro-form/p-tabview/div/div/p-tabpanel[1]/div/app-estudo-tecnico-dados-basicos/app-confirm-dialog[1]/p-dialog/div/div/div[3]/p-footer/button[2]'))
        )
        confirmar_envio.click()
        time.sleep(10)

        logger.info('ETP Enviado para Aprovações')

    except Exception:
        logger.exception('❌ Falha ao Enviar ETP para aprovações')
        raise
