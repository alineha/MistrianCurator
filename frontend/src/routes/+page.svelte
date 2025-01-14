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
  
    let archpercentage = $state(11);
  
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
        }
        else
        {
          archpercentage = -1
        }
    });
  
    let insectspercentage = $state(11);
  
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
        }
        else
        {
          insectspercentage = -1
        }
    });
    let fishpercentage = $state(11);
  
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
        }
        else
        {
          fishpercentage = -1
        }
    });
    let florapercentage = $state(11);
  
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
        }
        else
        {
          florapercentage = -1
        }
    });
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
            <h2 class="wing">{archpercentage}%</h2>
          </td>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={fishLogo} class="logo fish" alt="Svelte Logo" />
            </a>
            <h2 class="wing">{fishpercentage}%</h2>
          </td>
        </tr>
        <tr>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={floraLogo} class="logo flora" alt="Svelte Logo" />
            </a>
            <h2 class="wing">{florapercentage}%</h2>
          </td>
          <td>
            <a href="https://svelte.dev" target="_blank" rel="noreferrer">
              <img src={insectsLogo} class="logo insects" alt="Svelte Logo" />
            </a>
            <h2 class="wing">{insectspercentage}%</h2>
          </td>
        </tr>
      </tbody>
      </table>
    </center>
  </main>
  