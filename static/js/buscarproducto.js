    const eliminarTildes = (texto) => { return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "") ;}
    
    const pushearListaFiltrada = ()  =>{
        let carr = JSON.parse(localStorage.getItem('carrito')) || []
        localStorage.setItem('carrito', JSON.stringify(carr))
        const filtro = document.querySelector("#buscar").value 
        const UL = document.querySelector(".lista-filtrada-ul")
        let checkboxes = document.querySelectorAll(".categoria")

        const categoriasSeleccionadas = Array.from(checkboxes)
                .filter(checkbox => checkbox.checked)
                .map(checkbox => checkbox.value);

        UL.innerHTML = ""
        listaFiltrada = []
        menusFiltrados = []

        if (categoriasSeleccionadas.length === 0){
            for (let menu in menus){
                menusFiltrados.push(menu)
            }
        }
        else{
            menusFiltrados = categoriasSeleccionadas;
        }
        menusFiltrados.forEach(menu =>{
            let lista = menus[menu]; // [ {} {} {} {} ... {}]
            lista.forEach(elemento => {
                // for( const k in elemento){
                //     let texto = eliminarTildes(k).toLowerCase()
                //     if(filtro === "" || texto.includes(filtro)){
                //         listaFiltrada.push(elemento)
                //     }
                // }
                let texto = eliminarTildes(elemento.nombre).toLowerCase()
                if (filtro === "" || texto.includes(filtro)){
                    listaFiltrada.push(elemento)
                }
            });  
        })

        listaFiltrada.forEach(elemento => {       
            let IMG = document.createElement('img')
            let LI = document.createElement('li')
            let Titulo = document.createElement('h2')
            let Precio = document.createElement('p')
            let BtonAdd = document.createElement('button')

            IMG.src = elemento.img
            IMG.className = "lista-filtrada-img"
            LI.dataset.descripcion = elemento.nombre
            LI.className = "lista-filtrada-li"
            Titulo.innerHTML = elemento.nombre
            Titulo.className = "lista-filtrada-titulo" 
            Precio.innerHTML = "$"+ parseFloat(elemento.precio)
            Precio.className = "lista-filtrada-precio"
            BtonAdd.innerHTML = 'Comprar'
            BtonAdd.className = 'lista-filtrada-btn-add-carrito'


            LI.appendChild(IMG)
            LI.appendChild(Titulo)
            LI.appendChild(Precio)
            LI.appendChild(BtonAdd)
            UL.appendChild(LI)

            BtonAdd.addEventListener("click", () =>{
                console.log("hizo click")
                let carrito = JSON.parse(localStorage.getItem('carrito'))
                elemento.cantidad = 1
                carrito.push(elemento)
                localStorage.setItem('carrito', JSON.stringify(carrito))
            })
        })
    }

    const INPUT_SEARCH = document.querySelector("#buscar")

    pushearListaFiltrada()

    INPUT_SEARCH.addEventListener('input', pushearListaFiltrada)

    const checkboxes = document.querySelectorAll(".categoria")
    checkboxes.forEach(checkbox =>{
        checkbox.addEventListener("change", () =>{
            pushearListaFiltrada()})
    })