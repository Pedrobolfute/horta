document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault()
    const formData = new FormData(this)
    try{
        const response = await fetch('/change/', {
            method: 'POST',
            body: formData,
        })
        const data = await response.json()
        if(data.status === 'success'){
            window.location.href = '/login/'
        } else if(data.status === 'invalid') {
            alert(data.message)
            window.location.href = '/change/'
        }else if(data.status === 'empty'){
            alert(data.message)
        }
    } catch(error){
        alert('Error processing solicitation')
    }
}
)

console.log('opa')