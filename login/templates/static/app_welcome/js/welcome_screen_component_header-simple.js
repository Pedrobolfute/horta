const addAnimal = document.querySelector('.animal.add');
const animalForm = addAnimal.querySelector('.animal-form');
const animalOwner = document.querySelector('#owner')

// Expande o card e exibe o formulário ao clicar no card
addAnimal.addEventListener('click', (e) => {
  e.stopPropagation(); // Evita que o evento se propague para o clique global
  addAnimal.classList.add('expanded');
  animalForm.style.display = 'flex';
});

// Fecha o card se clicar fora ou se o botão de adicionar for clicado
document.addEventListener('click', (e) => {
  if (!addAnimal.contains(e.target)) {
    addAnimal.classList.remove('expanded');
    animalForm.style.display = 'none';
  }
});

// Lógica para o botão de adicionar animal
animalForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const selectedAnimal = document.querySelector('#animal-select').value;
  const animalColor = document.querySelector('#animal-color').value;
  const owner = sessionStorage.getItem('owner');

  if (!animalColor) {
    alert("Cadastro inválido: O campo de cor não pode estar vazio.");
    return; // Interrompe o envio do formulário
  }

  try {
    const response = await fetch(animalForm.action, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // Certifique-se de incluir o CSRF token
      },
      body: new URLSearchParams({
        animal: selectedAnimal,
        color: animalColor,
        owner: owner,
      }),
    });

    const result = await response.json();
    console.log(result);

    // Verifica se o cadastro foi bem-sucedido
    const animalsList = document.querySelector('.animals');
    if (response.ok && result.message) {
      alert("Animal cadastrado com sucesso!");

      updateHeaderCounts(selectedAnimal);

      
      // Adiciona o novo animal na lista dinamicamente
      const imgBase = animalForm.dataset.imgBase;

      const newAnimal = document.createElement('li');
      newAnimal.classList.add('animal');
      newAnimal.innerHTML = `
        <span class="number">#${result.new_animal_id}</span>
        <span class="name">${selectedAnimal.charAt(0).toUpperCase() + selectedAnimal.slice(1)}</span>
        <div class="detail">
          <ol class="types">
            ${result.food_list.length > 0 ? result.food_list.map(food => `<li class="type">${food}</li>`).join('') : '<li class="type">Sem alimentos cadastrados</li>'}
          </ol>
          <img src="${imgBase}${selectedAnimal}.svg" alt="${selectedAnimal}">
        </div>
      `;
      animalsList.insertBefore(newAnimal, addAnimal);



      // Resetar os campos do formulário
      animalForm.reset();

      // Fechar o card após cadastro
      addAnimal.classList.remove('expanded');
      animalForm.style.display = 'none';
    } else {
      alert("Erro ao cadastrar animal: " + result.error || "Tente novamente.");
    }
  } catch (err) {
    console.error('Erro ao enviar o formulário:', err);
  }
});

function handleLogout() {
  // Limpa o sessionStorage
  sessionStorage.clear();
  // Redireciona para a página de login
  window.location.href = '/login'; // Atualize para a URL correta do login
}

// Atualiza a contagem no header
function updateHeaderCounts(specie) {
  const specieKey = specie.toLowerCase(); // Normalizar a espécie para evitar inconsistências
  const headerCounts = document.querySelector('.animal-count ul');
  const specieItem = headerCounts.querySelector(`li[data-specie="${specieKey}"]`);

  if (specieItem) {
    // Incrementa a contagem existente
    const currentCount = parseInt(specieItem.dataset.count, 10) || 0;
    specieItem.dataset.count = currentCount + 1;
    specieItem.textContent = `${specie.charAt(0).toUpperCase() + specie.slice(1)}: ${currentCount + 1}`;
  } else {
    // Adiciona uma nova linha para a espécie
    const newSpecieItem = document.createElement('li');
    newSpecieItem.dataset.specie = specieKey;
    newSpecieItem.dataset.count = 1;
    newSpecieItem.textContent = `${specie.charAt(0).toUpperCase() + specie.slice(1)}: 1`;
    headerCounts.appendChild(newSpecieItem);
  }
}

document.querySelector('header h1').innerHTML += `, ${sessionStorage.getItem('owner')}!`