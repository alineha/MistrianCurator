<script lang="ts">
    import {
        categoriesPercentages,
        getSetPercentage,
        getBundleItems,
        getBundles,
    } from "$lib/utils";
    import { onMount } from "svelte";
    import { get, writable } from "svelte/store";
    import { page } from "$app/state";
    import { browser } from "$app/environment";
    import GameLogo from "../../components/GameLogo/+GameLogo.svelte";

    export let bundles: string[] = [];
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
            getSetPercentage(currCat, JSON.stringify(itemsCheckboxString));
        }
    }

    $: updateMuseumInfo(itemsCheckbox), itemsCheckbox;
    $: console.log(categoriesPercentages), categoriesPercentages;

    let isDataLoaded = false;
    onMount(async () => {
        store.subscribe(updatePercentage);

        function updatePercentage() {
            console.log("update");
            let museuminfo = localStorage.getItem("museum");
            if (museuminfo != null) {
                getSetPercentage(currCat, museuminfo);
            }
        }

        bundles = await getBundles(currCat);
        const bundlesWithItems = (
            await Promise.all(
                bundles.map((bundle) => getBundleItems(currCat, bundle)),
            )
        ).map((items, index) => ({
            id: bundles[index],
            items,
        }));
        for (var bundle of bundlesWithItems) {
            items[bundle.id] = bundle.items;
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
    <GameLogo />

    {#if isDataLoaded}
        <center
            ><h1>
                {currCat.toUpperCase()}: {Math.round(
                    $categoriesPercentages[currCat],
                )}% COMPLETE
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
                                        class={`item-icon ${itemsCheckbox[item.toLowerCase()] ? "" : "grayscale"}`}
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
