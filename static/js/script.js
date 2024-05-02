document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menu");
    const h2Elements = document.querySelectorAll(".options h2");

    // Toggle menu
    menuToggle.addEventListener("click", toggleMenu);

    // Toggle options
    h2Elements.forEach(function(h2) {
        h2.addEventListener("click", toggleOptions);
    });

    // Update footer
    updateFooter();
});

function toggleMenu() {
    menu.classList.toggle("collapsed");
}

function toggleOptions() {
    const nextUl = this.nextElementSibling;
    const chevronIcon = this.querySelector(".fas.fa-chevron-down");

    if (nextUl.style.display === "block") {
        nextUl.style.display = "none";
        chevronIcon.style.transform = "";
        chevronIcon.style.top = "";
    } else {
        nextUl.style.display = "block";
        chevronIcon.style.transform = "rotate(-90deg)";
        chevronIcon.style.top = "10px";
    }
}