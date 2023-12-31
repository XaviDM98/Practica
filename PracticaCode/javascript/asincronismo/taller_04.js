const saludar = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log(`Hola ${nombre}.`)
            resolve(nombre)
        }, 1000) 
    })
}

const hablar = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log(`Bla, bla, bla...`)
            resolve(nombre)
        }, 1000) 
    })
}

console.log('Iniciando conversacion...')
saludar('Xavier')
    .then( (dato) => hablar( dato ) )
    .then( (dato) => console.log( dato ) )