# test_siglelton

O silgleton define que o objeto de uma classe seja criado apenas uma vez e utilizado por toda aplicação.

O lazy singleton espera até que o objeto seja usado pra criar a instancia da classe, após isso o objeto referenciado na memória será sempre o mesmo.

usos comuns: 
    - classe de logs
    - conexão com banco de dados
    

faz mais sentido usá-lo em situações onde serviços precisem ser instaciados apenas 1 vez. Provavelmente conectores ou até mesmo dependencias menores.
