## Visão Interna do Tesseract - Simulação 3D
Este projeto é uma simulação visual de um tesseract, ou hipercubo, em que se projeta a forma geométrica de 4 dimensões (4D) para 3 dimenções (3D), permitindo a visualização a partir de diferentes ângulos. O código utiliza a biblioteca `matplotlib` para gerar gráficos 3D, rotacionando e projetando o tesseract de modo que suas conexões internas sejam exibidas em um espaço 3D.

**Como Funciona:**

- `Vértices do Tesseract`: O tesseract é definido em 4D por 16 vértices, representandos como coordenadas no espaço 4D. Estes vértices formam as conexões de um hipercubo.
- `Projetção 4D para 3D`: Para visualizar o tesseract, as coordenadas 4D são projetadas para um espaço 3D através de uma série de treansformações e rotações matriciais. Esta projeção simula como o tesseract parecia se visto de diferentes ângulos.
- `Animação`: Otesseract é rotacionado continuamente, e a visualização resultante é atualizada em tempo real, mostrando diferentes perspectivas da forma geométrica conforme ela se transforma.
- `Rotação e Perspectiva`: A rotação é aplicada nos planos XY, XZ, YW e ZW, em uma sequênica que permite que todos os aspectos do tesseract sejam explorados visualmente. A perspectiva resultante demonstra como uma pessoa poderia ver diferentes conexões entre os cubos ao "cair" dentro de um tesseract.

- **Requisitos**

- - Python 3.x
  - Biblioteca `matplotlib`
 
  **Como Executar**:

  - Instale as dependências com `pip install matplotlib`.
  - Execute o script em um ambiente Python compatível.
 
  Este projeto ilustra conceitos avançados de geometria e visualizaçõa multidimencional, proporcionando um experiência interativa para entender a complexidade de objetos em 4D.
