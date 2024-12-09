const addHorta = document.querySelector('.horta.add');
const hortaForm = addHorta.querySelector('.horta-form');
const hortaOwner = document.querySelector('#owner')

// Expande o card e exibe o formulário ao clicar no card
addHorta.addEventListener('click', (e) => {
  e.stopPropagation(); // Evita que o evento se propague para o clique global
  addHorta.classList.add('expanded');
  hortaForm.style.display = 'flex';
});

// Fecha o card se clicar fora ou se o botão de adicionar for clicado
document.addEventListener('click', (e) => {
  if (!addHorta.contains(e.target)) {
    addHorta.classList.remove('expanded');
    hortaForm.style.display = 'none';
  }
});

// Lógica para o botão de adicionar horta
hortaForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const selectedHorta = document.querySelector('#horta-select').value;
  const hortaColor = document.querySelector('#horta-color').value;
  const owner = sessionStorage.getItem('owner');

  if (!hortaColor) {
    alert("Cadastro inválido: a cor da cultura representa seu nutriente.");
    return; // Interrompe o envio do formulário
  }

  try {
    const response = await fetch(hortaForm.action, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // Certifique-se de incluir o CSRF token
      },
      body: new URLSearchParams({
        horta: selectedHorta,
        color: hortaColor,
        owner: owner,
      }),
    });

    const result = await response.json();
    console.log(result);

    // Verifica se o cadastro foi bem-sucedido
    const hortasList = document.querySelector('.hortas');
    if (response.ok && result.message) {
      alert("cultura cadastrada com sucesso!");

      updateHeaderCounts(selectedHorta);

      
      // Adiciona o novo horta na lista dinamicamente
      const imgBase = hortaForm.dataset.imgBase;

      const newHorta = document.createElement('li');
      newHorta.classList.add('horta');
      newHorta.innerHTML = `
        <span class="number">#${result.new_horta_id}</span>
        <span class="name">${selectedHorta.charAt(0).toUpperCase() + selectedHorta.slice(1)}</span>
        <div class="detail">
          <ol class="types">
            ${result.nutriente_list.length > 0 ? result.nutriente_list.map(nutriente => `<li class="type">${nutriente}</li>`).join('') : '<li class="type">Sem alimentos cadastrados</li>'}
          </ol>
          <img src="${imgBase}${selectedHorta}.svg" alt="${selectedHorta}">
        </div>
      `;
      hortasList.insertBefore(newHorta, addHorta);



      // Resetar os campos do formulário
      hortaForm.reset();

      // Fechar o card após cadastro
      addHorta.classList.remove('expanded');
      hortaForm.style.display = 'none';
    } else {
      alert("Erro ao cadastrar horta: " + result.error || "Tente novamente.");
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
  const headerCounts = document.querySelector('.horta-count ul');
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