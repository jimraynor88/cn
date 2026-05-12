---
title: "Servicios"
hide:
  - navigation
  - toc
---

<style>
/* Estilos para la página de donaciones - basados en tus variables */
:root {
  --primary-color: #123f9a;
  --primary-light: #3a66c7;
  --primary-dark: #0b2c6f;
}

.donation-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.donation-header {
  text-align: center;
  margin-bottom: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 16px;
}

.donation-header h1 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.donation-header p {
  font-size: 1.1rem;
  color: #555;
}

/* Recuadro de copia */
.copy-box {
  background-color: var(--primary-dark);
  color: white;
  padding: 1.5rem;
  border-radius: 12px;
  margin: 2rem 0;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.lightning-address {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin: 1rem 0;
}

.lightning-address code {
  background: white;
  color: var(--primary-dark);
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 1.1rem;
  word-break: break-all;
}

.copy-button {
  background-color: #ffc107;
  color: #333;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.2s;
}

.copy-button:hover {
  background-color: #e0a800;
  transform: translateY(-1px);
}

.copy-feedback {
  margin-top: 8px;
  font-size: 0.85rem;
  opacity: 0.8;
}

/* Grid de tarjetas */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
  margin: 2rem 0;
}

.service-card {
  background-color: var(--md-default-bg-color);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

.card-header {
  background-color: var(--primary-color);
  color: white;
  padding: 1rem;
  text-align: center;
}

.card-header h3 {
  margin: 0;
  font-size: 1.3rem;
}

.card-body {
  padding: 1.5rem;
  flex-grow: 1;
}

.price {
  font-size: 1.8rem;
  font-weight: bold;
  color: var(--primary-color);
  margin: 0.5rem 0;
  text-align: center;
}

.description {
  color: #555;
  margin-bottom: 1rem;
  text-align: center;
}

.card-footer {
  padding: 1rem;
  text-align: center;
  border-top: 1px solid #eee;
}

.pay-button {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 30px;
  cursor: pointer;
  font-weight: bold;
  text-decoration: none;
  display: inline-block;
  transition: background 0.2s;
}

.pay-button:hover {
  background-color: var(--primary-light);
}

.tip-card .card-header {
  background-color: #28a745;
}

/* Instrucciones */
.instructions {
  background-color: #f1f3f5;
  padding: 1.5rem;
  border-radius: 12px;
  margin: 2rem 0;
}

.instructions ol {
  margin-left: 1.5rem;
}

.instructions li {
  margin: 0.5rem 0;
}

.alert {
  background-color: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
}

/* Responsive */
@media (max-width: 768px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }
  .lightning-address {
    flex-direction: column;
  }
}
</style>

<div class="donation-container">

<div class="donation-header tip-card">
  <h1>☕️ ¡Gracias por tu apoyo!</h1>
  <p>Puedes contribuir con lo que desees o solicitar cualquiera de los servicios que ofrezco. Elige el método que prefieras.</p>
  <div class="card-footer">
    <button class="pay-button" onclick="payWithPayPal(5, 'Invitar al Café')">Invitar al Café</button>
  </div>
</div>

<!-- Recuadro de copia dirección Lightning (Bitrefill) -->
<div class="copy-box">
  <h3>⚡ Propinas a Bitcoin Lightning</h3>
  <p>Mi dirección Lightning (Bitrefill):</p>
  <div class="lightning-address">
    <code id="lightningAddr">jimraynor@bitrefill.me</code>
    <button class="copy-button" onclick="copyLightningAddress()">Copiar dirección</button>
  </div>
  <div id="copyFeedback" class="copy-feedback"></div>
  <p class="alert" style="background: rgba(255,255,255,0.2); color: white;">Esta dirección acepta importes cuantificados en Euros, y pagados en BTC dentro de la red Lightning. <br>Introduce el importe correspondiente en EUR y Bitrefill muestra los BTC a enviar.<br><br>Para otras criptos, pedir dirección temporal en privado.</p>
</div>

