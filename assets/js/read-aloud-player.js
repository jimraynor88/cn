// docs/assets/js/read-aloud-player.js

class ReadAloudPlayer {
  constructor(container) {
    this.container = container;
    this.synth = window.speechSynthesis;
    this.useResponsiveVoice = false;
    this.utterance = null;
    this.playing = false;
    this.paused = false;
    this.textChunks = [];
    this.currentChunkIndex = 0;
    this.rate = 1;
    this.totalChunks = 0;
    this.voices = [];
    this.voicesReady = false;
    this.currentVoice = null;
    this.responsiveVoiceName = 'Spanish Latin American Male'; // Voz por defecto

    this.buildUI();
    this.loadVoices();
    this.loadText();
  }

  buildUI() {
    this.container.innerHTML = `
      <div class="read-aloud-player">
        <div class="player-bar">
          <button class="play-pause-btn" title="Reproducir / Pausar">
            <svg class="icon-play" viewBox="0 0 24 24" width="20" height="20">
              <path d="M8 5v14l11-7z" fill="currentColor"/>
            </svg>
            <svg class="icon-pause" viewBox="0 0 24 24" width="20" height="20" style="display:none;">
              <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" fill="currentColor"/>
            </svg>
          </button>
          <button class="stop-btn" title="Detener">
            <svg viewBox="0 0 24 24" width="20" height="20">
              <path d="M6 6h12v12H6z" fill="currentColor"/>
            </svg>
          </button>
          <div class="progress-bar">
            <div class="progress-fill" style="width:0%"></div>
          </div>
          <span class="time-remaining">--:--</span>
          <select class="rate-select" title="Velocidad">
            <option value="0.56">0.56x</option>
            <option value="0.83">0.83x</option>
            <option value="1" selected>1x</option>
            <option value="1.1">1.1x</option>
            <option value="1.19">1.19x</option>
            <option value="1.28">1.28x</option>
            <option value="1.55">1.55x</option>
            <option value="1.82">1.82x</option>
            <option value="2.18">2.18x</option>
            <option value="2.81">2.81x</option>
          </select>
          <select class="voice-select" title="Voz"></select>
        </div>
        <div class="current-chunk-display" style="display:none;">
          <p class="current-chunk-text"></p>
        </div>
      </div>
    `;

    this.playPauseBtn = this.container.querySelector('.play-pause-btn');
    this.iconPlay = this.container.querySelector('.icon-play');
    this.iconPause = this.container.querySelector('.icon-pause');
    this.stopBtn = this.container.querySelector('.stop-btn');
    this.rateSelect = this.container.querySelector('.rate-select');
    this.voiceSelect = this.container.querySelector('.voice-select');
    this.progressFill = this.container.querySelector('.progress-fill');
    this.timeRemaining = this.container.querySelector('.time-remaining');
    this.chunkDisplay = this.container.querySelector('.current-chunk-display');
    this.chunkText = this.container.querySelector('.current-chunk-text');

    this.playPauseBtn.addEventListener('click', () => this.togglePlayPause());
    this.stopBtn.addEventListener('click', () => this.stop());
    this.rateSelect.addEventListener('change', (e) => {
      this.rate = parseFloat(e.target.value);
    });
    this.voiceSelect.addEventListener('change', (e) => {
      const value = e.target.value;
      if (this.useResponsiveVoice) {
        this.responsiveVoiceName = value;
        if (this.playing) {
          this.stop();
          this.play();
        }
      } else {
        const selected = this.voices.find(v => v.name === value);
        if (selected) {
          this.currentVoice = selected;
          if (this.playing) {
            this.stop();
            this.play();
          }
        }
      }
    });
  }

  async loadVoices() {
    const load = () => {
      this.voices = this.synth.getVoices();
      if (this.voices.length > 0) this.voicesReady = true;
    };
    load();
    if (!this.voicesReady && window.speechSynthesis.onvoiceschanged !== undefined) {
      await new Promise((resolve) => {
        const timeout = setTimeout(() => {
          window.speechSynthesis.onvoiceschanged = null;
          resolve();
        }, 2000);
        window.speechSynthesis.onvoiceschanged = () => {
          clearTimeout(timeout);
          load();
          resolve();
        };
      });
    }
    if (!this.voicesReady) load();
    this.populateVoiceSelector();
  }

