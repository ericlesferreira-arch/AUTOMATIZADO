from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from funcoes import gerar_nome
from TermoCiencia_BANPARA import TermoCiencia
from validarEassinar_BANPARA import validarEassinar
from Etp_BANPARA import Etp
from ValidarAssinarETP_BANPARA import ValidarAssinarETP
from TermoReferencia import TermoReferencia
from utils.logger import setup_logger
import time



logger = setup_logger()

# ============================================================
#  CONFIGURAÇÕES DO CLIENTE BANPARA
#  Ajuste os usuários abaixo conforme o ambiente do cliente
# ============================================================

USUARIO_PRINCIPAL   = 'Ericles.magno'   # Gestor / criador da demanda
USUARIO_EPC         = 'Julyson.Santos'       # Integrante EPC / aceite dos termos
USUARIO_RESPONSAVEL = 'Claudio.magno'      # Responsável pela demanda / assinatura
USUARIO_AUTORIDADE  = 'Teste.qa'      # Autoridade competente                
SENHA_PADRAO        = '12345'

URL_SISTEMA = 'https://banpara-tst-plc.govadm.com.br/login'

# ============================================================


class TestDOD_BANPARA:

    def setup_class(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)


    def test_loginn(self):
        logger.info("===== INÍCIO DO TESTE TestDOD - BANPARA =====")
        driver  = self.driver
        wait    = self.wait
        actions = self.actions

        logger.info("Acessando página de Login - BANPARA")
        driver.get(URL_SISTEMA)


        ## Nessa primeira Página, alterar apenas o Send_Keys da descrição da Demanda

        # ===== ETAPA 1: LOGIN =======

        try:
            logger.info("Iniciando Autenticação")

            Campo_login = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]'))
            )
            Campo_login.click()
            Campo_login.send_keys(USUARIO_PRINCIPAL)

            campo_senha = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]'))
            )
            campo_senha.click()
            campo_senha.send_keys(SENHA_PADRAO)

            botao_entrar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div[2]/div/div/div/div/div/div[2]/div/form/button'))
            )
            botao_entrar.click()
            time.sleep(1)

            botao_sim = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
            )
            botao_sim.click()
            time.sleep(1)

            logger.info("Autenticação Realizada com Sucesso")

        except Exception:
            logger.exception("❌ Erro durante o processo de autenticação")
            raise

        time.sleep(1)

        # ===== ETAPA 2: CRIAÇÃO DA DEMANDA ======

        try:
            logger.info("Inicio da criação da Demanda")

            Menu_Demandas = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-7"]/span'))
            )
            Menu_Demandas.click()
            time.sleep(1)

            submenu_registrodemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/app-menu/div/nav/div/div[1]/div/a[1]'))
            )
            submenu_registrodemanda.click()
            time.sleep(1)

            botao_CriarDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-list/p-table/div/div[1]/div/button[1]/i'))
            )
            botao_CriarDemanda.click()
            time.sleep(1)

            opcao_tipoDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-list/p-dialog/div/div/div[2]/div/div[3]/button'))
            )
            opcao_tipoDemanda.click()

            ## COLOCANDO O NOME DA DEMANDA COMO "RANDOM" GERAÇÃO AUTOMATICA PARA NAO PRECISAR EDITAR A CADA EXECUÇÃO

            campo_NovaDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="nmDemanda"]'))
            )
            campo_NovaDemanda.click()
            self.nome_demanda = gerar_nome()
            campo_NovaDemanda.send_keys(self.nome_demanda)

            Campo_tipo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[1]/div[2]/select'))
            )
            Campo_tipo.click()
            

            opcao_campo_tipo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[1]/div[2]/select/option[2]'))
            )
            opcao_campo_tipo.click()
            time.sleep(1)


            campo_responsavelDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUsuarioResponsavel"]'))
            )
            campo_responsavelDemanda.click()

            
            opcao_responsavelDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[2]/div[2]/select/option[6]'))
            )
            opcao_responsavelDemanda.click()

            campo_AutoridadeCompetente = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[3]/div[1]/select'))
            )
            campo_AutoridadeCompetente.click()
            time.sleep(1)

            
            opcao_AutoridadeCompetente = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiretoriaVinculada"]/option[4]'))
            )
            opcao_AutoridadeCompetente.click()
            time.sleep(1)

            Campo_NumProcesso = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[3]/div[2]/select'))
            )
            Campo_NumProcesso.click()

            
            opcao_Processo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="nuProcesso"]/option'))
            )
            opcao_Processo.click()
            time.sleep(1)

            Ndemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[1]/div[1]/input'))
            )
            Ndemanda.click()
            time.sleep(1)


            ícone = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[5]/div/app-quill-editor/div/div[1]/span[5]/button[3]'))
            )
            ícone.click()
            ícone.send_keys('TESTE AUTOMATIZADO 01')
            time.sleep(1)

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)

            time.sleep(1)


            Campo_JustificativaNecessidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-demanda-form/p-tabview/div/div/p-tabpanel[1]/div/app-demanda-dados-basicos/form/div/div/div[6]/div/app-quill-editor/div/div[1]/span[5]/button[3]'))
            )
            Campo_JustificativaNecessidade.click()
            Campo_JustificativaNecessidade.send_keys('AUTOMATIZADOOOO')
            time.sleep(1)
            

            botao_EnviarDemanda = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-tabpanel-0"]/app-demanda-dados-basicos/form/button[1]'))
            )
            botao_EnviarDemanda.click()

            Botao_SIMenviar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-tabpanel-0"]/app-demanda-dados-basicos/app-confirm-dialog/p-dialog/div/div/div[3]/p-footer/button[2]'))
            )
            Botao_SIMenviar.click()
            time.sleep(3)

            logger.info("Demanda Enviada para aprovações")

        except Exception:
            logger.exception("❌ Falha ao criar demanda")
            raise

        # ==== ETAPA 3: INDICAR EQUIPE PLANEJAMENTO ======

        try:
            menu_DemandasEquipe = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="#grupo-7"]/span'))
            )
            menu_DemandasEquipe.click()

            submenu_EquipePlanejamento = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[1]/div/app-menu/div/nav/div/div[1]/div/a[3]'))
            )
            submenu_EquipePlanejamento.click()

            opcao_Equipe = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="conteudo-principal"]/app-equipe-planejamento-list/p-table/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/a'))
            )
            logger.info("Indicação Primeiro Integrante")
            opcao_Equipe.click()

            # --- Primeiro Integrante ---
            campo_UnidadeIntegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUnidade"]'))
            )
            campo_UnidadeIntegrante.click()

            # ⚠️ VERIFICAR: índice da unidade no BANPARA (atualmente option[119])
            PrimeiraUnidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[1]/select/option[62]'))
            )
            PrimeiraUnidade.click()

            campo_NomeprimeiroIntegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUsuario"]'))
            )
            campo_NomeprimeiroIntegrante.click()

            # ⚠️ VERIFICAR: índice do usuário no BANPARA (atualmente option[4])
            primeirointegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[2]/select/option[7]'))
            )
            primeirointegrante.click()

            campo_papelEquipe1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]'))
            )
            campo_papelEquipe1.click()

            papel1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]/option[1]'))
            )
            papel1.click()

            botao_salvar1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="add"]'))
            )
            botao_salvar1.click()
            time.sleep(2)

            # --- Segundo Integrante ---
            campo_UnidadeIntegrante2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUnidade"]'))
            )
            logger.info("Segundo Integrante")
            campo_UnidadeIntegrante2.click()
            time.sleep(1)

            SegundaUnidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[1]/select/option[62]'))
            )
            SegundaUnidade.click()
            time.sleep(1)

            campo_NomeSegundoIntegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUsuario"]'))
            )
            campo_NomeSegundoIntegrante.click()
            time.sleep(1)

            Segundointegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[2]/select/option[7]'))
            )
            Segundointegrante.click()
            time.sleep(1)

            campo_papelEquipe2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]'))
            )
            campo_papelEquipe2.click()
            time.sleep(1)

            papel2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]/option[2]'))
            )
            papel2.click()

            botao_salvar2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="add"]'))
            )
            botao_salvar2.click()
            time.sleep(2)

            # --- Terceiro Integrante ---
            campo_UnidadeIntegrante3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUnidade"]'))
            )
            logger.info("Terceiro Integrante")
            campo_UnidadeIntegrante3.click()
            time.sleep(1)

            TerceiraUnidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[1]/select/option[62]'))
            )
            TerceiraUnidade.click()

            campo_NomeTerceiroIntegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idUsuario"]'))
            )
            campo_NomeTerceiroIntegrante.click()

            TerceiroIntegrante = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-app-layout/div/div/div/div[2]/app-equipe-planejamento/form/div/div/div[2]/div[2]/select/option[7]'))
            )
            TerceiroIntegrante.click()

            campo_papelEquipe3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]'))
            )
            campo_papelEquipe3.click()

            papel3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="idEquipePapel"]/option[3]'))
            )
            papel3.click()

            botao_salvar3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="add"]'))
            )
            botao_salvar3.click()
            time.sleep(2)

            logger.info("Indicação concluída")

        except Exception:
            logger.exception("❌ A indicação Falhou")
            raise

        mensagemtxt1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]'))
        )
        mensagemtxt1.click()
        time.sleep(1)

        mensagemtxt2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="toast-container"]'))
        )
        mensagemtxt2.click()
        time.sleep(3)

        TermoCiencia(driver)
        validarEassinar(driver, self.nome_demanda)
        self.nome_etp = Etp(driver)
        ValidarAssinarETP(driver, self.nome_etp)
        TermoReferencia(driver)

    def teardown_class(self):
        self.driver.close()
