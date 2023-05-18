let i = 0
let speed =  250
let txt = "Ifeanyi Yahweh Aghasili";
function type_it() {
    if(i < txt.length) {
        document.getElementById("name").innerHTML += txt.charAt(i);
        i++;
        setTimeout(type_it, speed);
    }
}

let greeting;

let d = new Date();
let hour = d.getHours();

function get_time(){
    
    if(hour < 12) {
        greeting = "Good Morning"
        // document.getElementById("time").innerHTML = greeting;
    }
    else if(hour < 16 | hour === 12) {
        greeting = "Good Afternoon"
        // document.getElementById("time").innerHTML = greeting;
    }
    else {
        greeting = "Good Evening"
        // document.getElementById("time").innerHTML = greeting;
    }

    function type_it() {
        
    }
    document.getElementById("time").innerHTML = greeting;
}

function y(){
    
    let value = window.scrollY
    // console.log(value)
    const v2 = 500;
    const hidden = document.getElementById('intro');
    if(value < (v2/2)) {
        hidden.style.opacity = "1"
        hidden.style.transition = "opacity .5s ease"
    }
    else {
        hidden.style.opacity = "0"
        hidden.style.transition = "opacity .5s ease"
    }
}


// function dor() {
    
//     setInterval(function random(){
//         const randomNum = Math.floor(Math.random() * 41)
//         const randomNum2 = Math.floor(Math.random() * 61)
//         const randomNum3 = Math.floor(Math.random() * 21)
//         console.log(randomNum + '%', randomNum2)
//         const blob = document.getElementById('blob')
//         blob.style.top = randomNum3 + '%';
//         blob.style.left = randomNum + '%'
//         const blob2 = document.getElementById('blob2')
//         blob2.style.left = randomNum2 + '%';
//         blob2.style.bottom = randomNum + '%'
//         const blob3 = document.getElementById('blob3')
//         blob3.style.bottom = randomNum2 + '%';
//         blob3.style.left = randomNum3 + '%'
//     }, 750)
   
// }


function grow() {
    const deee = document.getElementById('des')
    console.log("working somehow")
    deee.style.animation = "grow 1s forwards ease"
}


function vn() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            // console.log(entry)
            if (entry.intersectionRatio) {
                entry.target.classList.add('showing')
            } else {
                 entry.target.classList.remove('showing')
            }
        }) 
    })
    
    const elements = document.querySelectorAll('.section')
    elements.forEach((el) => observer.observe(el))

    
    // const biobtn = document.getElementById('biobtn')
    // const left = biobtn.offsetLeft
    // const right = biobtn.offsetHeight
    // const top = biobtn.offsetTop
    // const bottom = biobtn.offsetWidth
    // console.log(top, right, left, bottom)

    // const biobtn = document.getElementById('skbtn')
    // const left = biobtn.offsetLeft
    // const right = biobtn.offsetHeight
    // const top = biobtn.offsetTop
    // const bottom = biobtn.offsetWidth
    // console.log(top, right, left, bottom)
}

const modlBox = () => {
    const cards = document.querySelectorAll('.card')
    for(let i = 0; i < cards.length; i++) {
        const card = cards[i]
        
        card.onclick = () => {
            const srcLink = card.getAttribute('src')
            const modl = document.getElementById('modl')
            const img = document.getElementById('modlimg')
            img.setAttribute('src', srcLink)
            modl.classList.remove('hide')
            modl.classList.add('show')
            
            console.log(srcLink)
        }
    }
}

const doThis = () => {
    const modl = document.getElementById('modl')
    modl.classList.remove('show')
    modl.classList.add('hide')
}