const proxy = [
    {
      context: '/',
      target: 'http://localhost:5000',
      pathRewrite: {'^/api' : ''}
    }
  ];
  module.exports = proxy;
  