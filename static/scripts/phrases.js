let inp = document.getElementById('pass')
let text = document.getElementById('phrase')
let vid = document.getElementById('vid')

inp.oninput = function () {
    if (!inp.value) {
        text.innerText = ''
        return
    }
    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/phrases/check?pass=' + inp.value)
    xhr.onload = () => {
        if (xhr.status == 201) {
            let src = document.createElement('source')
            src.type = 'video/webm'
            src.src = 'data:video/webm;base64,' + xhr.response
            vid.appendChild(src)
            vid.hidden = false
            vid.width = 800
            text.hidden = true
            inp.hidden = true
        } else if (xhr.status == 200) {
            text.innerText = xhr.responseText
        } else {
            alert('ONLY DIGITS')
        }
    }
    xhr.send()
}