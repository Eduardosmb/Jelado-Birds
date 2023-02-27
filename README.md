# Jelado-Wars
Este é um projeto desenvolvido para a disciplina "Algebra Linear e Teoria da informação" do 3°semestre de ciências da computação do Insper. Nele foi criado um jogo em Pygame com a temática baseada no famoso jogo Angry Birds, mas com um toque espacial. O objetivo do jogo é obter a maior pontuação possível, destruindo os jelados. O jogo possui dois modos de dificuldade: fácil e difícil. 

## Como jogar

Para jogar, basta mirar com a própria seta do mouse e apertar o botão do mouse para atirar o projetil em direção aos jelados. O jogador deve destruir as naves inimigas e coletar jelados para marcar pontos. O jogo tem dois modos de dificuldade, fácil e difícil, para que o jogador possa escolher o nível de desafio que prefere. No modo fácil, tem apenas 1 planeta com campo gravitacional, enquanto no modo difícil, tem 2 planetas com campos gravitacionais.
Sobre os planetas, eles possuem um campo gravitacional, onde influencia na trajetória do projétil, que tem por objetivo destruir as naves inimigas. Vale ressaltar também como funciona o campo gravitacional do planeta, no caso isso se torna possível devido à aplicação da fórmula de atração entre corpos, que calcula a aceleração devida à gravidade a cada iteração para cada partícula. É importante lembrar que a aceleração gravitacional é um vetor com magnitude |a| = c/d**2, onde "c" é uma constante e "d" é a distância entre os dois corpos. Esse vetor é sempre direcionado para o corpo celeste que exerce a atração. Ao multiplicar a magnitude de "a" pela sua direção, obtemos um vetor que é somado ao vetor "v" de cada objeto, influenciando o trajeto dos mesmos na tela e gerando um jogo divertido. Além disso, cada planeta possui um campo gravitacional diferente, o que torna o jogo mais desafiador. Caso queira ver mais especificamente, basta acessar o arquivo "main.py"e verificar as linhas 302 a 307, onde está a fórmula de atração entre corpos.

## Gameplay

![gif-jelado-wars](https://user-images.githubusercontent.com/101536778/221229375-7b31fb7b-d09c-4228-b123-5a2bbf6ffeae.gif)


## Requisitos
Para jogar o jogo, é necessário ter as bibliotecas Pygame e Numpy instalados em sua máquina.

## Instalação
Para instalar o Pygame, abra o terminal e execute o seguinte comando:

- `pip install pygame`
- `pip install numpy`

Após a instalação do Pygame, baixe o projeto do repositório e execute o arquivo main.py para iniciar o jogo.

## Desenvolvedores
Este projeto foi desenvolvido por Enzo Quental e Eduardo Barros.

## Contribuições
Contribuições para o jogo são sempre bem-vindas! Se você quiser contribuir para o projeto, por favor, crie uma nova branch e faça um pull request para nós.
