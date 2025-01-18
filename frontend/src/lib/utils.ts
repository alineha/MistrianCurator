export let categories = ['archeology', 'fish', 'flora', 'insects'];
export let categoriesPercentages: { [id: string]: Number; } = {};
categories.forEach((category) => {
    categoriesPercentages[category] = 0;
});

export function getBaseUrl() {
    if (import.meta.env.MODE === 'development') {
        return 'http://localhost:8000';
    } else {
        return 'https://dominoisy.pythonanywhere.com';
    }
}

export async function getSetPercentage(category: string, museumInfo: string) {
    const response = await fetch(
        `${getBaseUrl()}/wing/percentage?wing=${category}`,
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

export async function getBundles(category: string) {
    const response = await fetch(
      `${getBaseUrl()}/wing/bundles?wing=${category}`,
      {
          method: 'GET'
      }
    );

    if (response.ok) {
      const data = await response.json();
      return data; // json
    }  

    return {}; // empty json
}

export async function getBundleItems(category: string, bundle: string) {
    const response = await fetch(
      `${getBaseUrl()}/wing/bundles/items?wing=${category}&bundle=${bundle}`,
      {
          method: 'GET'
      }
    );

    if (response.ok) {
      const data = await response.json();
      return data; // json
    }  

    return {}; // empty json
}