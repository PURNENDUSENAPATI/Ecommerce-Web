// asynchronous
const fs  = require('fs');
fs.readFile("delete.txt","utf-8",(err,data) =>{
console.log(data);
});
console.log("this is a message");

