import { createChannel, createClient } from 'nice-grpc-web';
import { Empty, RandomizerServiceDefinition } from './compiled_proto/randomizer';

export const main = async () => {
	const channel = createChannel('http://localhost:5001');
	const client = createClient(RandomizerServiceDefinition, channel);

	// 调用 GetRandomString 方法
	try {
		const randomStringResponse = await client.getRandomString(Empty.create());
		console.log('Random String:', randomStringResponse.value);
	} catch (error) {
		console.error('Error calling GetRandomString:', error);
	}

	// // 调用 GetRandomUUIDStream 方法
	// try {
	// 	const stream = client.getRandomUUIDStream(Empty.create());
	// 	for await (const response of stream) {
	// 		console.log('Random UUID:', response.uuid);
	// 	}
	// } catch (error) {
	// 	console.error('Error calling GetRandomUUIDStream:', error);
	// }

	// // 调用 GetArray 方法
	// try {
	// 	const arrayResponse = await client.getArray(Empty.create());
	// 	console.log('Array Response:', arrayResponse.row);
	// } catch (error) {
	// 	console.error('Error calling GetArray:', error);
	// }

	// 调用 GetArrayStream 方法
	// try {
	// 	const arrayStream = client.getArrayStream(Empty.create());
	// 	for await (const response of arrayStream) {
	// 		console.log('Array Stream Response:', response.row);
	// 	}
	// } catch (error) {
	// 	console.error('Error calling GetArrayStream:', error);
	// }
	// 调用GEtArray2D方法
	try {
		const array2DResponse = await client.get2DArray(Empty.create());
		console.log('Array 2D Response:', array2DResponse.matrix);
	} catch (error) {
		console.error('Error calling GetArray2D:', error);
	}
};