  async populateVoiceSelector() {
    // Si estamos usando ResponsiveVoice, obtenemos la lista de voces de su API
    if (this.useResponsiveVoice && window.responsiveVoice) {
      let rvVoices = window.responsiveVoice.getVoices();
      if (!rvVoices || rvVoices.length === 0) {
        // Puede que la lista aún no esté disponible, mostramos un placeholder
        this.voiceSelect.innerHTML = '<option value="">Cargando voces...</option>';
        // Esperamos un poco por si se cargan de forma asíncrona
        await new Promise(resolve => setTimeout(resolve, 500));
        rvVoices = window.responsiveVoice.getVoices();
      }
      if (rvVoices && rvVoices.length > 0) {
        this.voiceSelect.innerHTML = '';
        rvVoices.forEach(voice => {
          const option = document.createElement('option');
          option.value = voice.name;
          option.textContent = voice.name;
          this.voiceSelect.appendChild(option);
        });
        // Seleccionamos Spanish Female si existe, si no la primera
        const defaultVoice = rvVoices.find(v => v.name === 'Spanish Latin American Male') || rvVoices[0];
        this.voiceSelect.value = defaultVoice.name;
        this.responsiveVoiceName = defaultVoice.name;
      } else {
        // Fallback a las opciones fijas si la API no responde
        this.voiceSelect.innerHTML = `
          <option value="Spanish Female">Voz femenina (es-es)</option>
          <option value="Spanish Male">Voz masculina (es-es)</option>
          <option value="Spanish Latin American Female">Voz femenina (es-la)</option>
          <option value="Spanish Latin American Male">Voz masculina (es-la)</option>
        `;
      }
      return;
    }

    // Voces nativas del sistema
    const spanishVoices = this.voices.filter(v => v.lang.startsWith('es'));
    this.voiceSelect.innerHTML = '';

    if (spanishVoices.length > 0 && !this.useResponsiveVoice) {
      spanishVoices.forEach(voice => {
        const option = document.createElement('option');
        option.value = voice.name;
        option.textContent = voice.name + (voice.default ? ' (predeterminada)' : '');
        this.voiceSelect.appendChild(option);
      });
      this.currentVoice = spanishVoices[0];
    } else {
      const voices = [
        { name: 'Spanish Female', label: 'Voz femenina (español)' },
        { name: 'Spanish Male', label: 'Voz masculina (español)' }
      ];
      voices.forEach(v => {
        const option = document.createElement('option');
        option.value = v.name;
        option.textContent = v.label;
        this.voiceSelect.appendChild(option);
      });
      this.voiceSelect.value = this.responsiveVoiceName;
      this.currentVoice = null;
    }
  }

  loadText() {
    const article = document.querySelector('article') || document.body;
    const clone = article.cloneNode(true);
    const playerClone = clone.querySelector('#read-aloud-root');
    if (playerClone) playerClone.remove();
    const fullText = clone.innerText.trim();
    this.textChunks = fullText.split(/\n\s*\n/).filter(chunk => chunk.trim().length > 0);
    this.totalChunks = this.textChunks.length;
  }

  togglePlayPause() {
    if (this.playing && !this.paused) this.pause();
    else if (this.paused) this.resume();
    else this.play();
  }

  async play() {
    if (this.textChunks.length === 0) {
      this.showMessage('No hay texto para leer.');
      return;
    }

    if (!this.useResponsiveVoice) {
      if (!this.synth) {
        this.switchToResponsiveVoice();
      } else {
        if (!this.voicesReady) {
          this.chunkDisplay.style.display = 'block';
          this.chunkText.textContent = 'Verificando voces del sistema...';
          await this.loadVoices();
          if (!this.voicesReady) {
            this.switchToResponsiveVoice();
          }
        }
        if (!this.useResponsiveVoice) {
          this.startNativePlayback();
          return;
        }
      }
    }

    if (this.useResponsiveVoice) {
      this.startResponsivePlayback();
    }
  }

  switchToResponsiveVoice() {
    if (!this.useResponsiveVoice) {
      console.log('Cambiando a ResponsiveVoice (no hay voces nativas)');
      this.useResponsiveVoice = true;
      this.populateVoiceSelector(); // Ahora cargará todas las voces de RV
    }
  }

  startNativePlayback() {
    this.playing = true;
    this.paused = false;
    this.setPlayIcon('pause');
    this.chunkDisplay.style.display = 'block';
    this.speakChunkNative(this.currentChunkIndex);
  }

