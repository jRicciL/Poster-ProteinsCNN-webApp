

// create a `stage` object
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        ngl_mol_cdk2_conf: function (
            v_id, 
            conf_id = '1fin',
            representation = 'cartoon') {
 
            // Get the number of canvas
            let canvas_container = document.getElementById(v_id)
            let n_children = canvas_container.children.length

            // If at least one canvas already exist
            if (n_children > 0) {
                // Remove all children before create a new element
                canvas_container.textContent = '';
            } 

            let pdb_path = "https://raw.githubusercontent.com/jRicciL/Poster-ProteinsCNN-webApp/main/data/pdb_files/"
            pdb_path += conf_id
            pdb_path += '_ENS.pdb'
            var colors = {
                '1fin': '#DA5D5C',
                '4fku': '#27879C',
                '3pxf': '#EDA953',
                '5a14': '#2F917C'
            }
            var clear_colors = {
                '1fin': '#F7ABAA',
                '4fku': '#6ECBE0',
                '3pxf': '#FBD6A7',
                '5a14': '#58CCB4'
            }
            let color = colors[conf_id] 
            let clear_color = clear_colors[conf_id]

            let stage = new NGL.Stage(v_id, 
                {
                    backgroundColor:'#273139',
                    zoomSpeed: 0.8,
                    rotateSpeed: 0.8,
                    fogNear: 40
                });
            
            window.addEventListener( "resize", function( event ){
                stage.handleResize();
            }, false );
            
            stage.loadFile(pdb_path)
                .then(
                    function (component) {
                        let sele = "sidechainAttached and (7-19 or 29-32 or 64-65 or 79-89 or 128-133 or 142-148)"

                        component.addRepresentation(
                            representation, 
                            {color: color}
                            );
                        component.addRepresentation(
                            'surface', 
                            {
                             sele: "not hetero",
                             color: clear_color,
                             filterSele: '(7-19 or 29-32 or 64-65 or 79-89 or 128-133 or 142-148)',
                             surfaceType: "av",
                            //  colorScheme: "hydrophobicity",
                             scaleFactor: 1.2,
                            //  probeRadius: 2,
                             contour: true,
                            }
                        );
                        component.addRepresentation(
                            "licorice", 
                            {sele: sele,
                            //  color: "#E75F5E",
                             radius: 0.5}
                            );
                            //'(7-19 or 29-32 or 63-65 or 78-89 or 128-133 or 142-145)'
                        component.autoView('(7-19 or 29-32 or 64-65 or 79-89 or 128-133 or 142-148)');
                    }
                );
        } 
    }
});


    
