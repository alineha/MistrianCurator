<script lang="ts">
  import archeologyLogo from './assets/archeology.webp'
  import fishLogo from './assets/fish.webp'
  import floraLogo from './assets/flora.webp'
  import insectsLogo from './assets/insects.webp'
  import borderTitle from './assets/titleborder.png'
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
    <div class="title">
      <img class="leftBorder" src={borderTitle} alt="Border Left">
      <square class="title">Mistrian Curator</square>
      <img class="rightBorder" src={borderTitle} alt="Border Left">
    </div>
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

<style>
  .logo {
    height: 10em;
    padding: 0em 2em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo.archeo:hover {
    filter: drop-shadow(0 0 1em #d0c3beaa);
  }
  .logo.fish:hover {
    filter: drop-shadow(0 0 1em #bac8dbaa);
  }
  .logo.flora:hover {
    filter: drop-shadow(0 0 1em #b6cdcfaa);
  }
  .logo.insects:hover {
    filter: drop-shadow(0 0 1em #d0bdd9aa);
  }
  table.museum {
  text-align: center;
  }
  table.museum td {
    padding: 0px 0px;
  }
  h2.wing {
    text-align: center;
    padding-bottom: 1em;
    margin-top: 0;
  }
  square.title {
    font-size: 3.2em;
    background-color: #d0c2c7;
    border-radius: 15px 15px 15px 15px;
    border: 3px outset #554751;
    color: #010101;
    text-shadow: 2px 2px 2px #b9a7a3;
    padding: .3em;
    padding-left: .5em;
    padding-right: .4em;
    }
  div.title{
    padding: 1.5em;
    margin-bottom: 1.5em;
  }
  img.rightBorder {
    transform: scalex(-100%) scale(130%);
    margin-left: -2px;
  }
  img.leftBorder {
    transform: scale(130%);
    margin-right: -2px;
  }
</style>
