const fs  = require("fs");
let text  = fs.readFileSync("delete.txt","utf-8");
text  = text.replace("chinu","sanu");
console.log(text);

console.log("creat a new file");
fs.writeFileSync("sanu.txt",text);



