    const eliminarTildes = (texto) => { return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "") ;}
    
    const pushearListaFiltrada = ()  =>{
        const filtro = document.querySelector("#buscar").value 
        const UL = document.querySelector(".filtrado")
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
                        listaFiltrada.push(texto)
                    }
                }
                
            });  
        })

        listaFiltrada.forEach(item => {        
            let LI = document.createElement('li')
            LI.textContent = item 
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