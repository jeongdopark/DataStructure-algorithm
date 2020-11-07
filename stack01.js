

// class Stack{
//     constructor(){
//         this.dataStorage = [];
//         this.top = 0;
//     }

//     push(element){
//         this.dataStorage[this.top++] = element;
//     }

//     pop(){
//         --this.top;
//         this.dataStorage.pop();
//     }
    
//     peek(){
//         return this.dataStorage[this.top -1];
//     }

//     clear(){
//         this.top = 0;
//     }

//     length(){
//         return this.top;
//     }
// }

// var testStack = new Stack();
// testStack.push('a');
// testStack.push('b');
// testStack.push('d');
// console.log(testStack.dataStorage);
// console.log(testStack.dataStorage.length);

// testStack.pop();
// console.log(testStack.dataStorage);
// console.log(testStack.dataStorage.length);




class Stack{
    constructor(){
        this.dataStorage = [];
        this.top = 0;
    }
    push(element){
        this.dataStorage[this.top++] = element;
    }
    pop(){
        --this.top;
        return this.dataStorage.pop();
    }
    length(){
        return this.top;    
    }
    clear(){
        for(let i = 0; i < this.top; i++){
            this.dataStorage.pop();
        }
    }
    peek(){
        return this.dataStorage[this.top -1];
    }
}

// const test3 = new Stack();
// test3.push('a');
// test3.push('b');
// test3.push('c');
// test3.push('d');
// console.log(test3.top);
// test3.pop();
// console.log(test3.top);




// function test1(word){
//     const test2 = new Stack();
//     for(let i = 0; i < word.length; i++){
//         test2.push(word[i]);
//     }
//     let reverseWord = "";
//     for(let j = 0; j < word.length; j++){
//         reverseWord += test2.pop();
//     }

//     if(word == reverseWord){
//         console.log('true');
//     }else{
//         console.log('false');
//     }
// }

// 빨 노 흰 


const test = ['red','yellow' ,'blue','pink', 'deepblue','white', 'purple'];

function pickColor(arr, color){
    
    const pick = new Stack();
    for(let i = 0; i < arr.length; i++){  // dataStorage에 초기 배열을 넣는다. 
        pick.push(arr[i]); // pick.dataStorage = ['red', 'yellow', 'white']
    }
    
    
    let secondArr = [];
    const picktopNumber = pick.top
    
    
    
    for(let  j = 0; j < picktopNumber; j++){   // secondArr에 원하는 color가 나올 때까지 push한다. , pick top = 3
        let test = pick.pop();
        
        
        if(test == color){
            secondArr[j] = test;
            break;
        }else{
            secondArr[j] = test;
        }
    }    
    
    secondArr.pop();
    
    
    // let thirdArr = [];
    // const pickColor = secondArr.pop()// thirdArr에 원하는 color만 push한다.
    // thirdArr[0] = pickColor;
    const secondArrLength = secondArr.length;   
    for(let x = 0; x < secondArrLength; x++){
        pick.dataStorage[pick.top] = secondArr.pop();
        pick.top ++;        
    }
    
    return pick.dataStorage;
}
console.log(pickColor(test, 'blue'));
console.log(pickColor(test, 'red'));
console.log(pickColor(test, 'yellow'));
console.log(pickColor(test, 'purple'));
















