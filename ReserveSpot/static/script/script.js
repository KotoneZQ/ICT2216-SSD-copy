// Get the modal(s) by class name
const modals = document.getElementsByClassName('smodal');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    for (let i = 0; i < modals.length; i++) {
        if (event.target === modals[i]) {
            modals[i].style.display = "none";
        }
    }
}
function toggleForms() {
    const modal1 = document.getElementById('loginmodal');
    const modal2 = document.getElementById('registermodal');

    if (modal1.style.display === 'none' || modal1.style.display === '') {
        modal1.style.display = 'block';
        modal2.style.display = 'none';
    } else {
        modal1.style.display = 'none';
        modal2.style.display = 'block';
    }
}

function openTab(evt, tabName) {
    let i, tabcontent, tablinks;
    
    // Get all elements with class "tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    // Get all elements with class "tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}
