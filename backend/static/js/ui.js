const brightness = document.getElementById('brightness');
const colorsDiv  = document.getElementById('colors');
const applyBtn   = document.getElementById('apply');
const saveBtn    = document.getElementById('save');
const list       = document.getElementById('patterns');

function currentColors(){
  return Array.from(colorsDiv.querySelectorAll('input[type=color]')).map(i=>i.value.toUpperCase());
}

async function refreshPatterns(){
  const items = await API.getPatterns();
  list.innerHTML = '';
  items.forEach(p=>{
    const li = document.createElement('li');
    li.className='list-group-item d-flex justify-content-between align-items-center';
    li.innerHTML = `<span>${p.name}</span>
      <div class="d-flex gap-2">
        <button class="btn btn-sm btn-outline-success">Appliquer</button>
        <button class="btn btn-sm btn-outline-danger">Supprimer</button>
      </div>`;
    li.querySelector('.btn-outline-success').onclick = ()=>API.setState({brightness:p.brightness, colors:p.colors});
    li.querySelector('.btn-outline-danger').onclick = async()=>{ await API.delPattern(p.id); refreshPatterns(); };
    list.appendChild(li);
  });
}

applyBtn.onclick = ()=>API.setState({brightness:Number(brightness.value), colors: currentColors()});
saveBtn.onclick  = async ()=>{
  const name = prompt('Nom du pattern ?') || 'Preset';
  await API.addPattern({name, brightness:Number(brightness.value), colors: currentColors()});
  refreshPatterns();
};

refreshPatterns();
API.getState().then(s=>{ if(s?.brightness!=null) brightness.value = s.brightness; });