  speakChunkNative(index) {
    if (index >= this.textChunks.length) {
      this.stop();
      return;
    }
    this.currentChunkIndex = index;
    const text = this.textChunks[index];
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-ES';
    utterance.rate = this.rate;
    if (this.currentVoice) {
      utterance.voice = this.currentVoice;
    } else if (this.voices.length > 0) {
      const spanishVoice = this.voices.find(v => v.lang.startsWith('es'));
      if (spanishVoice) utterance.voice = spanishVoice;
    }

    this.updateProgress(index);
    this.chunkText.textContent = text;

    utterance.onstart = () => { this.chunkDisplay.style.display = 'block'; };
    utterance.onend = () => this.speakChunkNative(index + 1);
    utterance.onerror = (e) => {
      console.warn('Error nativo:', e.error);
      if (e.error === 'canceled' || e.error === 'interrupted') {
        this.stop();
      } else {
        this.switchToResponsiveVoice();
        this.startResponsivePlayback();
      }
    };
    this.utterance = utterance;
    try {
      this.synth.speak(utterance);
    } catch (err) {
      console.error('Error al hablar:', err);
      this.switchToResponsiveVoice();
      this.startResponsivePlayback();
    }
  }

  startResponsivePlayback() {
    if (!window.responsiveVoice) {
      this.showMessage('El servicio de voz no está disponible.');
      return;
    }
    this.playing = true;
    this.paused = false;
    this.setPlayIcon('pause');
    this.chunkDisplay.style.display = 'block';
    const fullText = this.textChunks.join(' ');
    this.chunkText.textContent = fullText;
    this.updateProgress(0);

    const self = this;
    window.responsiveVoice.speak(fullText, this.responsiveVoiceName, {
      rate: this.rate,
      onstart: () => {
        self.chunkDisplay.style.display = 'block';
      },
      onend: () => {
        self.stop();
      },
      onerror: (e) => {
        console.error('Error ResponsiveVoice:', e);
        self.showMessage('Error en la reproducción de voz.');
        self.stop();
      }
    });
    this.simulateProgress(fullText);
  }

  simulateProgress(text) {
    const words = text.split(/\s+/).length;
    const durationSec = (words / 150) / this.rate;
    const start = Date.now();
    const self = this;
    const interval = setInterval(() => {
      if (!self.playing) {
        clearInterval(interval);
        return;
      }
      const elapsed = (Date.now() - start) / 1000;
      const progress = Math.min((elapsed / durationSec) * 100, 100);
      self.progressFill.style.width = progress + '%';
      const remaining = durationSec - elapsed;
      if (remaining > 0) {
        const mins = Math.floor(remaining / 60);
        const secs = Math.floor(remaining % 60);
        self.timeRemaining.textContent = `${mins}:${secs.toString().padStart(2, '0')}`;
      } else {
        self.timeRemaining.textContent = '0:00';
        clearInterval(interval);
      }
    }, 200);
  }

  pause() {
    if (this.useResponsiveVoice) {
      window.responsiveVoice.pause();
    } else {
      this.synth.pause();
    }
    this.paused = true;
    this.setPlayIcon('play');
  }

  resume() {
    if (this.useResponsiveVoice) {
      window.responsiveVoice.resume();
    } else {
      this.synth.resume();
    }
    this.paused = false;
    this.setPlayIcon('pause');
  }

  stop() {
    if (this.useResponsiveVoice) {
      window.responsiveVoice.cancel();
    } else {
      this.synth.cancel();
    }
    this.playing = false;
    this.paused = false;
    this.currentChunkIndex = 0;
    this.progressFill.style.width = '0%';
    this.timeRemaining.textContent = '--:--';
    this.chunkDisplay.style.display = 'none';
    this.chunkText.textContent = '';
    this.setPlayIcon('play');
  }

  setPlayIcon(state) {
    if (state === 'play') {
      this.iconPlay.style.display = '';
      this.iconPause.style.display = 'none';
    } else {
      this.iconPlay.style.display = 'none';
      this.iconPause.style.display = '';
    }
  }

  showMessage(msg) {
    this.chunkDisplay.style.display = 'block';
    this.chunkText.textContent = msg;
    setTimeout(() => {
      if (this.chunkText.textContent === msg) this.chunkDisplay.style.display = 'none';
    }, 4000);
  }

  updateProgress(index) {
    const progress = ((index + 1) / this.totalChunks) * 100;
    this.progressFill.style.width = progress + '%';
    const wordsRemaining = this.textChunks.slice(index).join(' ').split(/\s+/).length;
    const minutesRemaining = (wordsRemaining / 150) / this.rate;
    const mins = Math.floor(minutesRemaining);
    const secs = Math.floor((minutesRemaining - mins) * 60);
    this.timeRemaining.textContent = `${mins}:${secs.toString().padStart(2, '0')}`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const root = document.getElementById('read-aloud-root');
  if (root) new ReadAloudPlayer(root);
});
