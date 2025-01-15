export const ssr = false;

import type { PageLoad } from './$types';

import Cookies from "cookies-ts"
 
const cookies = new Cookies()

export const load: PageLoad = ({ params }) => {
    console.log("batata");
	return {
		post: {
			title: "strawberry: "+ cookies.get("strawberry"),
			content: "cabbage: " + params.cabbage
		}
	};
};