import random
import string


def gerar_nome():
        caracteres = string.ascii_lowercase + string.digits
        return ''.join(random.choices(caracteres, k=10))




def gerar_nome_etp():
    numero = random.randint(1000, 9999)
    return f"ETP_Automatizado_{numero}"




def gerar_nome_tr():
    numero = random.randint(1000, 9999)
    return f"TR_Automatizado_{numero}"