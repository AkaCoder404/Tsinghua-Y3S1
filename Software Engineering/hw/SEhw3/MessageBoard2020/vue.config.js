module.exports = {
  publicPath: '/',
  outputDir: 'dist', //和编译结果输出路路径有关，开发阶段不不⽤用管
  devServer: {
    open: true, //是否开启
    host: 'localhost',
    port: '8080',
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000/api', // 实际后端地址
          ws: true,
          changeOrigin: true,
          pathRewrite: { //url转换
            '^/api': ''
        }
      }
    }
  }
};