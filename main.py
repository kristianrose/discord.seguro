import string, random, asyncio, requests, datetime
from colorama import Fore, init
init(convert=True)

class Change:
    def __init__(self, token):
        self.token = token
        self.api = 'https://discord.com/api/v7/'
    
    def genPass(self, length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def getHeaders(self, token):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.130 Safari/537.36',
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        return headers

    def logInfo(self, nova_senha, senha_antiga):
        date = datetime.datetime.now().strftime("%H:%M %p")
        f = open("loggin.txt", "a")
        data = '==============================='
        data += '\nNova Senha: ' + nova_senha
        data += '\nSenha Antiga: ' + senha_antiga
        data += '\nMudada em: ' + date
        data += '\n==============================\n\n'
        f.write(data);f.close()

    def mudarSenha(self, senhaa_antiga, interval):
        mudar_senha = senhaa_antiga,
        userInfo = requests.get(self.api + 'users/@me', headers=self.getHeaders(self.token)).json()
        novaSenha = self.genPass(10)
        payload = {
            'password': mudar_senha,
            'nova_senha': novaSenha,
            'discriminator': userInfo['discriminator'],
            'email': userInfo['email'],
            'avatar': userInfo['avatar']
        }
        requests.patch(self.api + "users/@me", json=payload, headers=self.getHeaders(self.token)) 
        self.logInfo(novaSenha, senhaa_antiga,)
        mudar_senha = novaSenha
        asyncio.sleep(interval * 3600) 
        
if __name__ == "__main__":
    print(f"[{Fore.RED}>{Fore.RESET}] Token do usuario")
    token = str(input(">"))
    print(f"[{Fore.RED}>{Fore.RESET}] Intervalo para mudar")
    interval = int(input(" > "))
    print(f"[{Fore.RED}>{Fore.RESET}] Senha atual")
    c_pass = str(input(" > "))

    Change(token).mudarSenha(c_pass, interval)
