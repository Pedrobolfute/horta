let checkbox_quest = document.querySelectorAll('.quest_label input:first-child')
let elementHidden = document.querySelectorAll('.more_info .hidden')
let cpfInput = document.querySelector('#cpf_id')

const checkbox_quest_size = checkbox_quest.length - 1

for(let i = 0; i <= checkbox_quest_size; i++){
    checkbox_quest[i].addEventListener('change', function(){
        let input = elementHidden[i].parentNode.querySelectorAll('input[type=text], input[type=number]')
        if(this.checked){
            elementHidden[i].removeAttribute('hidden')
        }else{
            input.forEach((value) => {
                value.value = ''
            })
            elementHidden[i].setAttribute('hidden', true)
        }
    })
}

document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault()
    const formData = new FormData(this)
    try{
        const response = await fetch('/register/', {
            method: 'POST',
            body: formData,
        })
        const data = await response.json()
        alert(data.message)
        if(data.status === 'created'){
            console.log('sim')
            window.location.href = '/login/'
        }
    } catch(error){
        alert('Error processing solicitation')
    }
})

cpfInput.addEventListener('change', function(){
    if(this.checked){
        cpfInput.setAttribute('value', 'CPF')
        console.log(cpfInput.value)
    }else{
        cpfInput.setAttribute('value', '')
        console.log(cpfInput.value)
    }
})