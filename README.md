## Visão Interna do Tesseract - Simulação 3D
Este projeto é uma simulação visual de um tesseract, ou hipercubo, em que se projeta a forma geométrica de 4 dimensões (4D) para 3 dimensões (3D), permitindo a visualização a partir de diferentes ângulos. O código utiliza a biblioteca `matplotlib` para gerar gráficos 3D, rotacionando e projetando o tesseract de modo que suas conexões internas sejam exibidas em um espaço 3D.

**Como Funciona:**

- `Vértices do Tesseract`: O tesseract é definido em 4D por 16 vértices, representandos como coordenadas no espaço 4D. Estes vértices formam as conexões de um hipercubo.
- `Projetção 4D para 3D`: Para visualizar o tesseract, as coordenadas 4D são projetadas para um espaço 3D através de uma série de transformações e rotações matriciais. Esta projeção simula como o tesseract parecia se visto de diferentes ângulos.
- `Animação`: O tesseract é rotacionado continuamente, e a visualização resultante é atualizada em tempo real, mostrando diferentes perspectivas da forma geométrica conforme ela se transforma.
- `Rotação e Perspectiva`: A rotação é aplicada nos planos XY, XZ, YW e ZW, em uma sequênica que permite que todos os aspectos do tesseract sejam explorados visualmente. A perspectiva resultante demonstra como uma pessoa poderia ver diferentes conexões entre os cubos ao "cair" dentro de um tesseract.

 **Requisitos**

 - Python 3.x
 - Biblioteca `matplotlib`
 
  **Como Executar**:

  - Instale as dependências com `pip install matplotlib`.
  - Execute o script em um ambiente Python compatível.
 
  Este projeto ilustra conceitos avançados de geometria e visualização multidimencional, proporcionando um experiência interativa para entender a complexidade de objetos em 4D.

  ## O que é um Tesseract?
  
  Um tesseract, também conhecido como hipercubo de quatro dimensões (4D), é a generalização do cubo tridimensional (3D) para uma quarta dimensão. É uma figura geométrica abstrata que representa o conceito de um cubo em um espaço de quatro dimensões.

  **Estrutura de um Tesseract**
  - Vertices: Um tesseract possui 16 vértices. Estes são os pontos onde as arestas se encontram, como mencionei anteriormente.
  - Arestas: O tesseract tem 32 arestas, que são as linhas conectando os vértices.
  - Faces: Ele possui 24 faces quadradas, que são as superfícies planas formadas pelas arestas.
  - Células: No tesseract, cada célula é um cubo tridimensional. Ele tem 8 dessas células.
 
  ## Projeção e Visualização
  Visualizar um tesseract é desafiador porque não podemos diretamente representar quatro dimensões em um espaço tridimensional. Em vez disso, usamos projeções e transformações para criar uma representação visual:

  - `Projeção 4D para 3D`: Para visualizar o tesseract, suas coordenadas em 4D são projetadas para um espaço 3D. Isso envolve cálculos matemáticos para reduzir a complexidade e mostrar uma representação mais compreensível.
  - `Transformações`: O tesseract pode ser rotacionado em diferentes planos e ângulos. Essas rotações ajudam a visualizar diferentes aspectos e conexões entre suas partes.
  - `Simulação Interna`: A simulação interna do tesseract tenta mostrar como seria a visão dentro dele. Isso envolve a projeção de suas células e faces de maneira que o observador possa perceber a complexidade do hipercubo.


  
