class Queue{
    constructor(){ 
        this.dataStorage = [];
    }
    enqueue(element){ 
        this.dataStorage.push(element);
    }
    dequeue(){  
        return this.dataStorage.shift();
    }
    length(){
        return this.dataStorage.length;
    }
    front(){
        return this.dataStorage[0];
    }
    back(){
        return this.dataStorage[this.dataStorage.length -1];
    }
    toString(){ // dataStorage에 저장된 모든 요소를 출력해준다.
        let str = "";
        for(let i = 0; i < this.dataStorage.length; i++){
            str += this.dataStorage[i] + "\n"; 
        }
        return str;
    }   
    clear(){
        this.dataStorage.splice(0,this.dataStorage.length);
    }
    empty(){ // queue가 비어있는지 확인해준다.
        if(this.dataStorage.length > 0){
            return false;
        }else{
            return true;
        }
    }
}

// // 테스트 !



const participant = [
    ['F', 'jeongdo'],
    ['M', 'gildong'],
    ['M', 'taesung'],
    ['F', 'yuri'],
    ['F', 'songe'],
    ['M', 'jeongwoo'],
    ['M', 'giseok'],
    ['M', 'eunseong']
]

function Dancer(name, sex){
    this.name = name;
    this.sex = sex;
}

function classification(group){
    for(let i = 0; i < participant.length; i++){
        let sex = participant[i][0];
        let name = participant[i][1];
        if(participant[i][0] == 'F'){
            femaleDancer.enqueue(new Dancer(name, sex));
        }else{
            maleDancer.enqueue(new Dancer(name, sex));            
        }
    }
}

function getPair(maleDancer, femaleDancer){
    const femaleNumber = femaleDancer.length();
    const maleNumber = maleDancer.length();
    if(femaleNumber >= maleNumber){
        for(let j = 0; j < maleNumber; j++){
            console.log(`${maleDancer.dequeue().name}님은 ${femaleDancer.dequeue().name}님과 파트너가 됐습니다.`);
        }
        console.log(`${femaleDancer.length()}명의 여성분이 남았습니다.`);
    }else if(femaleNumber < maleNumber){
        for(let k = 0; k < femaleNumber; k++){
            console.log(`${maleDancer.dequeue().name}님은 ${femaleDancer.dequeue().name}님과 파트너가 됐습니다.`);
        }
        console.log(`${maleDancer.length()}명의 남성분이 남았습니다.`);
    }
}

const maleDancer = new Queue();
const femaleDancer = new Queue();

classification(participant);
getPair(maleDancer, femaleDancer);







