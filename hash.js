
function simpleHash(data){
    var total = 0;
    for(var i = 0; i < data.length; i++){
        total += data.charCodeAt(i);
    }
    return total % this.table.length;
}
const table = new Array(137);
console.log(simpleHash(table));

