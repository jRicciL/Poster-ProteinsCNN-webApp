// create a `stage` object
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        ngl_mol: function (v_id, representation) {
 
            // Get the number of canvas
            let canvas_container = document.getElementById(v_id)
            let n_children = canvas_container.children.length

            // If at least one canvas already exist
            if (n_children > 0) {
                // Remove all children before create a new element
                canvas_container.textContent = '';
            } 

            let stage = new NGL.Stage(v_id, {backgroundColor:'white'});
            stage.loadFile("https://raw.githubusercontent.com/jRicciL/MD_namd_python/master/dm_sources_1L2Y/1-topologia/tc5b.pdb")
                .then(
                    function (component) {
                    component.addRepresentation(representation);
                    component.autoView();
                    }
                );
        } 
    }
});


    
