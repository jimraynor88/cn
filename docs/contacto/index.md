---
title: Contacto cifrado
description: Envíame un mensaje seguro con PGP
hide:
  - navigation
  - toc
---

# Contacto cifrado con PGP

Si quieres comunicarte conmigo de forma segura, utiliza este formulario. Tu mensaje se cifrará con mi clave pública y necesito tu clave pública para responderte de forma cifrada. **Puedes pegar tu clave o generar una nueva abajo.**

---

## 📝 Enviar mensaje cifrado

<div class="pgp-contact">

<div class="form-group">
  <label for="userName">Tu nombre o alias:</label>
  <input type="text" id="userName" placeholder="Ej: Juan Pérez" value="">
  <small>Obligatorio para identificarte.</small>
</div>

<div class="form-group">
  <label for="userContact">Tu contacto (email, Telegram, etc.):</label>
  <input type="text" id="userContact" placeholder="ejemplo@dominio.com o @usuario" value="">
  <small>Obligatorio para que pueda responderte.</small>
</div>

<div class="form-group">
  <label for="senderPubKey">Tu clave pública (obligatoria):</label>
  <textarea id="senderPubKey" rows="2" placeholder="Pega aquí tu clave pública PGP..."></textarea>
  <small>Debe empezar por <code>-----BEGIN PGP PUBLIC KEY BLOCK-----</code>.</small>
  <button type="button" id="generateKeyBtn" style="margin-top: 0.5rem;">🔑 Generar nuevo par de claves con mis datos</button>
</div>

<div id="keygenArea" style="display: none; margin-top: 1rem; padding: 0.5rem; border: 1px solid var(--md-default-fg-color--lighter); border-radius: 8px;">
  <button id="copyPubToFormBtn">📋 Pegar clave</button>
  <button id="downloadPubBtn">💾 Bajar clave pública</button>
  <button id="downloadPrivBtn">🔒 Bajar clave privada</button>
  <p class="warning" style="margin-top: 0.5rem;">⚠️ Guarda tus claves. Impórtalas a tu gestor de claves.<br>(Más info en la sección de  <a href="https://soyel.de/seguridad/pgp">Seguridad - PGP</a>)<br>Sin la clave privada, no podrás descifrar mis respuestas.</p>
</div>

<div class="form-group">
  <label for="message">Tu mensaje (texto plano):</label>
  <textarea id="message" rows="2" placeholder="Escribe aquí tu mensaje..."></textarea>
</div>

<div class="form-group">
  <label for="status">Estado:</label>
  <div id="status" style="margin-top: 0.5rem;"></div>
</div>

<div class="form-group action-buttons">
  <button id="encryptBtn">1. Cifrar</button>
  <button id="copyBtn" disabled>2. Copiar</button>
  <button id="sendBtn" disabled>3. Enviar</button>
</div>

<div class="form-group">
  <label for="encryptedResult">Mensaje cifrado (resultado):</label>
  <textarea id="encryptedResult" rows="3" readonly style="font-family: monospace;"></textarea>
  <small>Puedes copiarlo por si acaso.</small>
</div>

</div>

<script src="/js/openpgp.min.js"></script>
<script>
// ==================== TU CLAVE PÚBLICA (sin comentarios) ====================
const myPublicKeyArmored = `-----BEGIN PGP PUBLIC KEY BLOCK-----

xjMEaeRhURYJKwYBBAHaRw8BAQdA7e9GnK8CGBnr5t1bb6zZoYy9cUn0rEGY
Dcy97Hg2QurNG1BHUEBTb3lFbC5EZSA8UEdQQFNveUVsLkRlPsKMBBAWCgA+
BYJp5GFRBAsJBwgJkNP5iIW/02ftAxUICgQWAAIBAhkBApsDAh4BFiEEfBFQ
HIi/vrYNWvaL0/mIhb/TZ+0AAENAAP9YsnmsRn1KqCdBnxGK+XLnsbxAJE4c
7o1oqUj7B8+QpQEA4YZ1/JDVRpxCbX+UW/3wHJHVyjr/f8fP+lcYjRwvqAHO
OARp5GFREgorBgEEAZdVAQUBAQdAgnda3jj8kjacoJfA630q3wsbDh/x4TbN
lttgRYB+M18DAQgHwngEGBYKACoFgmnkYVEJkNP5iIW/02ftApsMFiEEfBFQ
HIi/vrYNWvaL0/mIhb/TZ+0AAM34AQC+pNxjHt8VF/DyDj+YWYsVoRlx+1wN
A7C53YAoiyvVNAD/aT/VT0OWrjRa2WnhbEqe8+jSpudyImo6MydyI92rgAk=
=I7Oi
-----END PGP PUBLIC KEY BLOCK-----`;

