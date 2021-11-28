# Servidor do ENEM 2019 quiz.

Para iniciar o servidor localmente por favor execute os seguintes comandos:

docker build -t enem-quiz .

docker run -p 3000:3000  -d enem-quiz

Entre em seu navegador web preferido e vá para: [Quiz nota do ENEM](http://localhost:3000/)