<!-- Tarjetas de Servicios y Propinas -->
<div class="cards-grid">
  <!-- Asesoría personal -->
  <div class="service-card">
    <div class="card-header">
      <h3>🎧 Asesoría personal (Llamada 1h)</h3>
    </div>
    <div class="card-body">
      <div class="price">28,10 €</div>
      <div class="description">Llamada de una hora para resolver tus dudas, orientación, guía, apoyo o consultoría personalizada.</div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="payWithPayPal(28.10, 'Asesoría personal 1h')">Pagar 28,10 €</button>
    </div>
  </div>

  <!-- Acceso a la sección Seguridad/Utilidades -->
  <div class="service-card">
    <div class="card-header">
      <h3>🔐 Acceso a Seguridad / Utilidades</h3>
    </div>
    <div class="card-body">
      <div class="price">12,80 €</div>
      <div class="description">Acceso completo a la sección privada con herramientas, guías y utilidades de seguridad.</div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="payWithPayPal(12.80, 'Acceso Seguridad/Utilidades')">Pagar 12,80 €</button>
    </div>
  </div>

  <!-- Acceso a mi Carta Natal -->
  <div class="service-card">
    <div class="card-header">
      <h3>🔮 Acceso a mi Carta Natal</h3>
    </div>
    <div class="card-body">
      <div class="price">8,21 €</div>
      <div class="description">Tener accceso a mi Carta Natal no solo te da información clave acerca de mi de forma exclusiva, te ayudará a tratar conmigo, a comprender por qué soy como soy, y cual es mi naturaleza.<br>A su vez, quizás te animes a pedir tu propia Carta Natal Personificada al comprobar cómo las hago y por qué son tan especiales.</div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="payWithPayPal(8,21, 'Acceso a mi Carta Natal')">Pagar 8,21 €</button>
    </div>
  </div>


  <!-- Carta Natal Personalizada -->
  <div class="service-card">
    <div class="card-header">
      <h3>✨ Carta Natal Personalizada</h3>
    </div>
    <div class="card-body">
      <div class="price">182 €</div>
      <div class="description">Tu propia Carta Natal Personificada, sentirás que te habla de si misma/o y a su vez de ti misma/o, conectando con ella (contigo) a un nivel que nunca creíste imaginar. Por fín comprenderás tu carta natal, porque te habla de tu a tu, para que la conozcas.</div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="payWithPayPal(182, 'Carta Natal Personalizada')">Pagar 182 €</button>
    </div>
  </div>

  <!-- Web básica -->
  <div class="service-card">
    <div class="card-header">
      <h3>🌐 Web como la mía (básica)</h3>
    </div>
    <div class="card-body">
      <div class="price">Desde 500 €</div>
      <div class="description">Creación de una web estática con MkDocs y Material, personalizada a tu gusto. Consulta antes para presupuesto exacto desde el formulario de <a href="https://soyel.de/contacto">contacto</a>.</div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="location.href='https://soyel.de/contacto'">Consultar</button>
    </div>
  </div>

</div>

<!-- Instrucciones de uso -->
<div class="instructions">
  <h3>📘 Cómo pagar o donar</h3>
  <ol>
    <li><strong>Con PayPal</strong>: Haz clic en el botón "Pagar" de la tarjeta correspondiente. Se abrirá PayPal, selecciona o introduce el importe requerido en OTROS, y selecciona el concepto desde la lista de debajo. (Requiere cuenta PayPal o tarjeta bancaria).</li>
    <li><strong>Con Bitcoin Lightning</strong>: Copia la dirección lightning <code>jimraynor@bitrefill.me</code> usando el botón de arriba. Luego abre tu monedero Lightning (Wallet of Satoshi, Zeus, Blixt, etc.), selecciona "Enviar a dirección Lightning" y pega la dirección. Introduce el importe en euros (si tu monedero lo permite) o en satoshis equivalentes. Servicio prestado por Bitrefill.</li>
    <li><strong>Para servicios</strong>: Una vez realizado el pago, contáctame desde el formulario de contacto o desde los enlaces a mis RRSS de aquí abajo con el comprobante para coordinar.</li>
  </ol>
  <div class="alert">
    💡 <strong>Nota sobre Lightning</strong>: Al usar Bitrefill, el pagador verá el cambio EUR → BTC en tiempo real. Bitrefill acredita el saldo en euros a mi cuenta (yo puedo gastarlo directamente en su tienda). Es una forma sencilla de recibir pagos pequeños sin gestionar un nodo.
  </div>
</div>

</div>

<script>
// Función para copiar la dirección Lightning
function copyLightningAddress() {
  const addr = document.getElementById('lightningAddr').innerText;
  navigator.clipboard.writeText(addr).then(() => {
    const feedback = document.getElementById('copyFeedback');
    feedback.innerText = '✅ ¡Dirección copiada! Pégala en tu monedero Lightning.';
    setTimeout(() => { feedback.innerText = ''; }, 3000);
  }).catch(() => {
    alert('No se pudo copiar. Cópiala manualmente: ' + addr);
  });
}

// Función para redirigir a PayPal con importe y descripción
//function payWithPayPal(amount, itemName) {
  // Asegurar que amount sea número con dos decimales
  //const fixedAmount = parseFloat(amount).toFixed(2);
  // URL de PayPal con tus datos (sustituye TU_EMAIL@proveedor.com por tu email de PayPal)
  //const paypalUrl = `https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=TU_EMAIL@proveedor.com&item_name=${encodeURIComponent(itemName)}&amount=${fixedAmount}&currency_code=EUR&return=${encodeURIComponent(window.location.origin)}/gracias/&cancel_return=${encodeURIComponent(window.location.href)}`;
  //window.open(paypalUrl, '_blank');
function payWithPayPal(amount, itemName) {
  const url = `https://www.paypal.com/donate/?hosted_button_id=QE7KUXLT3XQ6Y`;
  window.open(url, '_blank');
}

// Para el desplegable de propina, puedes hacer que al cambiar el select se actualice el botón o simplemente pasar el valor.
// Por simplicidad, ya está en el onclick del botón.
</script>

<!-- Nota: Reemplaza TU_EMAIL@proveedor.com por tu email real de PayPal. Si prefieres usar el botón de donación de PayPal con hosted_button_id, puedes modificar la función payWithPayPal. -->
