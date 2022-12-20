class ProjectCard extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.innerHTML = `
      <style>
        .project-card {
          padding: 20px;
          box-sizing: border-box;
          border: 1px dashed white;
          display: inline-block;
        }

        .project-card:hover {
          border: 1px dashed yellow;
        }

        h4 {
          margin: 0 0 7px 0;
        }

        p {
          margin: 0px;
        }

        img {
          padding-bottom: 10px;
        }

        span {
          display: block;
          font-size: 20px;
        }

        a {
          text-decoration: none;
        }

        .project-name {
          font-size: 28px;
        }

        .artist-name {
          font-size: 24px;
        }
      </style>

      <a href="${this.getAttribute('link-to-project')}">
        <div class="project-card">
            <img src="${this.getAttribute('thumbnail')}"/>
            <h4 class="project-name">
              ${this.getAttribute('project-name')}
            </h4  >
            <p class="artist-name">
              ${this.getAttribute('artist-name')}
            </p>
        </div>
      </a>
      `;
    }
  }
  
  customElements.define('project-card', ProjectCard);