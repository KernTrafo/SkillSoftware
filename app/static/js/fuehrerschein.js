function addFuehrerschein(fuehrerschein) {
    let x = document.getElementById(fuehrerschein).textContent;
    
    // add fuehrerschein to selected list
    document.getElementById('fuehrerscheinauswahllist').insertAdjacentHTML('beforeend', '<button class="btn btn-primary fuehrerschein-button selected" id="' + fuehrerschein + '_selected" type="button" style="margin-right: 5px;" onclick="removeFuehrerschein(this.id)">' + x + '<i class="fas fa-minus"></i></button>');
    
    // remove from fuehrerscheins
    document.getElementById(fuehrerschein).remove(); 
    let y = 'data_fuehrerschein_' + x;
    document.getElementById(y).checked = true;
}


// remove fuehrerschein from selected list
function removeFuehrerschein(fuehrerschein) {
    let x = document.getElementById(fuehrerschein).textContent;

    // add back to fuehrerscheins
    document.getElementById('fuehrerscheinvorschlaegelist').insertAdjacentHTML('beforeend', '<button class="btn btn-primary fuehrerschein-button" id="' + fuehrerschein.slice(0, -9) + '" type="button" style="margin-right: 5px;" onclick="addFuehrerschein(this.id)">' + x + '<i class="fas fa-plus"></i></button>');
    
    // remove from selected items
    document.getElementById(fuehrerschein).remove(); 
    let y = 'data_fuehrerschein_' + x;
    document.getElementById(y).checked = false;
}
