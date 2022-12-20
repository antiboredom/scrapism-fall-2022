class BioBlock extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.innerHTML = `
      <style>
          bio-block {
            width: 70%;
            line-height: 1.6;
            display: block;
            margin: 0 0 40px 0;
            word-wrap: break-word;
          }

          bio-block h3 {
            margin-bottom: 10px;
          }

          bio-block p {
            margin: 0px;
          }

          @media screen and (max-width: 500px) {
            bio-block {
              width: 100%;
            }
          }
      </style>

        <div class="bio-block">
          <a href="${this.getAttribute('link-to-project')}">
            <h3>${this.getAttribute('artist-name')}</h3>
          </a>
          <p>${this.getAttribute('artist-bio')}</p>
        </div>
      </a>
      `;
    }
  }
  
  customElements.define('bio-block', BioBlock);