    const eliminarTildes = (texto) => { return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "") ;}
    
    const pushearListaFiltrada = ()  =>{
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
                for( const k in elemento){
                    let texto = eliminarTildes(k).toLowerCase()
                    if(filtro === "" || texto.includes(filtro)){
                        listaFiltrada.push(elemento)
                    }
                }
                
            });  
        })

        listaFiltrada.forEach(elemento => {       
            let IMG = document.createElement('img')
            let LI = document.createElement('li')
            let Titulo = document.createElement('h2')
            let Precio = document.createElement('p')
            let BtonAdd = document.createElement('button')
            for(const k in elemento){
                IMG.src = elemento[k]
                IMG.className = "lista-filtrada-img"
                LI.dataset.descripcion = k
                LI.className = "lista-filtrada-li"
                Titulo.innerHTML = k
                Titulo.className = "lista-filtrada-titulo" 
                Precio.innerHTML = "$8000"
                Precio.className = "lista-filtrada-precio"
                BtonAdd.innerHTML = 'Comprar'
                BtonAdd.className = 'lista-filtrada-btn-add-carrito'
            }
            LI.appendChild(IMG)
            LI.appendChild(Titulo)
            LI.appendChild(Precio)
            LI.appendChild(BtonAdd)
            UL.appendChild(LI)
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