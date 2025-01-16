<style>
    @import './+page.css';
</style>

<script lang="ts">
    import borderTitle from '../../../static/titleborder.png'
    import {getBundleItems, getBundles} from '$lib/utils';
    import {onMount} from 'svelte';
    import {museuminfo2} from '$lib/stores';
    
    
    let categories = ['archeology', 'fish', 'flora', 'insects'];
    var categoriesPercentages: { [id: string]: Number; } = {};
    categories.forEach((category) => {
        categoriesPercentages[category] = -1;
    });
    
    async function getSetPercentage(category: string, museumInfo: string) {
        const response = await fetch(
            `http://127.0.0.1:8000/wing/percentage?wing=${category}`,
            {
                method: 'POST',
                body: museumInfo
            }
        );
        
        if (response.ok) {
            const data = await response.json();
            categoriesPercentages[category] = parseFloat(data)*100;
            return data; // json
        }  
        
        return {}; // empty json
    }
    
    export let bundles: string[] = [];
    export let bundlesNumber: number = 0;
    export let items: { [id: string] : string[]; } = {};
    export let itemsCheckbox: { [id: string] : boolean; } = {};
    museuminfo2.subscribe(updateMuseumInfo);

    
    function updateMuseumInfo(){
        let museum = localStorage.getItem("museuminfo2");
        if(museum != null)
        {
            getSetPercentage('flora', museum);
        }
    }
    
    
    let isDataLoaded = false;
    onMount(async () => {
		bundles = await getBundles("flora");
        bundlesNumber = bundles.length-1;
        for (var bundle of bundles)
        {
            let itemsOfBundle = await getBundleItems("flora", bundle);
            items[bundle] = itemsOfBundle;
        }
        let museum = localStorage.getItem("museuminfo2");
        if(museum != null)
        {
            console.log("AAAAAA");
            let museumNotJson = JSON.parse(museum);
    
            for (var bundle2 in items)
            {
                for (var item of items[bundle2]){
                    let itemLowercase = item.toLowerCase();
                    if (museumNotJson[itemLowercase] == "YES"){
                        itemsCheckbox[itemLowercase] = true;
                        console.log(itemLowercase);
                    }
                    else
                    {
                        itemsCheckbox[itemLowercase] = false;
                        console.log(itemLowercase); 
                    }
                }
            }
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
        <center><h1>FLORA: {categoriesPercentages['flora']}% COMPLETE</h1></center>
        <div id="app" class="container">
            {#if isDataLoaded}
                {#each bundles as bundle}
                    <div>
                        <h1>{bundle}</h1>
                        {#if items[bundle]?.length > 0}
                            {#each items[bundle] as item}
                                <div class="item"><label><input type="checkbox" bind:checked={itemsCheckbox[item.toLowerCase()]}>{item}</label></div>
                            {/each}
                        {/if}
                    </div>
                {/each}
            {/if}
        </div> 
</main>