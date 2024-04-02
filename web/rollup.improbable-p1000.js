// 编译 ES6 代码, rollup 插件2.78.0
import commonjs from '@rollup/plugin-commonjs';
import resolve from '@rollup/plugin-node-resolve';
import multiInput from 'rollup-plugin-multi-input';
import rimraf from 'rimraf';

// 删除上次生成的内容
rimraf.sync('client-es6/*');

export default {
	input: ['client/**/*.js'],
	output: {
		dir: './client/es6',
		format: 'esm',
		sourcemap: false
	},
	external: '@rollup/plugin-commonjs',
	plugins: [multiInput(), resolve(), commonjs()]
};
