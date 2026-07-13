function randomColor() {

    let letters = "0123456789ABCDEF";
    let color = "#";

    for(let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }

    return color;
}

function changeColor() {

    let color = randomColor();

    document.getElementById("colorBox").style.background = color;
    document.getElementById("colorCode").innerText = color;

    document.body.style.background = color;
}