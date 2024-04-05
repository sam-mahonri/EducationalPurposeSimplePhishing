# Aplicação Flask Simples de Phishing para Fins Educacionais

Esta é uma aplicação Flask de phishing desenvolvida com propósitos educacionais para demonstrar como os ataques de phishing podem ser executados e como se proteger contra eles. **Este projeto é estritamente para uso educacional e não deve ser usado para atividades ilegais.**

## Funcionalidades

- **Página de Login Falsa:** A aplicação apresenta uma página de login falsa(Kahoo[o]t e Goo[o]gle), projetada para se parecer com um serviço legítimo, como um site de rede social ou um serviço de e-mail.
- **Coleta de Credenciais:** Quando os usuários inserem suas credenciais na página de login falsa, a aplicação as armazena em um arquivo de registro para fins educacionais. Neste exemplo, as credenciais são apenas mostradas no log, sem banco de dados.
- **Alerta de Phishing:** Uma mensagem de alerta é exibida aos usuários após tentarem fazer login na página falsa, informando que estão em um ambiente de phishing e incentivando-os a ter cuidado.

## Rodando a Aplicação em Ambiente de Desenvolvimento

Siga estas etapas para executar a aplicação Flask de phishing em um ambiente de desenvolvimento:

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/sam-mahonri/EducationalPurposeSimplePhishing.git
   
   cd EducationalPurposeSimplePhishing
   ```

2. **Crie e ative o ambiente virtual e instale as dependências:**
   ```bash
   python -m venv .venv

   .venv/Scripts/Activate.ps1

   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**
   Como este exemplo é apenas para fins educacionais, a chave secreta e demais credenciais não precisam estar em um .env

4. **Execute a Aplicação:**
   ```bash
   flask run
   ```

5. **Acesse a Página de Login Falsa:**
   Abra um navegador da web e acesse `http://localhost:5000` para acessar a página de login falsa.

6. **Teste o Funcionamento:**
   Insira credenciais de teste na página de login falsa e verifique se elas são registradas corretamente no arquivo de registro.

7. **Encerre a Aplicação:**
   Quando terminar, pressione `Ctrl + C` no terminal para encerrar o servidor Flask.

## Avisos Legais

Este projeto é fornecido apenas para fins educacionais e éticos. O uso deste software para atividades ilegais é estritamente proibido. Os desenvolvedores e mantenedores deste projeto não assumem qualquer responsabilidade pelo uso indevido desta aplicação.

---

**Aviso:** Nunca use técnicas de phishing para enganar ou prejudicar os outros. Este projeto é destinado exclusivamente para fins educacionais e de conscientização sobre segurança cibernética.
