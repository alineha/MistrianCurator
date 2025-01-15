<style>
  @import './+page.css';
</style>

<script lang="ts">
    import archeologyLogo from '../../static/archeology.webp'
    import fishLogo from '../../static/fish.webp'
    import floraLogo from '../../static/flora.webp'
    import insectsLogo from '../../static/insects.webp'
    import borderTitle from '../../static/titleborder.png'
    import {Circle} from 'svelte-loading-spinners'; 
    
    function swapDisplay(percTextId: string, circleDivId: string) {
      var txt = document.getElementById(percTextId);
      var div = document.getElementById(circleDivId);
      if (txt && div)
      {
        txt.style.display = 'block';
        div.style.display = 'none';
      }
    };

    let categories = ['archeology', 'fish', 'flora', 'insects'];
    var categoriesPercentages: { [id: string]: Number; } = {};
    categories.forEach((category) => {
      categoriesPercentages[category] = -1;
    });
    let files;
    let dataFile = null;

    async function getSetPercentage(category: string, museumInfo: string) {
      const response = await fetch(
        `http://127.0.0.1:8000/wing/percentage?wing=${category}`,
        {
            method: 'POST',
            body: JSON.stringify(museumInfo)
        }
      );

      console.log(category)
      
      if (response.ok) {
        const data = await response.json();
        categoriesPercentages[category] = parseFloat(data)*100;
        swapDisplay(`${category}perc`, `${category}circle`);
        return data; // json
      }  

      return {}; // empty json
    }

    async function upload() {
        const formData = new FormData();
        formData.append('gamedata', files[0]);
        
        const response = await fetch('http://localhost:8000/import', {
            method: 'POST',
            body: formData
        });
        let museuminfo = await response.json();
  

        await getSetPercentage(categories[0], museuminfo);
        await getSetPercentage(categories[1], museuminfo);
        await getSetPercentage(categories[2], museuminfo);
        await getSetPercentage(categories[3], museuminfo);
      };

      
    
  </script>
  
  <main>
      <center><div class="title">
        <img class="leftBorder" src={borderTitle} alt="Border Left">
        <square class="title">Mistrian Curator</square>
        <img class="rightBorder" src={borderTitle} alt="Border Left">
      </div></center>
  <center>
    <table class="museum">
      <tbody>
        <tr>
          <td>
            <a href="https://vite.dev" target="_blank" rel="noreferrer">
              <img src={archeologyLogo} class="logo archeo" alt="Vite Logo" />
            </a>
            <div class="container_row">
              <h2 id="archeologyperc" class="wing" style="display:none">{categoriesPercentages['archeology']}%</h2>
              <div class="wingLayer" id="archeologycircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={fishLogo} class="logo fish" alt="Svelte Logo" />
            </a>
            <div class="container_row">
              <h2 id="fishperc" class="wing" style="display:none">{categoriesPercentages['fish']}%</h2>
              <div class="wingLayer" id="fishcircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
        </tr>
        <tr>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={floraLogo} class="logo flora" alt="Svelte Logo" />
            </a>
            <div class="container_row">
              <h2 id="floraperc" class="wing" style="display:none">{categoriesPercentages['flora']}%</h2>
              <div class="wingLayer" id="floracircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={insectsLogo} class="logo insects" alt="Svelte Logo" />
            </a>
            <div class="container_row">
              <h2 id="insectsperc" class="wing" style="display:none">{categoriesPercentages['insects']}%</h2>
              <div class="wingLayer" id="insectscircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
        </tr>
      </tbody>
      </table>
      <input id="fileUpload" type="file" bind:files>
      {#if dataFile && files[0]}
          <p>
              {files[0].name}
          </p>
      {/if}
      <button onclick={upload}>Submit</button>
    </center>
  </main>
  