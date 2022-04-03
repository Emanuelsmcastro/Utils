import subprocess
import re

inf = subprocess.check_output('netsh wlan show profiles'.split(), encoding='cp858')
regex = re.compile(r'Todos os Perfis de Usuários:.*')
math = regex.findall(inf)
redes = [rede.replace('Todos os Perfis de Usuários: ', '') for rede in math]

for rede in redes:
    password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'{rede}', 'key', '=', 'clear'],
                                       encoding='cp858')
    regex_password = re.compile(r'Conteúdo da Chave.*')
    math_password = regex_password.findall(password)
    print('*' * 20 + f'\n{rede}\n{math_password[0]}\n' + '*' * 20 + '\n')
