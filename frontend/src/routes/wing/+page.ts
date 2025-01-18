export const load = async ({ params, url }) => {
	const currCat = url.searchParams.get("which");
	if (currCat === null) {
		throw new Error("Param 'which' is required")
	}
}