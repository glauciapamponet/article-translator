# Processo de ciclo de vida de aprendizado de máquina

* Criar e operar uma carga de trabalho típica de ML é um processo iterativo e consiste em várias fases. Identificamos essas fases vagamente com base no modelo de processo de padrão aberto para Cross Industry Standard Process Data Mining (CRISP-DM) como uma diretriz geral. 
  * O CRISP-DM é usado como linha de base porque é uma ferramenta comprovada no setor e é neutro em termos de aplicação, o que o torna uma metodologia fácil de aplicar que é aplicável a uma ampla variedade de pipelines e cargas de trabalho de ML. 
  * 
O processo de ML de ponta a ponta inclui as seguintes fases:
    * Identificação de metas de negócios 
    * Enquadramento de problemas de ML
    *Recolha de dados
    * Integração e preparação de dados
    * Engenharia de recursos
    * Treinamento de modelo
    * Validação do modelo
    * Avaliação de negócios
    * Implantação de produção (implantação de modelo e inferência de modelo)
  * Este artigo apresenta uma visão geral de alto nível das várias fases de um ciclo de vida de ML de ponta a ponta, o que ajuda a estruturar nossa discussão sobre segurança, conformidade e operacionalização das práticas recomendadas de ML, que serão úteis em nossas postagens posteriores no blog.
#
O processo de ciclo de vida do machine learning
  * A figura anterior descreve o processo de ciclo de vida do ML, juntamente com os especialistas no assunto e as partes interessadas de negócios envolvidas em diferentes estágios do processo. Também é importante observar que o ciclo de vida do ML é um processo interativo.
[! [Descrição da imagem](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyapti32u87scnstv7osv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyapti32u87scnstv7osv.png)  
_The process_ do ciclo de vida do aprendizado de máquina
##
Fase 1
  * A Fase 1 é definir o problema e os objetivos do negócio. Especialistas em domínio e proprietários de empresas estão mais envolvidos nesta parte, determinando as métricas de sucesso. Os KPIs e a determinação dos requisitos regulatórios e de conformidade também se enquadram nessa fase. Os cientistas de dados normalmente trabalham com as PMEs para enquadrar o problema de negócios de uma forma que lhes permita desenvolver uma solução de ML viável.
##
Fase 2
  * A Fase 2 envolve a coleta e preparação de todos os dados relevantes de várias fontes de dados. Essa função geralmente é desempenhada por engenheiros de dados com experiência em ferramentas de big data para extração, transformação e carregamento de dados (ETL). É importante garantir que os dados tenham controle de versão e a linhagem dos dados seja rastreada para fins de auditoria e conformidade. 
  * Uma vez que os conjuntos de dados brutos estão disponíveis, os cientistas de dados realizam a exploração de dados, determinam os recursos de entrada e as variáveis de destino, análise de valores discrepantes e transformações de dados necessárias que podem ser necessárias. Também é importante garantir que quaisquer transformações aplicadas aos dados de treinamento também possam ser aplicadas na produção no momento da inferência.
##
Fase 3
  * Em seguida, é a fase de desenvolvimento e avaliação do modelo. Os cientistas de dados determinam a estrutura que desejam usar, definem conjuntos de dados fora da amostra e fora do tempo e experimentam vários algoritmos de ML, hiperparâmetros, em alguns casos, adicionam dados de treinamento adicionais.
##
Fase 4
  * Em seguida, você pega os modelos treinados e os executa em conjuntos de dados fora do tempo e fora de amostra, e escolhe o modelo ou modelos que retornam os melhores resultados próximos às métricas determinadas na Fase 1. Os artefatos de modelo e qualquer código correspondente devem ser versionados corretamente e armazenados em um repositório de código centralizado ou em um sistema de gerenciamento de artefatos.
  * Observe que esse estágio do processo é experimental e os cientistas de dados podem voltar ao estágio de coleta de dados ou engenharia de recursos se o desempenho do modelo for consistentemente ruim. Mais detalhes sobre dados e linhagem de artefatos de ML estão disponíveis na seção Rastreabilidade deste documento.
  * Os cientistas de dados também são obrigados a fornecer razões ou explicar a influência do recurso / modelo nas previsões. A interpretabilidade do modelo é discutida em seções posteriores.
##
Fase 5
  * A próxima fase é implantar os modelos em produção. Essa geralmente é a etapa mais impactante e difícil devido à lacuna entre as tecnologias e os conjuntos de habilidades usados para criar e implantar modelos em produção. 
  * Uma grande parte para tornar isso bem-sucedido requer intensa colaboração entre profissionais de infraestrutura, como engenheiros de DevOps, cientistas de dados, engenheiros de dados, especialistas em domínio, usuários finais e proprietários de empresas durante o processo de tomada de decisão. Deve haver métricas padronizadas e todos os tomadores de decisão devem ser capazes de interpretá-las diretamente.
  * Na maioria das organizações, os ciclos de vida dos modelos de ML terminam com a fase de implantação. Há uma necessidade de alguma forma de validação de sombra em que os modelos são implantados, mas não integrados ao fluxo de trabalho de produção para capturar as diferenças entre o treinamento e os dados em tempo real. 
  * Isso garante que o modelo continue a funcionar conforme o esperado ao receber dados de sistemas de produção. Depois que essa validação for bem-sucedida, as previsões do modelo poderão ser usadas em fluxos de trabalho de produção.
  * No entanto, para que os modelos de ML sejam eficazes a longo prazo, é necessário monitorar continuamente o modelo em tempo real (se possível) para determinar o desempenho dele, pois a precisão dos modelos pode diminuir com o tempo. 
  * Se o desempenho de um modelo diminuir abaixo de um determinado limite, talvez seja necessário treinar novamente e reimplantar seu modelo. 
* * *
Espero que este guia forneça uma visão geral de alto nível de Diferentes frases deCiclo de vida do aprendizado de máquina.
Deixe-me saber sua opinião na seção 👇 de comentários  
E se você ainda não o fez, certifique-se de me seguir nas alças abaixo:
👋 **conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/adit-modi-2a4362191/)**  
🤓 **conecte-se comigo no [Twitter](https://twitter.com/adi_12_modi)**  
🐱 💻 **siga-me no [github](https://github.com/AditModi)**  
✍️ **Faça o checkout [meus blogs](https://aditmodi.hashnode.dev)**
Curta, compartilhe e siga-me 🚀 para mais conteúdo.
[! [aditmodiimage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F497987%2Fedde8513-7308-4a4d-9592-2be160d074d2.png)
](/aditmodi)
##
[Adit Modi](/aditmodi)Seguir
[Engenheiro de nuvem sênior | Construtor de comunidades da AWS | 12x certificado pela AWS | 3x Azure Certified | Autor de Cloud Tech, DailyDevOps & BigDataJournal | Embaixador da HashiCorp | Levante "Capitão das Nuvens"](/aditmodi)
* * *
👨 💻 **Junte-se à nossa [Cloud Tech SlackCommunity](https://join.slack.com/t/cloudtechcommunity/shared_invite/zt-wptacj2f-Eu4PPvq6WEkBTHg7PR2ncA)**  
👋 **Siga-nos no [Linkedin](https://www.linkedin.com/company/cloud-techs) /[Twitter](https://twitter.com/AboutCloudTech) para as últimas notícias**  
💻 **Dê uma olhada em nosso[Github Repos](https://github.com/My-Machine-Learning-Projects-2020) para saber mais sobre nossos projetos**  
✍️ **Nosso[Site](https://cloudtech.hashnode.dev)**
* * *
[Guia de referência](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/modern-data-architecture.html)