export async function getBundles(category: string) {
    const response = await fetch(
      `http://127.0.0.1:8000/wing/bundles?wing=${category}`,
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
      `http://127.0.0.1:8000/wing/bundles/items?wing=${category}&bundle=${bundle}`,
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