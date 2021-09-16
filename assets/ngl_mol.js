// create a `stage` object
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        ngl_mol: function (v_id, v_child, in_value) {
            
            console.log(v_id)
            // Get the number of canvas
            let canvas_container = document.getElementById(v_id)
            let n_childs = canvas_container.children.length
            // console.log(n_childs) 
            // console.log('Test') 

            // If canvas already exist
            if (n_childs > 0) {
                // Remove all childs before create a new element
                canvas_container.innerHTML = '';
            } 

            let stage = new NGL.Stage(v_id);
            stage.loadFile("https://raw.githubusercontent.com/jRicciL/MD_namd_python/master/dm_sources_1L2Y/1-topologia/tc5b.pdb")
                .then(
                    function (component) {
                    // add a "cartoon" representation to the structure component
                    component.addRepresentation("cartoon");
                    // provide a "good" view of the structure
                    component.autoView();
                    }
                );
            

            
        } 
    }
});