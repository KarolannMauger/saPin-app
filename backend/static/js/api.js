const API = {
  getState(){ return fetch('/api/state').then(r=>r.json()); },
  setState(body){
    return fetch('/api/state', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body:JSON.stringify(body)
    }).then(r=>r.json());
  },
  getPatterns(){ return fetch('/api/patterns').then(r=>r.json()); },
  addPattern(p){
    return fetch('/api/patterns', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body:JSON.stringify(p)
    }).then(r=>r.json());
  },
  delPattern(id){ return fetch(`/api/patterns/${id}`, {method:'DELETE'}).then(r=>r.json()); },
};
