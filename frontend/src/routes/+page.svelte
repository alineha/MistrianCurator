<style>
  @import './+page.css';
</style>

<script lang="ts">
    import archeologyLogo from '../../static/archeology.webp'
    import fishLogo from '../../static/fish.webp'
    import floraLogo from '../../static/flora.webp'
    import insectsLogo from '../../static/insects.webp'
    import borderTitle from '../../static/titleborder.png'
    import {onMount} from 'svelte';
    import {Circle} from 'svelte-loading-spinners';

    let archpercentage = $state(-1);

    function swapDisplay(percTextId: string, circleDivId: string) {
      var txt = document.getElementById(percTextId);
      var div = document.getElementById(circleDivId);
      if (txt && div)
      {
        txt.style.display = 'block';
        div.style.display = 'none';
      }
    };

    onMount(async () => {
      const response = await fetch(
            'http://127.0.0.1:8000/wing/percentage?wing=archeology',
            {
                method: 'GET'
            }
        );
        if(response.ok)
        {
          const data = await response.json();
          archpercentage = parseFloat(data)*100;
          swapDisplay('archperc', 'archcircle');
        }
        else
        {
          archpercentage = -1
        }
    });
  
    let insectspercentage = $state(-1);
  
    onMount(async () => {
      const response = await fetch(
            'http://127.0.0.1:8000/wing/percentage?wing=insects',
            {
                method: 'GET'
            }
        );
        if(response.ok)
        {
          const data = await response.json();
          insectspercentage = parseFloat(data)*100;
          swapDisplay('insectsperc', 'insectscircle');
        }
        else
        {
          insectspercentage = -1
        }
    });
    let fishpercentage = $state(-1);
  
    onMount(async () => {
      const response = await fetch(
            'http://127.0.0.1:8000/wing/percentage?wing=fish',
            {
                method: 'GET'
            }
        );
        if(response.ok)
        {
          const data = await response.json();
          fishpercentage = parseFloat(data)*100;
          swapDisplay('fishperc', 'fishcircle');
        }
        else
        {
          fishpercentage = -1
        }
    });
    let florapercentage = $state(-1);
  
    onMount(async () => {
      const response = await fetch(
            'http://127.0.0.1:8000/wing/percentage?wing=flora',
            {
                method: 'GET'
            }
        );
        if(response.ok)
        {
          const data = await response.json();
          florapercentage = parseFloat(data)*100;
          swapDisplay('floraperc', 'floracircle');
        }
        else
        {
          florapercentage = -1
        }
    });

    let files = $state();
    let dataFile = null;

    function upload() {
        const formData = new FormData();
        formData.append('gamedata', files[0]);
        const upload = fetch('http://localhost:8000/import', {
            method: 'POST',
            body: formData,
        }).then((response) => { console.log(response.body);return response.json()}).then((result) => {
            console.log('Success:', result);
        })
                .catch((error) => {
                    console.error('Error:', error);
                });
    }
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
              <h2 id="archperc" class="wing" style="display:none">{archpercentage}%</h2>
              <div class="wingLayer" id="archcircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={fishLogo} class="logo fish" alt="Svelte Logo" />
            </a>
            <div class="container_row">
              <h2 id="fishperc" class="wing" style="display:none">{fishpercentage}%</h2>
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
              <h2 id="floraperc" class="wing" style="display:none">{florapercentage}%</h2>
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
              <h2 id="insectsperc" class="wing" style="display:none">{insectspercentage}%</h2>
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
  