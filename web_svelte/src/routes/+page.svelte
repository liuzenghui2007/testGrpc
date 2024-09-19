<script>
	import { onMount } from 'svelte';
	import { main } from '../client.js'; // Ensure the path to 'client.js' is correct

	onMount(async () => {
		try {
			const randomString = await main(); // Ensure `main` is an async function returning a value
			console.log('main test:', randomString);
		} catch (err) {
			console.error('main test error:', err); // Fixed typo from 'mian' to 'main'
		}
	});
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
