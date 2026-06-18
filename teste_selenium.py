from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Configuração inicial do WebDriver (Neste caso, a usar o Chrome)
driver = webdriver.Chrome()

# Maximiza a janela do navegador logo após abrir
driver.maximize_window()

# 2. Define o tempo máximo (em segundos) que o Selenium vai esperar que um elemento apareça
wait = WebDriverWait(driver, 10) 

try:
    # 3. Aceder ao site que está a desenvolver
    driver.get("https://paraibahotdog.netlify.app/")

    print("Site carregado com sucesso. A iniciar os testes...")
    
    # =========================================================================
    # ÁREA DE TESTES - REPLIQUE OS BLOCOS ABAIXO CONFORME A SUA NECESSIDADE
    # =========================================================================
    time.sleep(2)
    
    # ---> AÇÃO: CLICAR NUM BOTÃO OU LINK <---
    xpath_unidades = "/html/body/div/header/div/nav[1]/ul/li[2]/a"
    botao_unidades = wait.until(EC.presence_of_element_located((By.XPATH, xpath_unidades)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_unidades)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_unidades)

    xpath_aguasclaras = "/html/body/div/main/section[3]/div/a[1]"
    botao_aguasclaras = wait.until(EC.presence_of_element_located((By.XPATH, xpath_aguasclaras)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_aguasclaras)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_aguasclaras)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    

    xpath_home = "/html/body/div/header/div/a[1]/img"
    botao_home = wait.until(EC.presence_of_element_located((By.XPATH, xpath_home)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_home)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_home)
    time.sleep(2)


    xpath_aguasclaras2 = "/html/body/div/main/section[3]/div/a[2]"
    botao_aguasclaras2 = wait.until(EC.presence_of_element_located((By.XPATH, xpath_aguasclaras2)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_aguasclaras2)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_aguasclaras2)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    

    xpath_home = "/html/body/div/header/div/a[1]/img"
    botao_home = wait.until(EC.presence_of_element_located((By.XPATH, xpath_home)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_home)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_home)
    time.sleep(2)


    xpath_cardapiohome = "/html/body/div/main/section[2]/a/span"
    botao = wait.until(EC.presence_of_element_located((By.XPATH, xpath_cardapiohome)))
    # Passo A: Faz scroll na página até o botão ficar bem no centro do ecrã
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
    time.sleep(2)
    
    # Passo B: Força o clique diretamente no código da página (ignora o que estiver à frente)
    driver.execute_script("arguments[0].click();", botao)
    
    print("Clique realizado com sucesso.")
    time.sleep(2) # Pausa de 2 segundos para dar tempo de a animação de scroll terminar

    driver.switch_to.window(driver.window_handles[-1])
    print("Foco alterado para o novo separador do cardápio.")
    
    # 3. Espera mais um pouco para garantir que a página do cardápio carregou completamente
    time.sleep(5)


    xpath_produtocardapio = "/html/body/div/main/section/div[2]/section[1]/div/button[1]/div[1]"
    botao_produtocardapio = wait.until(EC.presence_of_element_located((By.XPATH, xpath_produtocardapio)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_produtocardapio)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_produtocardapio)
    time.sleep(2)
    xpath_fechaproduto = "/html/body/div/div/div/div/div[2]/div[1]/button"
    botao_fechaproduto = wait.until(EC.presence_of_element_located((By.XPATH, xpath_fechaproduto)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_fechaproduto)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_fechaproduto)
    time.sleep(2)
    
    for i in range(100):
        # 1. Guarda a posição da barra de rolagem ANTES de descer
        posicao_antiga = driver.execute_script("return window.pageYOffset;")
        
        # 2. Tenta descer os 100 pixels
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(0.1)
        
        # 3. Guarda a posição da barra DEPOIS de descer
        posicao_nova = driver.execute_script("return window.pageYOffset;")
        
        # 4. A magia: Se a posição for a mesma, significa que bateu no fundo!
        if posicao_antiga == posicao_nova:
            print("Chegou ao fim da página! Interrompendo o scroll para poupar tempo.")
            break # O 'break' cancela o resto das repetições imediatamente

    print("Pronto para a próxima ação.")

    xpath_home = "/html/body/div/header/div/a[1]/img"
    botao_home = wait.until(EC.presence_of_element_located((By.XPATH, xpath_home)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_home)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_home)
    time.sleep(2)

    
    for i in range(1, 6):
        # A letra 'f' antes das aspas permite injetar a variável {i} direto no XPath
        xpath_duvida = f"/html/body/div/main/section[4]/div/div[{i}]/button"
        
        # Procura o botão da dúvida atual (1, depois 2, depois 3...)
        botao_duvida = wait.until(EC.presence_of_element_located((By.XPATH, xpath_duvida)))
        
        # Faz o scroll até à dúvida
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_duvida)
        time.sleep(1) # Pausa mais curta apenas para o ecrã estabilizar
        
        # Clica na dúvida para abrir a resposta
        driver.execute_script("arguments[0].click();", botao_duvida)
        print(f"Dúvida {i} clicada com sucesso.")
        
        # Espera 2 segundos para dar tempo de ver a resposta aberta antes de ir para a próxima
        time.sleep(2)

    xpath_blog = "/html/body/div/header/div/nav[1]/ul/li[3]/a"
    botao_blog = wait.until(EC.presence_of_element_located((By.XPATH, xpath_blog)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_blog)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_blog)
    time.sleep(2)

    xpath_noticias = "/html/body/div/main/section[2]/div[2]/ul/li[2]/button"
    xpath_promocoes = "/html/body/div/main/section[2]/div[2]/ul/li[3]/button"
    
    # Variáveis de controle (Flags) para o robô lembrar no que já clicou
    ja_clicou_no_noticias = False
    ja_clicou_no_promocoes = False

    print("Iniciando a descida da página e busca pelos elementos...")

    # O loop agora só vai parar quando bater no fundo da tela
    while True:
        
        # 1. Tenta achar e clicar no PRIMEIRO elemento (se ainda não tiver clicado)
        if not ja_clicou_no_noticias:
            elementos_1 = driver.find_elements(By.XPATH, xpath_noticias)
            if len(elementos_1) > 0:
                botao_1 = elementos_1[0]
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_1)
                time.sleep(1) # Pausa para ver centralizado
                
                driver.execute_script("arguments[0].click();", botao_1)
                print("Primeiro elemento clicado com sucesso!")
                
                ja_clicou_no_noticias = True # Marca como concluído para não clicar de novo
                time.sleep(1) # Pausa rápida após o clique

        # 2. Tenta achar e clicar no SEGUNDO elemento 
        # (O 'elif' garante que ele só vai procurar o segundo DEPOIS que o primeiro já foi clicado)
        elif ja_clicou_no_noticias and not ja_clicou_no_promocoes:
            elementos_2 = driver.find_elements(By.XPATH, xpath_promocoes)
            if len(elementos_2) > 0:
                botao_2 = elementos_2[0]
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_2)
                time.sleep(1)
                
                driver.execute_script("arguments[0].click();", botao_2)
                print("Segundo elemento clicado com sucesso!")
                
                ja_clicou_no_promocoes = True # Marca como concluído
                time.sleep(1)

        # 3. Ação contínua: Continua a rolar a tela para baixo
        posicao_antiga = driver.execute_script("return window.pageYOffset;")
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(0.2) # Velocidade do scroll
        posicao_nova = driver.execute_script("return window.pageYOffset;")
        
        # 4. Regra de parada: Verifica se chegou ao fundo absoluto da página
        if posicao_antiga == posicao_nova:
            print("Chegou ao fim da página! O scroll terminou.")
            break # Agora o laço só é quebrado aqui!
    
    for i in range(1, 3):
        # A letra 'f' antes das aspas permite injetar a variável {i} direto no XPath
        xpath_avaliacao = f"/html/body/div/main/section[3]/div[2]/div[2]/button[2]"
        
        # Procura o botão da avaliação atual (1, depois 2, depois 3...)
        botao_avaliacao = wait.until(EC.presence_of_element_located((By.XPATH, xpath_avaliacao)))
        
        # Faz o scroll até à avaliação
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_avaliacao)
        time.sleep(1) # Pausa mais curta apenas para o ecrã estabilizar
        
        # Clica na avaliação para abrir a resposta
        driver.execute_script("arguments[0].click();", botao_avaliacao)
        print(f"Avaliação {i} clicada com sucesso.")
        
        # Espera 2 segundos para dar tempo de ver a resposta aberta antes de ir para a próxima
        time.sleep(2)

    xpath_fidelidade = "/html/body/div/header/div/nav[1]/ul/li[4]/a"
    botao_fidelidade = wait.until(EC.presence_of_element_located((By.XPATH, xpath_fidelidade)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_fidelidade)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_fidelidade)
    time.sleep(2)

    xpath_cadastrofidelidade = "/html/body/div/main/section/div/form/input"
    # Mudamos o nome da variável para 'campo_email' para fazer mais sentido
    campo_email = wait.until(EC.presence_of_element_located((By.XPATH, xpath_cadastrofidelidade)))
    # 1. Faz o scroll até o campo ficar no centro da tela
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campo_email)
    time.sleep(1) # Pausa rápida para a tela estabilizar
    # 2. (Opcional, mas recomendado) Clica no campo para dar "foco" nele
    driver.execute_script("arguments[0].click();", campo_email)
    time.sleep(1)
    # 3. Limpa qualquer texto que já esteja no campo (por segurança)
    campo_email.clear()
    # 4. A MÁGICA: Digita o texto dentro do input!
    campo_email.send_keys("teste@meuemail.com")
    print("E-mail preenchido com sucesso.")
    time.sleep(2)

    xpath_consultafidelidade = "/html/body/div/main/section/div/form/button"
    botao_consultafidelidade = wait.until(EC.presence_of_element_located((By.XPATH, xpath_consultafidelidade)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_consultafidelidade)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", botao_consultafidelidade)
    time.sleep(2)

except Exception as e:
    # Caso o XPath esteja errado ou o elemento não carregue, ele avisa aqui
    print(f"Ocorreu um erro durante a execução: {e}")

finally:
    # 4. Finalizar e fechar o navegador
    print("Teste finalizado.")
    # Comentado temporariamente para o ecrã não fechar automaticamente
    driver.quit()