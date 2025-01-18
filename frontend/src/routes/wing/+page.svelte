<style>
    @import './+page.css';
</style>

<script lang="ts">
    import borderTitle from '../../../static/titleborder.png'
    import {categoriesPercentages, getSetPercentage, getBundleItems, getBundles} from '$lib/utils';
    import {onMount} from 'svelte';    
    import { writable } from 'svelte/store';
    import { page } from '$app/state';

    let currCat = page.url.searchParams.get('which')    
    console.log(currCat)
    
    export let bundles: string[] = [];
    export let bundlesNumber: number = 0;
    export let items: { [id: string] : string[]; } = {};
    export let itemsCheckbox: { [id: string] : boolean; } = {};
    const storedValue = typeof window !== 'undefined' ? localStorage.getItem('museum') : null;
    const store = writable(storedValue ? JSON.parse(storedValue) : null);
    let museum = $store;
    
    store.subscribe(updatePercentage);
    
    function updatePercentage(){
        let museuminfo = localStorage.getItem("museum");
        if(museuminfo != null)
        {
            getSetPercentage(currCat, museuminfo);
        }
    }

    $: updateMuseumInfo(itemsCheckbox), itemsCheckbox;

    function updateMuseumInfo(itemsCheckbox : { [id: string]: boolean }){
        let museuminfo = localStorage.getItem("museum");
        if(museuminfo != null)
        {
            let itemsCheckboxString = JSON.parse(museuminfo);
            for (var item in itemsCheckbox){
                if (itemsCheckbox[item])
                {
                    itemsCheckboxString[item] = "YES";
                }
                else
                {
                    itemsCheckboxString[item] = "NO";
                }
            }
            localStorage.setItem("museum", JSON.stringify(itemsCheckboxString));
        }
    }
    
    let isDataLoaded = false;
    onMount(async () => {
		bundles = await getBundles(currCat);
        bundlesNumber = bundles.length-1;
        for (var bundle of bundles)
        {
            let itemsOfBundle = await getBundleItems(currCat, bundle);
            items[bundle] = itemsOfBundle;
        }
        let museuminfo = localStorage.getItem("museum");
        if(museuminfo != null)
        {
            let museumNotJson = JSON.parse(museuminfo);
    
            for (var bundle2 in items)
            {
                for (var item of items[bundle2]){
                    let itemLowercase = item.toLowerCase();
                    if (museumNotJson[itemLowercase] == "YES"){
                        itemsCheckbox[itemLowercase] = true;
                    }
                    else
                    {
                        itemsCheckbox[itemLowercase] = false;
                    }
                }
            }
        }
        else
        {
            localStorage.setItem("museum", "{}");
        }

        isDataLoaded = true;
	});

    
</script>

<main>
    <center><div class="title">
      <img class="leftBorder" src={borderTitle} alt="Border Left">
      <a href="/"><square class="title">Mistrian Curator</square></a>
      <img class="rightBorder" src={borderTitle} alt="Border Left">
    </div></center>
        
            {#if isDataLoaded}
            <center><h1>{currCat.toUpperCase()}: {categoriesPercentages[currCat]}% COMPLETE</h1></center>
        <div id="app" class="container">
                {#each bundles as bundle}
                <div>
                    <h1>{bundle}</h1>
                    {#if items[bundle]?.length > 0}
                    {#each items[bundle] as item}
                                <div>
                                    <label style="font-size:1.25em;">
                                        <input type="checkbox" bind:checked={itemsCheckbox[item.toLowerCase()]}>
                                            {#await import(`../../../static/items/${item}.webp`) then { default: src }}
                                                {#if itemsCheckbox[item.toLowerCase()]}
                                                    <img {src} style="height: 1.25em" alt="{item}"/>
                                                {:else}
                                                    <img {src} style="height: 1.25em; -webkit-filter: grayscale(100%) brightness(0); filter: grayscale(100%) brightness(0);" alt="{item}"/>
                                                {/if}
                                            {/await}{item}
                                    </label></div>
                            {/each}
                        {/if}
                    </div>
                {/each}
              </div>  
            {/if}
        
</main>