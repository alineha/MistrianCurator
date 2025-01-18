<script lang="ts">
  import { onMount } from "svelte";
  import { Circle } from "svelte-loading-spinners";
  import type { Writable } from "svelte/store";
  import { writable, get } from "svelte/store";
  import { getBaseUrl } from "$lib/utils";
  import GameLogo from "../components/GameLogo/+GameLogo.svelte";

  function swapDisplay(percTextId: string, circleDivId: string) {
    var txt = document.getElementById(percTextId);
    var div = document.getElementById(circleDivId);
    if (txt && div) {
      txt.style.display = "block";
      div.style.display = "none";
    }
  }

  function swapDisplayInverted(percTextId: string, circleDivId: string) {
    var txt = document.getElementById(percTextId);
    var div = document.getElementById(circleDivId);
    if (txt && div) {
      txt.style.display = "none";
      div.style.display = "block";
    }
  }

  let categories = ["archeology", "fish", "flora", "insects"];
  var categoriesPercentages: { [id: string]: Number } = {};
  categories.forEach((category) => {
    categoriesPercentages[category] = -1;
  });
  let files: FileList | null = null;
  let dataFile = null;

  async function getSetPercentage(category: string, museumInfo: string) {
    const response = await fetch(
      `${getBaseUrl()}/wing/percentage?wing=${category}`,
      {
        method: "POST",
        body: JSON.stringify(museumInfo),
      },
    );

    if (response.ok) {
      const data = await response.json();
      categoriesPercentages[category] = parseFloat(data) * 100;
      swapDisplay(`${category}perc`, `${category}circle`);
      return data; // json
    }

    return {}; // empty json
  }

  let museuminfo;

  const storedValue =
    typeof window !== "undefined" ? localStorage.getItem("museum") : null;
  const store = writable(storedValue ? JSON.parse(storedValue) : null);
  let museum = $store;

  store.subscribe((value) => {
    if (value !== null) {
      localStorage.setItem("museum", JSON.stringify(value));
    }
  });

  onMount(async () => {
    if (museum != null) {
      await Promise.all(
        categories.map((category) => getSetPercentage(category, museum)),
      );
    } else {
      categories.forEach((category) => {
        categoriesPercentages[category] = 0;
        swapDisplay(`${category}perc`, `${category}circle`);
      });
    }
  });

  async function upload() {
    if (!files || files.length === 0) {
      return;
    }
    const formData = new FormData();
    formData.append("gamedata", files[0]);

    const response = await fetch(`${getBaseUrl()}/import`, {
      method: "POST",
      body: formData,
    });
    museuminfo = await response.json();
    localStorage.setItem("museum", JSON.stringify(museuminfo));

    await getSetPercentage(categories[0], museuminfo);
    await getSetPercentage(categories[1], museuminfo);
    await getSetPercentage(categories[2], museuminfo);
    await getSetPercentage(categories[3], museuminfo);
  }

  async function clear() {
    localStorage.clear();

    swapDisplayInverted(`${categories[0]}perc`, `${categories[0]}circle`);
    swapDisplayInverted(`${categories[1]}perc`, `${categories[1]}circle`);
    swapDisplayInverted(`${categories[2]}perc`, `${categories[2]}circle`);
    swapDisplayInverted(`${categories[3]}perc`, `${categories[3]}circle`);
  }
</script>

<main>
  <GameLogo />
  <center>
    <table class="museum">
      <tbody>
        <tr>
          <td>
            <a href="/wing?which=archeology">
              <img
                src='/archeology.webp'
                class="logo archeo"
                alt="Archeology Wing"
              />
            </a>
            <div class="container_row">
              <h2 id="archeologyperc" class="wing" style="display:none">
                {categoriesPercentages["archeology"]}%
              </h2>
              <div
                class="wingLayer"
                id="archeologycircle"
                style="display:block"
              >
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
          <td>
            <a href="/wing?which=fish">
              <img src='/fish.webp' class="logo fish" alt="Fish Wing" />
            </a>
            <div class="container_row">
              <h2 id="fishperc" class="wing" style="display:none">
                {categoriesPercentages["fish"]}%
              </h2>
              <div class="wingLayer" id="fishcircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
        </tr>
        <tr>
          <td>
            <a href="/wing?which=flora">
              <img src='/flora.webp' class="logo flora" alt="Flora Wing" />
            </a>
            <div class="container_row">
              <h2 id="floraperc" class="wing" style="display:none">
                {categoriesPercentages["flora"]}%
              </h2>
              <div class="wingLayer" id="floracircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
          <td>
            <a href="/wing?which=insects">
              <img src='/insects.webp' class="logo insects" alt="Insects Wing" />
            </a>
            <div class="container_row">
              <h2 id="insectsperc" class="wing" style="display:none">
                {categoriesPercentages["insects"]}%
              </h2>
              <div class="wingLayer" id="insectscircle" style="display:block">
                <Circle size="30" color="#FFFFFF" unit="px" duration="1s" />
              </div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <h2>Submit your <a href="/gamedata">gamedata</a> file below to start:</h2>
    <input id="fileUpload" type="file" bind:files />
    {#if dataFile && files && files[0]}
      <p>
        {files[0].name}
      </p>
    {/if}
    <button onclick={upload}>Submit</button>
    <div style="padding-top: 1em">
      <button onclick={clear}>Clear data</button>
    </div>
  </center>
</main>

<style>
  @import "./+page.css";
</style>
