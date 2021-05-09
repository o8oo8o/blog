
module.exports = {
    devServer: {
        host: '0.0.0.0',
        port: 8088,
        proxy: {
            '/api': {
                target: 'http://192.168.1.230:8899',
                ws: true,
                secure:false,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api',//重写,
                }
            },
        }
    },
    // publicPath: process.env.NODE_ENV === 'production' ? '/www/' : '/test/'
};


