function nextTab(nxtTab) {
    let nextTabToClick = document.getElementById(nxtTab);
    nextTabToClick.click();
    // scroll to top
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome, Firefox, IE, Opera
};
