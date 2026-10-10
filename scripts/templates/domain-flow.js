(() => {
  'use strict';
  const flow = JSON.parse(document.getElementById('flow-data').textContent);
  const get = id => document.getElementById(id);
  const stage = document.querySelector('.stage');
  const messages = new Map(flow.messages.map(message => [message.step, message]));
  const routeSelect = get('route-select');
  let route = flow.routes[0];
  let position = 0;
  let buttons = [];

  for (const item of flow.routes) {
    const option = document.createElement('option');
    option.value = item.id;
    option.textContent = item.label;
    routeSelect.append(option);
  }
  get('route-field').hidden = flow.routes.length === 1;
  get('steps-panel').open = !window.matchMedia('(max-width: 720px)').matches;

  function routeSteps() { return route.steps.map(step => messages.get(step)); }
  function text(id, value) { get(id).textContent = value; }
  function make(tag, value, className) {
    const element = document.createElement(tag);
    if (value) element.textContent = value;
    if (className) element.className = className;
    return element;
  }

  function buildSteps() {
    get('steps').replaceChildren();
    get('print-steps').replaceChildren();
    buttons = routeSteps().map((message, index) => {
      const li = make('li');
      const button = make('button');
      button.type = 'button';
      const name = make('span', message.name, 'step-name');
      name.append(make('small', message.kind));
      button.append(make('span', `${flow.code}.${message.step}`, 'step-id'), name);
      button.addEventListener('click', () => { position = index; render(); });
      li.append(button);
      get('steps').append(li);
      const printable = make('li');
      printable.append(make('h3', `${flow.code}.${message.step} · ${message.name}`),
        make('p', `${message.kind}: ${message.sender} → ${message.receiver}`),
        make('p', `Datos: ${message.data}`), make('p', `Condición: ${message.condition}`));
      get('print-steps').append(printable);
      return button;
    });
  }

  function render(updateUrl = true) {
    const steps = routeSteps();
    const message = steps[position];
    stage.dataset.kind = message.kind;
    text('step-position', `Paso ${position + 1} de ${steps.length} · ${flow.code}.${message.step}`);
    text('message-kind', message.kind);
    text('message-title', message.name);
    text('sender', message.sender);
    text('receiver', message.receiver);
    text('sender-label', message.sender === message.receiver ? 'Contexto que inicia' : 'Emisor');
    text('receiver-label', message.sender === message.receiver ? 'El mismo contexto' : 'Receptor');
    text('connection-label', message.sender === message.receiver ? 'Acción interna' : 'Envía el mensaje');
    text('message-data', message.data);
    text('message-condition', message.condition);
    text('route-description', route.description);
    text('completion', position === steps.length - 1 ? 'Has llegado al final de esta ruta.' : '');
    text('announcement', `Paso ${position + 1} de ${steps.length}. ${message.kind}: ${message.name}. De ${message.sender} a ${message.receiver}.`);
    get('previous').disabled = position === 0;
    get('next').disabled = position === steps.length - 1;
    get('restart').disabled = position === 0;
    buttons.forEach((button, index) => {
      if (index === position) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    const traveller = document.querySelector('.traveller');
    // Replay only the message's short transit, never hide content while animating.
    traveller.style.animation = 'none';
    void traveller.getBoundingClientRect();
    traveller.style.animation = '';
    if (updateUrl) {
      const hash = new URLSearchParams({ruta: route.id, paso: String(position + 1)});
      history.replaceState(null, '', `#${hash}`);
    }
  }

  function readLocation() {
    const params = new URLSearchParams(location.hash.slice(1));
    route = flow.routes.find(item => item.id === params.get('ruta')) || flow.routes[0];
    const requested = Number(params.get('paso'));
    position = Number.isInteger(requested) && requested >= 1 ? Math.min(requested - 1, route.steps.length - 1) : 0;
    routeSelect.value = route.id;
    buildSteps();
    render(false);
  }
  function move(delta) {
    const next = Math.max(0, Math.min(route.steps.length - 1, position + delta));
    if (next !== position) { position = next; render(); }
  }
  get('previous').addEventListener('click', () => move(-1));
  get('next').addEventListener('click', () => move(1));
  get('restart').addEventListener('click', () => { position = 0; render(); });
  routeSelect.addEventListener('change', () => {
    route = flow.routes.find(item => item.id === routeSelect.value);
    position = 0;
    buildSteps();
    render();
  });
  get('flow-select').addEventListener('change', event => { location.href = event.target.value; });
  document.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || event.target.closest('select,input,textarea,[contenteditable]')) return;
    if (event.key === 'ArrowRight') { event.preventDefault(); move(1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); move(-1); }
  });
  window.addEventListener('hashchange', readLocation);
  readLocation();
})();
