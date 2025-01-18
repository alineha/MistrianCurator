<script lang="ts">
    import borderTitle from "../../../static/titleborder.png";
    import {
        categoriesPercentages,
        getSetPercentage,
        getBundleItems,
        getBundles,
    } from "$lib/utils";
    import { onMount } from "svelte";
    import { writable } from "svelte/store";
    import { page } from "$app/state";
    import { browser } from "$app/environment";

    export let bundles: string[] = [];
    export let bundlesNumber: number = 0;
    export let items: { [id: string]: string[] } = {};
    export let itemsCheckbox: { [id: string]: boolean } = {};
    const storedValue =
        typeof window !== "undefined" ? localStorage.getItem("museum") : null;
    const store = writable(storedValue ? JSON.parse(storedValue) : null);

    const currCat = page.url.searchParams.get("which")!;

    function updateMuseumInfo(itemsCheckbox: { [id: string]: boolean }) {
        if (!browser) return;
        let museuminfo = localStorage.getItem("museum");
        if (museuminfo != null) {
            let itemsCheckboxString = JSON.parse(museuminfo);
            for (var item in itemsCheckbox) {
                if (itemsCheckbox[item]) {
                    itemsCheckboxString[item] = "YES";
                } else {
                    itemsCheckboxString[item] = "NO";
                }
            }
            localStorage.setItem("museum", JSON.stringify(itemsCheckboxString));
        }
    }

    $: updateMuseumInfo(itemsCheckbox), itemsCheckbox;

    let isDataLoaded = false;
    onMount(async () => {
        store.subscribe(updatePercentage);

        function updatePercentage() {
            let museuminfo = localStorage.getItem("museum");
            if (museuminfo != null) {
                getSetPercentage(currCat, museuminfo);
            }
        }

        bundles = await getBundles(currCat);
        bundlesNumber = bundles.length - 1;
        for (var bundle of bundles) {
            let itemsOfBundle = await getBundleItems(currCat, bundle);
            items[bundle] = itemsOfBundle;
        }
        let museuminfo = localStorage.getItem("museum");
        if (museuminfo != null) {
            let museumNotJson = JSON.parse(museuminfo);

            for (var bundle2 in items) {
                for (var item of items[bundle2]) {
                    let itemLowercase = item.toLowerCase();
                    if (museumNotJson[itemLowercase] == "YES") {
                        itemsCheckbox[itemLowercase] = true;
                    } else {
                        itemsCheckbox[itemLowercase] = false;
                    }
                }
            }
        } else {
            localStorage.setItem("museum", "{}");
        }

        isDataLoaded = true;
    });
</script>

<main>
    <center
        ><div class="title">
            <img class="leftBorder" src={borderTitle} alt="Border Left" />
            <a href="/"><square class="title">Mistrian Curator</square></a>
            <img class="rightBorder" src={borderTitle} alt="Border Left" />
        </div></center
    >

    {#if isDataLoaded}
        <center
            ><h1>
                {currCat.toUpperCase()}: {categoriesPercentages[currCat]}%
                COMPLETE
            </h1></center
        >
        <div id="app" class="container">
            {#each bundles as bundle}
                <div>
                    <h1>{bundle}</h1>
                    {#if items[bundle]?.length > 0}
                        {#each items[bundle] as item}
                            <label style="font-size:1.25em;">
                                <div class="item">
                                    <input
                                        type="checkbox"
                                        bind:checked={itemsCheckbox[
                                            item.toLowerCase()
                                        ]}
                                    />
                                    <img
                                        src={`/items/${item}.webp`}
                                        alt={item}
                                        style="height: 1.25em; {itemsCheckbox[
                                            item.toLowerCase()
                                        ]
                                            ? ''
                                            : '-webkit-filter: grayscale(100%) brightness(0); filter: grayscale(100%) brightness(0);'}"
                                    />
                                    {item}
                                </div>
                            </label>
                        {/each}
                    {/if}
                </div>
            {/each}
        </div>
    {/if}
</main>

<style>
    @import "./+page.css";
</style>
