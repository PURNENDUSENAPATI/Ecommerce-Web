const http = require("http");
const fs  =require('fs');
const file = fs.readFileSync('chinu_shop.html');

const server  = http.createServer((req,res)=>
{
    res.writeHead(200,{'content':'text/html'});
    res.end(file);
});
server.listen(81,'127.0.0.1',()=>
{
    console.log('listen on port80');
});