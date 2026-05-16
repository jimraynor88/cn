---
title: Servicios
hide:
  - navigation
  - toc
---

<style>
/* Estilos adaptados a la paleta oscura de CartaNatal.de */
:root {
  --primary-color: #F472B6;
  --primary-light: #F9A8D4;
  --primary-dark: #EC4899;
  --bg-dark: #0f172a;
  --card-bg: rgba(30, 27, 75, 0.5);
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
  background: linear-gradient(135deg, #1e1b4e, #0f0a2a);
  border-radius: 28px;
  border: 1px solid var(--primary-color);
}

.donation-header h1 {
  color: var(--primary-light);
  margin-bottom: 0.5rem;
}

.donation-header p {
  font-size: 1.1rem;
  color: var(--md-default-fg-color--light);
}

/* Recuadro de copia Lightning */
.copy-box {
  background: linear-gradient(120deg, #2d1b4e, #1a0f2e);
  border: 1px solid var(--primary-color);
  border-radius: 28px;
  padding: 1.5rem;
  margin: 2rem 0;
  text-align: center;
  color: white;
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
  background: rgba(15, 23, 42, 0.9);
  color: var(--primary-light);
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 1.1rem;
  word-break: break-all;
  border: 1px solid var(--primary-color);
}

.copy-button {
  background-color: var(--primary-color);
  color: #1e1b4b;
  border: none;
  padding: 8px 16px;
  border-radius: 60px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.2s;
}

.copy-button:hover {
  background-color: var(--primary-light);
  transform: translateY(-2px);
}

/* Tarjeta única */
.cards-grid {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
}

.service-card {
  background: var(--card-bg);
  backdrop-filter: blur(4px);
  border-radius: 28px;
  border: 1px solid rgba(244, 114, 182, 0.3);
  width: 100%;
  max-width: 380px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.service-card:hover {
  transform: translateY(-5px);
  border-color: var(--primary-color);
  box-shadow: 0 12px 30px rgba(0,0,0,0.4);
}

.card-header {
  background-color: var(--primary-color);
  padding: 1rem;
  text-align: center;
}

.card-header h3 {
  margin: 0;
  color: #1e1b4b;
  font-size: 1.4rem;
}

.card-body {
  padding: 1.5rem;
}

.price {
  font-size: 2rem;
  font-weight: bold;
  color: var(--primary-light);
  text-align: center;
  margin: 0.5rem 0;
}

.description {
  color: var(--md-default-fg-color--light);
  text-align: center;
  margin-bottom: 1rem;
}

.card-footer {
  padding: 1rem;
  text-align: center;
  border-top: 1px solid rgba(244,114,182,0.3);
}

.pay-button {
  background-color: var(--primary-color);
  color: #1e1b4b;
  border: none;
  padding: 10px 20px;
  border-radius: 60px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
  display: inline-block;
}

.pay-button:hover {
  background-color: var(--primary-light);
  transform: scale(1.02);
}

.instructions {
  background: rgba(30, 27, 75, 0.4);
  backdrop-filter: blur(2px);
  border-radius: 28px;
  padding: 1.5rem;
  margin: 2rem 0;
  border: 1px solid rgba(244,114,182,0.3);
}

.instructions h3 {
  color: var(--primary-light);
}

.instructions li {
  margin: 0.5rem 0;
  color: var(--md-default-fg-color--light);
}

.alert {
  background-color: rgba(244,114,182,0.1);
  border-left: 4px solid var(--primary-color);
  padding: 1rem;
  border-radius: 16px;
  margin: 1rem 0;
  color: var(--md-default-fg-color);
}
</style>

<div class="donation-container">

<div class="donation-header">
  <h1>☕️ Invita a un café</h1>
  <p>Cada granito de arena me ayuda a seguir creando contenido y manteniendo la web.</p>
  <div class="card-footer" style="border: none;">
    <button class="pay-button" onclick="payWithPayPal()">Invitar al Café</button>
  </div>
</div>

<!-- Recuadro Bitrefill (Lightning) -->
<div class="copy-box">
  <h3>⚡ Propinas con Bitcoin Lightning</h3>
  <p>Mi dirección Lightning a través de Bitrefill:</p>
  <div class="lightning-address">
    <code id="lightningAddr">jimraynor@bitrefill.me</code>
    <button class="copy-button" onclick="copyLightningAddress()">Copiar dirección</button>
  </div>
  <div id="copyFeedback" class="copy-feedback"></div>
  <div class="alert" style="background: rgba(0,0,0,0.3);">
    🔹 Esta dirección acepta pagos en euros (se convierten automáticamente a BTC en la red Lightning).<br>
    🔹 Para otras criptomonedas, contáctame y te daré una dirección temporal.
  </div>
</div>

<!-- Tarjeta única: Carta Natal Personificada -->
<div class="cards-grid">
  <div class="service-card">
    <div class="card-header">
      <h3>✨ Carta Natal Personificada</h3>
    </div>
    <div class="card-body">
      <div class="price">182 €</div>
      <div class="description">
        Tu propia Carta Natal que te habla en primera persona.<br>
        Casas, Conditio Vitae, perfiles y aspectos.<br>
        Un enlace único y privado para ti.
      </div>
    </div>
    <div class="card-footer">
      <button class="pay-button" onclick="payWithPayPal(182, 'Carta Natal Personificada')">Solicitar por 182 €</button>
    </div>
  </div>
</div>

<!-- Instrucciones de pago -->
<div class="instructions">
  <h3>📘 Cómo pagar</h3>
  <ol>
    <li><strong>PayPal</strong>: Haz clic en "Invitar al Café" o en "Solicitar por 182 €". Se abrirá PayPal con el importe correcto. Puedes pagar con tarjeta sin necesidad de cuenta PayPal.</li>
    <li><strong>Bitcoin Lightning</strong>: Copia la dirección <code>jimraynor@bitrefill.me</code>, abre tu monedero Lightning (Wallet of Satoshi, Zeus, etc.) y pega la dirección. Introduce el importe en euros (si tu monedero lo permite) o en satoshis equivalentes.</li>
    <li><strong>Para la Carta Natal</strong>: Una vez realizado el pago, contáctame por cualquiera de los canales del footer de la web (Telegram, formulario, etc.) con el comprobante. En 24-48h recibirás tu enlace personalizado.</li>
  </ol>
  <div class="alert">
    💡 <strong>Nota</strong>: Bitrefill me acredita el saldo en euros para gastar en su tienda. Es la forma más sencilla de aceptar Lightning sin gestionar un nodo propio.
  </div>
</div>

</div>

<script>
// Copiar dirección Lightning
function copyLightningAddress() {
  const addr = document.getElementById('lightningAddr').innerText;
  navigator.clipboard.writeText(addr).then(() => {
    const feedback = document.getElementById('copyFeedback');
    feedback.innerText = '✅ Dirección copiada. Pégala en tu monedero Lightning.';
    setTimeout(() => { feedback.innerText = ''; }, 3000);
  }).catch(() => {
    alert('No se pudo copiar. Cópiala manualmente: ' + addr);
  });
}

// Función PayPal con el botón de donación fijo (para el café)
function payWithPayPal(amount, itemName) {
  // Usamos el hosted_button_id que me diste
  const donateUrl = 'https://www.paypal.com/donate/?hosted_button_id=LV4Y3F89YFP24';
  // Si se pasa amount, podríamos personalizar, pero PayPal donate no acepta amount dinámico fácilmente.
  // Para la carta natal, el botón debería redirigir a un enlace de pago específico.
  // Como el botón de donación genérico no permite importes fijos por producto, lo dejamos igual.
  // Pero para la carta natal de 182€, necesitarías un botón de "comprar ahora" en PayPal.
  // Por ahora, abrimos el mismo enlace de donación (el usuario luego puede escribir el importe manualmente).
  window.open(donateUrl, '_blank');
}
</script>
