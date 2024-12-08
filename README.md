# 🕹️ **Jogo da Forca** 🦸‍♂️🦸‍♀️

Um jogo interativo de **Forca** baseado em personagens da Marvel e DC. Teste seus conhecimentos sobre os personagens icônicos de quadrinhos em um desafio divertido e envolvente!

---

## 🚀 **Visão Geral do Projeto**

O código implementa um jogo da forca simples, onde o usuário tenta adivinhar o nome de personagens da Marvel/DC com um número limitado de tentativas. A cada tentativa, o usuário deve tentar acertar letras no nome, com dicas sobre o tema para facilitar a experiência.

---

## 🛠️ **Recursos Principais**

### Funcionalidades:
- **Personagens da Marvel/DC como Palavras**: Base de palavras armazenada no arquivo `Forca.txt`.
- **Mecânica de Forca Tradicional**: Baseia-se na tentativa de acertar letras com um número limitado de tentativas.
- **Dica Incluída no Jogo**: O jogo fornece uma dica para ajudar o jogador.
- **Interface Limpa no Console**: A tela é limpa em cada etapa para uma melhor experiência visual.
- **Rejogar após cada tentativa**: Permite ao usuário continuar jogando com outras palavras.

---

## ⚙️ **Configuração**

### Pré-requisitos
- Python 3.x instalado no seu sistema.
- Arquivo de palavras `Forca.txt` contendo os nomes dos personagens da Marvel/DC para serem usados no jogo.

---

## ▶️ **Como Executar**

1. Clone este repositório no seu ambiente local:
```bash
git clone https://github.com/seu-usuario/jogo-da-forca.git
```

2. Certifique-se de que o arquivo `Forca.txt` está no mesmo diretório que o código.  
   O arquivo deve conter uma lista de palavras, uma palavra por linha, representando os nomes dos personagens.

3. Execute o código no terminal com:
```bash
python seu_arquivo.py
```

---

## 🎮 **Como Jogar**

Após iniciar o programa, você verá o seguinte fluxo:

1. **Menu inicial com palavras aleatórias**:  
   O jogo seleciona automaticamente uma palavra da base de dados `Forca.txt`.

2. **Dica apresentada no console**:
   O jogo exibe a mensagem:  
   ```
   Dica: Personagem da Marvel e DC
   ```

3. **Interface da Forca com espaço para adivinhação de letras**:
   O jogador verá algo como `_ _ _ _` para letras não descobertas e espaços preenchidos com letras corretamente adivinhadas.

4. **Tentativas são contabilizadas**:  
   Cada letra errada diminui o número de tentativas restantes.

---

## 💬 **Exemplo do Fluxo**

Ao iniciar, o jogo se parecerá com o seguinte exemplo no console:

```
* Forca *
Dica: Personagem da Marvel e DC
Erros:  
Tentativas restantes: 6

_ _ _ _ 

Digite uma letra: 
```

Caso você adivinhe corretamente:

```
Você conseguiu!
* Forca *
H U L K
Fim de Jogo!
```

Caso contrário, uma mensagem informando o erro será exibida, e o jogo continuará até que o usuário perca ou ganhe.

---

## 🧮 **Tecnologias Utilizadas**

- **Python 3.x**
- Manipulação de arquivos com `open()`.
- Utilização de funções `os.system('cls')` para manter o console limpo durante a experiência.

---

Agora é sua vez de testar seus conhecimentos sobre os personagens da Marvel/DC! Boa sorte! 🦸‍♂️🦸‍♀️✨