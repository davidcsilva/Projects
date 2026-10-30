'''
Exercício 9.24 O que acontece com a agenda se ocorrer um erro de leitura ou
gravação? Explique.


Em situações onde ocorre uma falha de hardware, problemas de permissão, disco cheio ou corrupção de dados durante a **leitura** ou a **gravação**, os impactos na agenda são distintos:

---

### 1. Se ocorrer um erro durante a leitura (`carregar_agenda`)

* **Tratamento parcial (ex.: `FileNotFoundError`):**
O programa prevê que o arquivo possa não existir na primeira execução e inicia uma agenda vazia em memória.
* **Erros não tratados ou de formatação (ex.: `PermissionError`, dados corrompidos):**
* **Interrupção inesperada:** Se o arquivo não tiver permissão de leitura ou o disco falhar, o Python lançará uma exceção não capturada e o programa será encerrado abruptamente.
* **Perda de acesso aos dados prévios:** Os contatos contidos no disco não serão transferidos para a memória do programa.
* **Risco de sobrescrita subsequente:** Se o erro não for tratado adequadamente e o usuário prosseguir cadastrando dados e salvando, o arquivo antigo (que não pôde ser lido) pode ser completamente sobrescrito por uma agenda em branco ou parcial.



---

### 2. Se ocorrer um erro durante a gravação (`salvar_agenda`)

A operação de gravação padrão é executada abrindo o arquivo no modo `"w"` (`with open(..., "w")`):

* **Truncação imediata do arquivo:**
No exato momento em que `open(..., "w")` é chamado, o sistema operacional esvazia (zera) o arquivo em disco para prepará-lo para a nova escrita.
* **Falha durante a escrita (ex.: falta de espaço no disco, queda de energia, remoção do pendrive):**
* **Corrupção ou perda total:** Se a escrita falhar no meio do processo, o arquivo anterior já terá sido truncado e o novo estará incompleto ou com 0 bytes.
* **Perda dos dados do disco:** Os dados gravados anteriormente no arquivo são permanentemente perdidos.



---

### Como prevenir esses problemas?

1. **Tratamento robusto de exceções (`try/except` abrangente):**
Capturar falhas genéricas de I/O (`IOError`, `OSError`, `PermissionError`) tanto na leitura quanto na escrita, informando o usuário sem abortar o aplicativo.
2. **Gravação atômica via arquivo temporário (melhor prática):**
Gravar primeiro em um arquivo temporário auxiliar (ex.: `agenda.tmp`). Somente após a escrita e o fechamento serem concluídos sem falhas, o programa renomeia/substitui o arquivo principal (`os.replace("agenda.tmp", "agenda.txt")`). Dessa forma, se a gravação falhar no meio, a versão antiga intacta permanece preservada no disco.
'''