// ==================== DOM Elements ====================
const userNameEl = document.getElementById('userName');
const userContactEl = document.getElementById('userContact');
const senderKeyEl = document.getElementById('senderPubKey');
const messageEl = document.getElementById('message');
const encryptedResultEl = document.getElementById('encryptedResult');
const statusEl = document.getElementById('status');
const encryptBtn = document.getElementById('encryptBtn');
const copyBtn = document.getElementById('copyBtn');
const sendBtn = document.getElementById('sendBtn');
const generateKeyBtn = document.getElementById('generateKeyBtn');
const keygenArea = document.getElementById('keygenArea');
const copyPubToFormBtn = document.getElementById('copyPubToFormBtn');
const downloadPubBtn = document.getElementById('downloadPubBtn');
const downloadPrivBtn = document.getElementById('downloadPrivBtn');

let currentEncrypted = '';
let lastGeneratedPublic = '';
let lastGeneratedPrivate = '';

function setStatus(text, isError = false) {
  statusEl.innerHTML = `<span style="color: ${isError ? 'red' : 'green'};">${text}</span>`;
}

function isPublicKeyValid(pubKey) {
  const trimmed = pubKey.trim();
  return trimmed.startsWith('-----BEGIN PGP PUBLIC KEY BLOCK-----') &&
         trimmed.endsWith('-----END PGP PUBLIC KEY BLOCK-----');
}

async function encryptMessageWithTimeout(publicKeyArmored, plaintext, timeoutMs = 30000) {
  const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Tiempo de espera agotado.')), timeoutMs)
  );
  const encryptPromise = (async () => {
    const publicKey = await openpgp.readKey({ armoredKey: publicKeyArmored });
    const message = await openpgp.createMessage({ text: plaintext });
    return await openpgp.encrypt({ message, encryptionKeys: publicKey });
  })();
  return await Promise.race([encryptPromise, timeoutPromise]);
}

async function generateKeyWithNameAndContact(name, contact) {
  let userID = name;
  if (contact) userID += ` <${contact}>`;
  return await openpgp.generateKey({
    type: 'ecc',
    curve: 'ed25519',
    userIDs: [{ name: userID }],
    format: 'armored'
  });
}

function downloadKey(key, filename) {
  const blob = new Blob([key], { type: 'application/pgp-keys' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// === Generar clave ===
generateKeyBtn.addEventListener('click', async () => {
  const name = userNameEl.value.trim();
  const contact = userContactEl.value.trim();
  if (!name) {
    setStatus('❌ Introduce tu nombre o alias.', true);
    return;
  }
  generateKeyBtn.disabled = true;
  generateKeyBtn.textContent = 'Generando...';
  keygenArea.style.display = 'none';
  try {
    const { privateKey, publicKey } = await generateKeyWithNameAndContact(name, contact);
    lastGeneratedPublic = publicKey;
    lastGeneratedPrivate = privateKey;
    keygenArea.style.display = 'block';
    setStatus('✅ Claves generadas. Puedes usarlas.');
  } catch (err) {
    setStatus('❌ Error al generar claves: ' + err.message, true);
  } finally {
    generateKeyBtn.disabled = false;
    generateKeyBtn.textContent = '🔑 Generar nueva clave con mis datos';
  }
});

copyPubToFormBtn.addEventListener('click', () => {
  if (!lastGeneratedPublic) {
    setStatus('❌ Primero genera las claves.', true);
    return;
  }
  senderKeyEl.value = lastGeneratedPublic;
  setStatus('✅ Clave pública añadida al formulario.');
});

downloadPubBtn.addEventListener('click', () => {
  if (!lastGeneratedPublic) {
    setStatus('❌ Primero genera las claves.', true);
    return;
  }
  const name = userNameEl.value.trim().replace(/\s+/g, '_') || 'anonymous';
  downloadKey(lastGeneratedPublic, `${name}_public.asc`);
});

downloadPrivBtn.addEventListener('click', () => {
  if (!lastGeneratedPrivate) {
    setStatus('❌ Primero genera las claves.', true);
    return;
  }
  const name = userNameEl.value.trim().replace(/\s+/g, '_') || 'anonymous';
  downloadKey(lastGeneratedPrivate, `${name}_private.asc`);
});

// === Cifrar mensaje ===
encryptBtn.addEventListener('click', async () => {
  const name = userNameEl.value.trim();
  const contact = userContactEl.value.trim();
  const plaintext = messageEl.value.trim();
  const senderPubKey = senderKeyEl.value.trim();

  if (!name || !contact || !plaintext || !senderPubKey) {
    setStatus('❌ Completa todos los campos (nombre, contacto, mensaje, clave pública).', true);
    return;
  }
  if (!isPublicKeyValid(senderPubKey)) {
    setStatus('❌ La clave pública no tiene el formato correcto.', true);
    return;
  }

  setStatus('🔐 Cifrando mensaje...');
  encryptBtn.disabled = true;
  copyBtn.disabled = true;
  sendBtn.disabled = true;
  encryptedResultEl.value = '';

  try {
    let fullMessage = `De: ${name} (${contact})\n\n${plaintext}\n\n--- Clave pública del remitente ---\n${senderPubKey}`;
    const encrypted = await encryptMessageWithTimeout(myPublicKeyArmored, fullMessage);
    currentEncrypted = encrypted;
    encryptedResultEl.value = encrypted;
    setStatus('✅ Mensaje cifrado. Ahora puedes copiarlo o enviarlo.');
    copyBtn.disabled = false;
    sendBtn.disabled = false;
  } catch (err) {
    setStatus(`❌ Error: ${err.message}`, true);
    encryptBtn.disabled = false;
  }
});

copyBtn.addEventListener('click', async () => {
  if (!currentEncrypted) return setStatus('❌ No hay mensaje cifrado.', true);
  try {
    await navigator.clipboard.writeText(currentEncrypted);
    setStatus('📋 Copiado al portapapeles.');
  } catch (err) {
    setStatus('❌ No se pudo copiar.', true);
  }
});

// Envío con reintento y detección de bloqueo
async function sendWithRetry(url, data, retries = 1) {
  for (let i = 0; i <= retries; i++) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 30000);
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        signal: controller.signal
      });
      clearTimeout(timeoutId);
      if (response.ok) return { ok: true };
      else return { ok: false, error: await response.text() };
    } catch (err) {
      let errorMsg = err.message;
      if (err.message.includes('Failed to fetch') || err.name === 'TypeError') {
        errorMsg = 'El navegador bloqueó la conexión. Desactiva los escudos de Brave o usa otro navegador.';
      }
      if (i === retries) return { ok: false, error: errorMsg };
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }
  return { ok: false, error: 'Máximo de reintentos' };
}

