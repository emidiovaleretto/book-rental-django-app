const html = document.querySelector("html")
const btnSwitch = document.getElementById("btn-switch")

btnSwitch.addEventListener("click", (event) => {
    event.preventDefault

    html.classList.toggle("dark")
})