<style>
  @import './+page.css';
</style>

<script lang="ts">
    import { onMount } from 'svelte';
    import archeologyLogo from '../../static/archeology.webp'
    import fishLogo from '../../static/fish.webp'
    import floraLogo from '../../static/flora.webp'
    import insectsLogo from '../../static/insects.webp'
    import borderTitle from '../../static/titleborder.png'
    import {Circle} from 'svelte-loading-spinners'; 
    import type { Writable } from 'svelte/store';
    import { writable, get } from 'svelte/store'

    
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
    let files: FileList | null = null;
    let dataFile = null;

    async function getSetPercentage(category: string, museumInfo: string) {
      const response = await fetch(
        `http://127.0.0.1:8000/wing/percentage?wing=${category}`,
        {
            method: 'POST',
            body: JSON.stringify(museumInfo)
        }
      );
      
      if (response.ok) {
        const data = await response.json();
        categoriesPercentages[category] = parseFloat(data)*100;
        swapDisplay(`${category}perc`, `${category}circle`);
        return data; // json
      }  

      return {}; // empty json
    }

    let museuminfo;
    
    const storedValue = typeof window !== 'undefined' ? localStorage.getItem('museuminfo2') : null;
    const store = writable(storedValue ? JSON.parse(storedValue) : null);
    
    store.subscribe((value) => {
      if (value !== null) {
        localStorage.setItem("museuminfo2", JSON.stringify(value));
      }
    });
    
    export const museuminfo2 = $store;

    onMount(async () => {
      if (museuminfo2 != null){
      await getSetPercentage(categories[0], museuminfo2);
      await getSetPercentage(categories[1], museuminfo2);
      await getSetPercentage(categories[2], museuminfo2);
      await getSetPercentage(categories[3], museuminfo2);
    }
	  });
  
  async function upload() {
        const formData = new FormData();
        formData.append('gamedata', files[0]);
        
        const response = await fetch('http://localhost:8000/import', {
            method: 'POST',
            body: formData
        });
        museuminfo = await response.json();

        await getSetPercentage(categories[0], museuminfo);
        await getSetPercentage(categories[1], museuminfo);
        await getSetPercentage(categories[2], museuminfo);
        await getSetPercentage(categories[3], museuminfo);
      };

      
    
  </script>
  
  <main>
      <center><div class="title">
        <img class="leftBorder" src={borderTitle} alt="Border Left">
        <a href="/"><square class="title">Mistrian Curator</square></a>
        <img class="rightBorder" src={borderTitle} alt="Border Left">
      </div></center>
  <center>
    <table class="museum">
      <tbody>
        <tr>
          <td>
            <a href="/archeology">
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
            <a href="/fish">
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
            <a href="/flora">
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
            <a href="/insects">
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
      <h2>Submit your <a href="/gamedata">gamedata</a> file below to start:</h2>
      <input id="fileUpload" type="file" bind:files>
      {#if dataFile && files[0]}
          <p>
              {files[0].name}
          </p>
      {/if}
      <button onclick={upload}>Submit</button>
    </center>
  </main>
  