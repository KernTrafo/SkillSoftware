// add missing user skill to user skill list
function addMissingWeiterbildungenSkill(input) {
    let x = input.parentNode.parentNode.firstChild.textContent;    
    let y = 'skilluser ' + x;

    // add skill to skill list
    document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<button class="btn btn-primary recommendation-button selected" id="' + y + '" type="button" onclick="removeUserSkill(this.id)">' + x + '<i class="fas fa-minus"></i></button>');
    
    // change missing to available
    input.parentNode.parentNode.firstChild.classList.toggle('skill-button');
    input.parentNode.parentNode.firstChild.classList.toggle('missing-skill-button');
    
    // remove focus on dropdown menu
    input.parentNode.parentNode.classList.toggle('show');
    
    if (input.parentNode.parentNode.firstChild.classList.contains('skill-button')) {
        input.innerHTML = 'Von meinen Skills entfernen';
    }
    else if (input.parentNode.parentNode.firstChild.classList.contains('missing-skill-button')) {
        input.innerHTML = 'Zu meinen Skills hinzufügen';
    }
}


// change color of bars
function weiterbildungenMatch() {
   // assign percentage from backend
    var weiterbildungen_percent_dict = {
        weiterbildungen0percent: 100,
        weiterbildungen1percent: 70,
        weiterbildungen2percent: 20,
    };
    
    // assign percentage from backend
    var weiterbildungen_ort_dict = {
        weiterbildungen0ort: 'Essen',
        weiterbildungen1ort: 'Meschede',
        weiterbildungen2ort: 'Biblis',
    };
    
    // assign percentage from backend
    var weiterbildungen_fachgebiet_dict = {
        weiterbildungen0fachgebiet: 'Maschinenbauer',
        weiterbildungen1fachgebiet: 'Ein weiterer Beruf',
        weiterbildungen2fachgebiet: 'Irgendein Beruf',
    };
    
    // assign percentage from backend
    var weiterbildungen_erfahrung_dict = {
        weiterbildungen0erfahrung: 'Senior',
        weiterbildungen1erfahrung: 'Junior',
        weiterbildungen2erfahrung: 'Professional',
    };

    // choose threshold for colors
    var green = 79;
    var yellow = 49; 

    // matching score
    var i = 0
    for(var key in weiterbildungen_percent_dict) {
        var value = weiterbildungen_percent_dict[key];
        let matchbar = 'weiterbildungenbar' + i;
        let matchbutton = 'weiterbildungenbutton' + i;
        
        document.getElementById(matchbar).style.height = value + '%';
        document.getElementById(matchbutton).textContent = value + '% Match';

        if (value > green) {
            document.getElementById(matchbar).style.backgroundColor = 'green';
        }
        else if (value > yellow) {
            document.getElementById(matchbar).style.backgroundColor = 'yellow';
        }
        else {
            document.getElementById(matchbar).style.backgroundColor = 'red';
        }
        i++;
    }
    
    // ort
    var i = 0
    for(var key in weiterbildungen_ort_dict) {
        var value = weiterbildungen_ort_dict[key];
        let matchort = 'ortweiterbildungen' +i;
        document.getElementById(matchort).textContent = value;
        i++;
    }
    
    // fachgebiet
    var i = 0
    for(var key in weiterbildungen_fachgebiet_dict) {
        var value = weiterbildungen_fachgebiet_dict[key];
        let matchfachgebiet = 'fachgebietweiterbildungen' + i;
        document.getElementById(matchfachgebiet).textContent = value;
        i++;
    }
    
    // erfahrung
    var i = 0
    for(var key in weiterbildungen_erfahrung_dict) {
        var value = weiterbildungen_erfahrung_dict[key];
        let matcherfahrung = 'erfahrungweiterbildungen' + i;
        document.getElementById(matcherfahrung).textContent = value;
        i++;
    }
}
 