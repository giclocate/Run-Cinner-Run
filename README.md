

<div align="center">
 
![logo_rcr5-removebg-preview_resized](https://github.com/giclocate/Game-P1/assets/107434982/fa710965-77e0-4f37-bb68-b8027464ffe6)

</div>


















# ‘RUN, CINER, RUN!’   
É um jogo 2D  desenvolvido com o emprego da linguagem python e algumas de suas bibliotecas com destaque para a pygame.  Foi idealizado  por alunos do Centro de Informática da UFPE como projeto final da disciplina de programação 1.

### Integrantes e divisão de trabalho  

__Amós Santana (akbs)__-implementação de obstáculos e gerenciamento.     
__Ana Luisa Feitosa (alfg)__ - implementação de coletáveis, pontuação e cenário.  
__Eric Makiyama (ehm2)__ -  implementação de sons, coletáveis e colisão.  
__Giovanna Clócate (gcca)__ - criação do repositório, modulação e personagem.  
__Lucas dos Santos (lss11)__ - organização da documentação e coletáveis.  
__Saunay Coutinho (svsc)__ - gerenciamento e implementação do menu.  

# Arquitetura e organização do código  
O jogo incorpora múltiplos sprites, manipulação de eventos, sistema de colisão, coleta de objetos e outras características. Vamos decompor a arquitetura e organização do código:  




### Estrutura Geral  
___Importações e Inicializações:___   
* O código começa importando módulos necessários, como pygame e várias classes de sprites. Além disso, inicializa os módulos de mixer de sons e fontes do Pygame, através do pygame.mixer.init e pygame.font.init, respectivamente.  

___Funções Auxiliares:___  
* Define uma função ‘exibir_texto’ para renderizar e exibir texto na tela do menu;
* Define uma função ‘exibe_mensagem’ para renderizar e exibir texto na tela. Isso é útil para mostrar informações como o contador de  pontuação ;
* Define uma função ‘exibe_mensagem2’ executa a mesma funcionalidade que ‘exibe_mensagem’ no entanto, com uma tipografia diferente ;

___Menu:___  
 * A função menu exibe o menu inicial do jogo, onde o jogador pode iniciar o jogo ou sair. Utiliza exibir_texto para mostrar as opções disponíveis e aguarda a entrada do usuário;

___Loop Principal (main):___   
* Inicializa o Pygame e configura a tela. Chama a função menu para processar a escolha do jogador. Carrega e reproduz a música de fundo;
* Cria grupos de sprites para diferentes categorias de objetos no jogo (como obstáculos e itens coletáveis) e adiciona os sprites a estes grupos;
* Implementa lógicas para movimentação do personagem, sistema de colisões, e coleta de itens;
* Atualiza a tela e os sprites, e verifica condições de fim de jogo (como colisões que resultam em game over).

### Organização do Código  

* O código segue uma estrutura modular, onde as funcionalidades estão atribuídas em funções específicas.
* O código foi divido em módulos conforme suas respectivas funções dentro das modulações (main.py; sprite.py; utils.py e menu.py) para uma melhor visualização e organização de mudanças e adição de códigos em cada funcionalidade
* Utiliza orientação a objetos para os sprites (por exemplo, Aluno, Nuvens, Ground), facilitando a manipulação de seus comportamentos e propriedades.
* Separa a lógica de inicialização e configuração do Pygame e da tela de jogo da lógica principal de gameplay dentro da função main.
* Emprega grupos de sprites do Pygame para gerenciar diferentes tipos de objetos no jogo, o que permite uma verificação eficiente de colisões e atualização dos objetos.




# Ferramentas, bibliotecas e frameworks utilizados  

### Ferramentas e Frameworks:   

* __Visual Studio Code:__ A utilização do VScode foi definida devido a sua integração com o Python e com o Github e por oferecer  recursos objetivos de edição, depuração e gerenciamento do código, além de uma variedade de extensões que podem auxiliar no desenvolvimento de jogos com Pygame.  

* __Git/Github:__ Utilizar o Git/GitHub foi importante para o desenvolvimento do código, pois permitiu o controle do trabalho colaborativo entre os membros da equipe, garantindo a atualização das alterações do código e facilitando o gerenciamento de mudanças no projeto.  

* __Notion:__ Recorrer ao Notion como principal ferramenta de organização foi essencial para o andamento do projeto pois é uma plataforma centralizada para documentação, planejamento e organização de tarefas, o que promoveu a colaboração eficiente e a gestão ágil do andamento do projeto.  

* __WhatsApp/Discord:__ Foram as ferramentas utilizadas como principal meio de comunicação interna e também com os monitores . 

### Bibliotecas:  

* __Pygame:__ Essa biblioteca foi interessante de ser utilizada devido à sua facilidade de aprendizado e funcionalidades para desenvolver jogos em Python, incluindo manipulação gráfica e sonora de forma eficiente, permitindo que o projeto fosse desenvolvido de forma rápida e mais acessível.  

* __Random:__ Não é uma biblioteca externa, mas sim um módulo padrão do Python que implementa geradores de números para várias distribuições. Seu uso foi muito indispensável porque permitiu a geração de elementos aleatórios, como a escolha de sons de colisão e a criação de objetos em posições variadas, adicionando elementos de imprevisibilidade e diversidade ao jogo, tornando-o mais dinâmico e interessante para o jogador.  

* __Sys:__ Essa biblioteca fornece variadas funções e variáveis, utilizadas em geral para manipular diferentes partes do ambiente de tempo de execução Python, permitindo operar no intérprete, no caso deste projeto foi utilizado a função ‘exit’, para encerrar o jogo.  


# Conceitos apresentados na disciplina aplicados ao projeto  
Alguns dos conceitos que vimos na disciplina e que estão presentes no código do projeto são:  

__Comandos condicionais:__   
* São utilizados para controlar o fluxo do programa com base em condições específicas.  
* Exemplo no código: estão presentes na parte do código que verifica eventos como pressionar uma tecla para iniciar o jogo (menu) ou para sair (menu).  

__Laços de repetição:__  
* São utilizados para executar um bloco de código repetidamente até que uma condição seja atendida.  
* Exemplo no código: Laços de repetição são encontrados nos loops while True no menu principal e no loop principal do jogo, onde o jogo é continuamente atualizado e renderizado.  

__Listas:__  
* São usadas para armazenar e manipular coleções de itens mutáveis.  
* Exemplo no código:, listas são utilizadas para armazenar grupos de sprites, como em ’all_sprites’ e ‘group_obstacles’.  

__Funções e escopo variável:__  
* Funções são blocos de código reutilizáveis que podem ser chamados em diferentes partes do programa. Variáveis têm escopos que determinam onde podem ser acessadas.  
* Exemplo no código: Funções são definidas para exibir texto na tela (exibir_texto) e para o menu (menu), enquanto variáveis locais e globais são usadas em diferentes partes do código.  

__Tuplas:__  
* Tuplas são utilizadas quando se deseja agrupar itens relacionados de forma a garantir que eles permaneçam juntos e na mesma ordem. 
* Exemplo no código: Tuplas foram utilizadas para definir a posição inicial do sprite do aluno na tela do jogo  ’self.rect.center=(100,ALTURA - 125)’.

# Desafios e erros enfrentados  

### Qual o maior erro que cometemos?  
Inicialmente começamos a desenvolver o código de forma não modulada pela não familiaridade com POO e classes. Esse com certeza foi nosso maior erro pois dificultou a organização inicial do código levando a potenciais erros de estruturação do código e afetou bastante a nossa otimização em meio ao prazo estipulado. Além disso, esse erro nos fez ficarmos dependentes dos commits uns dos outros para dar continuidade e andamento ao projeto.  

### Como lidamos? 
Esse problema logo foi resolvido, pois antes de dar andamento ao desenvolvimento do código optamos por aprender um pouco mais sobre modulação e começamos a dividir o código em classes e a utilizar programação orientada ao objeto. Isso aprimorou a organização do código e também a produtividade do time. Aprendemos a criação de branches de maneira adequada, os erros em relação aos commits nos obrigou a aprender a dar reset no commit anterior e com certeza nos fez aprender bastante.  


### Qual o maior desafio enfrentado? 
Inquestionavelmente o nosso maior desafio foi a utilização da ferramenta Github. Por ser um framework que nenhum dos integrantes do grupo tinha habilidade prática, tivemos que investir um tempo considerável no estudo de como  utilizá-lo, o que acarretou no atraso de algumas etapas do projeto devido ao curto tempo que tínhamos para desenvolvê-lo . 

### Como lidamos?
Prezamos por pesquisar e entender melhor o funcionamento da plataforma, fizemos isso por meio de videoaulas disponibilizadas pelos monitores, pesquisas em fóruns e principalmente com a ajuda de outros colegas desenvolvedores, que nos fizeram aprender vários métodos de utilização do Git e GitHub.

# Lições aprendidas durante o projeto
 Essa experiência de elaborar um jogo nos proporcionou valiosas lições sobre a importância das habilidades interpessoais, do trabalho em equipe e do compromisso com a busca ativa de conhecimento. Inicialmente, enfrentamos o desafio de não modularizar nosso código adequadamente, resultado de uma falta de familiaridade com POO, técnicas e até mesmo boas práticas de programação. Isso nos mostrou que a comunicação clara e a capacidade de colaborar são essenciais desde o início de qualquer projeto. Aprendemos que a habilidade de expressar ideias de forma eficaz e ouvir ativamente os integrantes da equipe é fundamental e o compartilhamento de conhecimento, principalmente, para evitar que alguém fique para trás.  
  Acerca do maior desafio que enfrentamos que foi a utilização do GitHub, uma ferramenta nova para todos nós, em vez de nos sentirmos sobrecarregados, encaramos isso como uma oportunidade de crescimento pessoal, profissional e acadêmico, pois entendemos que saber utilizar essa plataforma é uma demanda do sertor. Investimos tempo em aprender juntos, compartilhamos recursos e apoiamos uns aos outros durante o processo de aprendizado. Essa experiência destacou que a disposição para aprender, colaborar e apoiar a equipe são habilidades tão essenciais quanto as habilidades técnicas. Assim, aprendemos que muito além das hard skills as soft skills são fundamentais para o sucesso em equipe e no desenvolvimento pessoal contínuo.


# Capturas de tela
 
![image](https://github.com/giclocate/Game-P1/assets/107434982/91db1a3d-7992-4bfc-a8c2-3c8708dc294e)  
![image](https://github.com/giclocate/Game-P1/assets/107434982/4ddc289d-0f59-4b84-9b60-f0ad8c630a2d) 