sendBtn.addEventListener('click', async () => {
  if (!currentEncrypted) {
    setStatus('❌ Primero cifra el mensaje.', true);
    return;
  }
  setStatus('📡 Enviando...');
  sendBtn.disabled = true;
  copyBtn.disabled = true;
  const result = await sendWithRetry('https://mimail.jimraynor.workers.dev', { text: currentEncrypted }, 1);
  if (result.ok) {
    setStatus('✅ Mensaje enviado. Recibiré tu mensaje cifrado.');
    // Limpiar formulario
    userNameEl.value = '';
    userContactEl.value = '';
    senderKeyEl.value = '';
    messageEl.value = '';
    encryptedResultEl.value = '';
    currentEncrypted = '';
    copyBtn.disabled = true;
    sendBtn.disabled = true;
    const oldDiv = document.getElementById('manualInstructions');
    if (oldDiv) oldDiv.remove();
  } else {
    let errorMsg = `❌ Error: ${result.error}`;
    setStatus(errorMsg, true);
    let manualDiv = document.getElementById('manualInstructions');
    if (!manualDiv) {
      manualDiv = document.createElement('div');
      manualDiv.id = 'manualInstructions';
      manualDiv.style.marginTop = '1rem';
      manualDiv.style.padding = '0.5rem';
      manualDiv.style.backgroundColor = '#f8f9fa';
      manualDiv.style.border = '1px solid #ccc';
      manualDiv.style.borderRadius = '4px';
      document.querySelector('.pgp-contact').appendChild(manualDiv);
    }
    manualDiv.innerHTML = `
      <strong>⚠️ Envío automático falló. Puedes enviar el mensaje manualmente:</strong><br>
      Copia el texto cifrado de arriba y envíalo por correo a <strong>pgp@soyel.de</strong><br>
     `;
    sendBtn.disabled = false;
    copyBtn.disabled = false;
  }
});

// Limpiar mensaje manual si hay cambios
function resetManual() {
  const div = document.getElementById('manualInstructions');
  if (div) div.remove();
}
userNameEl.addEventListener('input', resetManual);
userContactEl.addEventListener('input', resetManual);
messageEl.addEventListener('input', resetManual);
senderKeyEl.addEventListener('input', resetManual);
</script>

<style>
.pgp-contact textarea, .pgp-contact input {
  width: 100%;
  box-sizing: border-box;
  margin: 0.5rem 0;
  padding: 0.5rem;
  font-family: monospace;
}
button {
  margin: 0.25rem;
  padding: 0.5rem 1rem;
  background-color: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: var(--md-accent-fg-color);
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.form-group {
  margin-bottom: 1rem;
}
.action-buttons {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
small {
  display: block;
  margin-top: -0.25rem;
  color: #666;
}
.warning {
  margin-top: 0.5rem;
  padding: 0.5rem;
  background-color: #fff3cd;
  color: #856404;
  border-radius: 4px;
}
</style>
