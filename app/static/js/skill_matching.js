function addSkill(input) {
    let x = input
    let y = 'skillinput ' + x;
    let z = 'skilluser ' + x;
    
    if (input == '') {
        // pass
    }
    else {
        // add skill to skill list
        document.getElementById('faehigkeiten_menu').insertAdjacentHTML('beforeend', '<div class="dropdown d-inline"><button class="btn btn-primary dropdown-toggle small-button skill-button" style="margin-right: 5px;" aria-expanded="false" data-bs-toggle="dropdown" id="' + y + '" type="button">' + x + '&nbsp;</button><div class="dropdown-menu"><a class="dropdown-item" onclick="nextTab(\'dashboardtab6\')">Analysieren</a><a class="dropdown-item" onclick="removeSkill(\'' + y + '\')">Entfernen</a></div></div>');
        
        if (document.getElementById('matching_skills').value == '') {
            document.getElementById('matching_skills').value = input;
        }
        else {
            let tempSkills = document.getElementById('matching_skills').value + ',' + input
            document.getElementById('matching_skills').value = tempSkills;
        }
        // clean input
        document.getElementById('keyword_input').value = ''
        }
    };

// remove skill
function removeSkill(skill) {
    let x = skill.slice(11);
    // convert to array
    let array = document.getElementById('matching_skills').value.split(',');
    // remove skill from array
    array = array.filter(e => e !== x);
    // convert back to string
    document.getElementById('matching_skills').value = array.join();   
    // remove from skill list
    document.getElementById(skill).parentNode.remove();
    // remove from users
    let matches = document.getElementById('profilepredictions').childElementCount -1;
    for (i = 0; i < matches; i++) {
        let ysliced = i + 'skilluser ' + x;
        document.getElementById(ysliced).parentNode.remove();
    }
};
