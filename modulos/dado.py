def leiadinheiro(text):
    while True:
        text_user = input(text).strip().lower().replace(',', '.')
        text_user_temp = text_user.replace('.', '')
        if text_user_temp.isnumeric():
            return float(text_user)
        else:
            print('\033[31mErro! Digite um valor válido: \033[m')