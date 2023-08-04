let articulos = [
    { nombre: 'TV Sony', modelo: 'KD-65X85J LA8', costo: 1999 },
    { nombre: 'Audifonos Inalambricos', modelo: 'WH-CH710N', costo: 259 },
    { nombre: 'Auriculares inalámbricos con Noise Cancelling', modelo: 'WF1000XM4/BMUC', costo: 321.9 },
    { nombre: 'Smart TV Samsung', modelo: '55" AU7000 UHD 4K', costo: 884 },
    { nombre: 'Laptop Lenovo', modelo: 'Core i3 1ma, 1tb, 12gb, touch, 15 pulg', costo: 656.25 },
    { nombre: 'Laptop Dell', modelo: 'Core i7 11va, 512gb ssd, 16gb, tec iluminado', costo: 1207.51 }
]

const imprimirArticulo = (objeto) => {
    console.log( `${objeto.nombre} - ${objeto.modelo}, Valor: ${objeto.costo}` )
}

console.log('==================================')
console.log('Uso del FOREACH')
console.log('==================================')

articulos.forEach( function(elemento) {
    console.log( elemento.nombre )
} )

articulos.forEach( imprimirArticulo )

console.log('==================================')
console.log('Uso del SOME')
console.log('==================================')

let articulos_baratos = articulos.some( (articulo) => articulo.costo <= 100 )
console.log( articulos_baratos )

const existen_articulos_caros = (dato) => dato.costo > 1000

let articulos_caros = articulos.some( existen_articulos_caros )
console.log( articulos_caros )

console.log('==================================')
console.log('Uso del FILTER')
console.log('==================================')